const nodemailer = require('nodemailer');
const dotenv = require('dotenv');
const https = require('https');

dotenv.config();

// Helper to make HTTPS POST requests without external dependencies
const postRequest = (url, headers, body) => {
  return new Promise((resolve, reject) => {
    const u = new URL(url);
    const options = {
      hostname: u.hostname,
      path: u.pathname,
      method: 'POST',
      headers: {
        ...headers,
        'Content-Type': 'application/json',
      }
    };

    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', (chunk) => { data += chunk; });
      res.on('end', () => {
        resolve({
          ok: res.statusCode >= 200 && res.statusCode < 300,
          status: res.statusCode,
          body: data
        });
      });
    });

    req.on('error', (err) => { reject(err); });
    req.write(JSON.stringify(body));
    req.end();
  });
};

const getCleanEnv = (key, fallback = '') => {
  const val = process.env[key] || fallback;
  return val.trim().replace(/^["']|["']$/g, '');
};

const createGmailTransporter = (port, secure) => {
  const user = getCleanEnv('EMAIL_USER');
  const pass = getCleanEnv('EMAIL_PASS');
  return nodemailer.createTransport({
    service: 'gmail',
    host: 'smtp.gmail.com',
    port: port,
    secure: secure,
    auth: { user, pass },
    tls: { rejectUnauthorized: false },
    connectionTimeout: 8000,
    socketTimeout: 8000,
    family: 4,
  });
};

const sendEmail = async (to, subject, html) => {
  const senderName = 'AutoAid';
  const rawEmail = getCleanEnv('EMAIL_USER', 'umar68408@gmail.com');

  // Method 1: Resend HTTP API (Recommended for Render free tier)
  if (process.env.RESEND_API_KEY) {
    try {
      const res = await postRequest(
        'https://api.resend.com/emails',
        { 'Authorization': `Bearer ${process.env.RESEND_API_KEY}` },
        {
          from: `${senderName} <onboarding@resend.dev>`,
          to: [to],
          subject: subject,
          html: html
        }
      );
      if (!res.ok) {
        throw new Error(`Resend API failed with status ${res.status}: ${res.body}`);
      }
      console.log(`Email sent to ${to} via Resend HTTP API`);
      return;
    } catch (error) {
      console.error('Resend HTTP API failed:', error);
    }
  }

  // Method 2: Brevo HTTP API (Alternative for Render free tier)
  if (process.env.BREVO_API_KEY) {
    try {
      const res = await postRequest(
        'https://api.brevo.com/v3/smtp/email',
        { 'api-key': process.env.BREVO_API_KEY },
        {
          sender: { name: senderName, email: rawEmail },
          to: [{ email: to }],
          subject: subject,
          htmlContent: html
        }
      );
      if (!res.ok) {
        throw new Error(`Brevo API failed with status ${res.status}: ${res.body}`);
      }
      console.log(`Email sent to ${to} via Brevo HTTP API`);
      return;
    } catch (error) {
      console.error('Brevo HTTP API failed:', error);
    }
  }

  // Method 3: Primary SMTP (Gmail Port 465)
  const mailOptions = {
    from: `"${senderName}" <${rawEmail}>`,
    to: to,
    subject: subject,
    html: html,
  };

  try {
    const primaryTransporter = createGmailTransporter(465, true);
    await primaryTransporter.sendMail(mailOptions);
    console.log(`Email sent to ${to} via Gmail SMTP (Port 465)`);
    return;
  } catch (err465) {
    console.warn(`Gmail SMTP Port 465 failed: ${err465.message}. Trying Port 587...`);
  }

  // Method 4: Fallback SMTP (Gmail Port 587)
  try {
    const secondaryTransporter = createGmailTransporter(587, false);
    await secondaryTransporter.sendMail(mailOptions);
    console.log(`Email sent to ${to} via Gmail SMTP (Port 587)`);
    return;
  } catch (err587) {
    console.error(`Gmail SMTP Port 587 failed: ${err587.message}`);
    throw new Error(`Failed to send email via SMTP: ${err587.message}`);
  }
};

const sendOtpEmail = async (email, otp) => {
    const subject = 'Your AutoAid Verification Code';
    const html = `
      <!DOCTYPE html>
      <html>
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AutoAid Verification Code</title>
      </head>
      <body style="margin: 0; padding: 0; background-color: #F8FAFC; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;">
        <table role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0" style="background-color: #F8FAFC; padding: 40px 10px;">
          <tr>
            <td align="center">
              <table role="presentation" width="100%" max-width="520" border="0" cellspacing="0" cellpadding="0" style="max-width: 520px; background-color: #FFFFFF; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.01); border: 1px solid #E2E8F0;">
                
                <!-- Header Banner -->
                <tr>
                  <td style="background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%); padding: 32px 40px; text-align: center;">
                    <table role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td align="center">
                          <div style="display: inline-block; background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%); padding: 10px 20px; border-radius: 12px; font-size: 22px; font-weight: 800; color: #FFFFFF; letter-spacing: 1px; box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);">
                            🚗 Auto<span style="color: #60A5FA;">Aid</span>
                          </div>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>

                <!-- Content Body -->
                <tr>
                  <td style="padding: 40px 40px 32px 40px;">
                    <h1 style="margin: 0 0 12px 0; font-size: 24px; font-weight: 700; color: #0F172A; text-align: center;">
                      Verify Your Account
                    </h1>
                    <p style="margin: 0 0 28px 0; font-size: 15px; line-height: 24px; color: #475569; text-align: center;">
                      Please use the 6-digit verification code below to complete your authentication on AutoAid:
                    </p>

                    <!-- OTP Box -->
                    <table role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-bottom: 28px;">
                      <tr>
                        <td align="center">
                          <div style="background-color: #F1F5F9; border: 2px dashed #CBD5E1; border-radius: 12px; padding: 20px 24px; text-align: center; width: fit-content;">
                            <span style="font-family: 'Courier New', Courier, monospace, monospace; font-size: 38px; font-weight: 800; color: #1E293B; letter-spacing: 12px; display: inline-block; margin-left: 12px;">
                              ${otp}
                            </span>
                          </div>
                        </td>
                      </tr>
                    </table>

                    <!-- Expiration Notice -->
                    <div style="background-color: #FEF3C7; border-left: 4px solid #F59E0B; border-radius: 8px; padding: 14px 16px; margin-bottom: 28px;">
                      <p style="margin: 0; font-size: 13px; line-height: 18px; color: #92400E; font-weight: 500;">
                        ⏳ <strong>Time-sensitive:</strong> This code will expire in <strong>5 minutes</strong>. Do not share this code with anyone.
                      </p>
                    </div>

                    <p style="margin: 0; font-size: 13px; line-height: 20px; color: #64748B; text-align: center;">
                      If you did not request this verification code, you can safely ignore this email.
                    </p>
                  </td>
                </tr>

                <!-- Divider -->
                <tr>
                  <td style="padding: 0 40px;">
                    <div style="border-top: 1px solid #E2E8F0;"></div>
                  </td>
                </tr>

                <!-- Footer -->
                <tr>
                  <td style="padding: 24px 40px; background-color: #F8FAFC; text-align: center;">
                    <p style="margin: 0 0 6px 0; font-size: 12px; color: #94A3B8; font-weight: 500;">
                      AutoAid Roadside Assistance & Service Platform
                    </p>
                    <p style="margin: 0; font-size: 11px; color: #CBD5E1;">
                      © 2026 AutoAid Inc. All rights reserved.
                    </p>
                  </td>
                </tr>

              </table>
            </td>
          </tr>
        </table>
      </body>
      </html>
    `;
    await sendEmail(email, subject, html);
};

module.exports = { sendOtpEmail, sendEmail };
