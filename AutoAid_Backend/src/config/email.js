const nodemailer = require('nodemailer');
const dotenv = require('dotenv');

dotenv.config();

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
  const mailOptions = {
    from: process.env.EMAIL_USER,
    to: to,
    subject: subject,
    html: html,
  };

  await transporter.sendMail(mailOptions);
  console.log(`Email sent to ${to}`);
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
