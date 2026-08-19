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

const transporter = nodemailer.createTransport({
  host: 'smtp.gmail.com',
  port: 465,
  secure: true,
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASS,
  },
  family: 4, // Force IPv4 to avoid IPv6 connection timeouts on Render
});

const sendEmail = async (to, subject, html) => {
  // Method 1: Resend HTTP API (Recommended for Render free tier)
  if (process.env.RESEND_API_KEY) {
    try {
      const res = await postRequest(
        'https://api.resend.com/emails',
        { 'Authorization': `Bearer ${process.env.RESEND_API_KEY}` },
        {
          from: 'AutoAid <onboarding@resend.dev>',
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
      throw error;
    }
  }

  // Method 2: Brevo HTTP API (Alternative for Render free tier)
  if (process.env.BREVO_API_KEY) {
    try {
      const res = await postRequest(
        'https://api.brevo.com/v3/smtp/email',
        { 'api-key': process.env.BREVO_API_KEY },
        {
          sender: { name: 'AutoAid', email: process.env.EMAIL_USER || 'no-reply@autoaid.com' },
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
      throw error;
    }
  }

  // Fallback: SMTP (For local dev where ports are not blocked)
  const mailOptions = {
    from: process.env.EMAIL_USER,
    to: to,
    subject: subject,
    html: html,
  };

  await transporter.sendMail(mailOptions);
  console.log(`Email sent to ${to} via SMTP`);
};

const sendOtpEmail = async (email, otp) => {
    const subject = 'AutoAid Account Verification OTP';
    const html = `
      <div style="font-family: Arial, sans-serif; padding: 20px;">
        <h2>Welcome to AutoAid!</h2>
        <p>Your OTP for account verification is:</p>
        <h1 style="color: #007bff; letter-spacing: 5px;">${otp}</h1>
        <p>This code expires in 5 minutes.</p>
        <p>If you did not request this, please ignore this email.</p>
      </div>
    `;
    await sendEmail(email, subject, html);
};

module.exports = { sendOtpEmail, sendEmail };
