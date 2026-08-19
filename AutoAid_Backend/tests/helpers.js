// tests/helpers.js  — Shared utilities for AutoAid IDT test runner
const http = require('http');

const BASE_URL = 'http://localhost:3000';

// ── Simple HTTP client (no external deps) ──────────────────────────────────
function request(method, path, body, cookieHeader) {
    return new Promise((resolve) => {
        const payload = body ? JSON.stringify(body) : null;
        const options = {
            hostname: 'localhost',
            port: 3000,
            path,
            method,
            headers: {
                'Content-Type': 'application/json',
                ...(payload ? { 'Content-Length': Buffer.byteLength(payload) } : {}),
                ...(cookieHeader ? { Cookie: cookieHeader } : {})
            }
        };
        const req = http.request(options, (res) => {
            let data = '';
            res.on('data', chunk => { data += chunk; });
            res.on('end', () => {
                let json;
                try { json = JSON.parse(data); } catch { json = { raw: data }; }
                resolve({ status: res.statusCode, headers: res.headers, body: json });
            });
        });
        req.on('error', (err) => resolve({ status: 0, body: { error: err.message } }));
        if (payload) req.write(payload);
        req.end();
    });
}

// ── Test runner ────────────────────────────────────────────────────────────
let results = [];

function clearResults() {
    results = [];
}

async function runTest(id, description, fn) {
    try {
        const result = await fn();
        const pass = result.pass === true;
        results.push({ id, description, pass, note: result.note || '', actual: result.actual || '' });
        const icon = pass ? '✅' : '❌';
        console.log(`  ${icon} ${id}: ${description}`);
        if (!pass) console.log(`       FAIL → ${result.note}`);
    } catch (err) {
        results.push({ id, description, pass: false, note: `Exception: ${err.message}`, actual: '' });
        console.log(`  ❌ ${id}: ${description}`);
        console.log(`       ERROR → ${err.message}`);
    }
}

function printSummary(moduleName) {
    const passed = results.filter(r => r.pass).length;
    const failed = results.filter(r => !r.pass).length;
    console.log(`\n${'─'.repeat(60)}`);
    console.log(`  Module: ${moduleName}`);
    console.log(`  Passed : ${passed} / ${results.length}`);
    console.log(`  Failed : ${failed} / ${results.length}`);
    console.log(`${'─'.repeat(60)}\n`);
    const savedResults = [...results];
    results = []; // Clear for next module
    return savedResults;
}

// ── Frontend validation helpers (replicate JS logic) ──────────────────────
function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(String(email).toLowerCase());
}

function validateEmailContact(email) {
    // Contact Us has stricter check: must have @ and match /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
    if (!email.includes('@')) return false;
    return /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email);
}

function validatePakistaniPhone(number) {
    return /^(0)(3\d{9}|[1-9]\d{9})$/.test(number);
}

function validatePakistaniPhoneService(number) {
    // Service forms use slightly different regex: /^(03\d{2}-?\d{7})$/
    return /^(03\d{2}-?\d{7})$/.test(number.replace(/\s/g, ''));
}

function validateModelYear(text) {
    const currentYear = new Date().getFullYear();
    const match = text.match(/\b(19[5-9]\d|20[0-2]\d)\b/);
    if (!match) return { isValid: false, error: 'No valid year found (1950–' + currentYear + ')' };
    const year = parseInt(match[0]);
    if (year < 1950 || year > currentYear) return { isValid: false, error: 'Year out of range' };
    return { isValid: true };
}

function filterAlpha(value) {
    return value.replace(/[^a-zA-Z\s]/g, '');
}

function filterDigits(value) {
    return value.replace(/\D/g, '').slice(0, 11);
}

function calculateAge(dob) {
    const birth = new Date(dob);
    const today = new Date();
    let age = today.getFullYear() - birth.getFullYear();
    const m = today.getMonth() - birth.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birth.getDate())) age--;
    return age;
}

module.exports = {
    request, runTest, printSummary, results, clearResults,
    validateEmail, validateEmailContact, validatePakistaniPhone, validatePakistaniPhoneService,
    validateModelYear, filterAlpha, filterDigits, calculateAge
};
