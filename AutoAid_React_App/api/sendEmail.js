import nodemailer from 'nodemailer';

export default async function handler(req, res) {
  // Only allow POST requests
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  // Basic security check to prevent abuse from random people
  const authHeader = req.headers.authorization;
  if (authHeader !== `Bearer ${process.env.VITE_EMAIL_API_SECRET || 'autoaid-secret-key-123'}`) {
    return res.status(401).json({ error: 'Unauthorized' });
  }

  const { to, subject, html, text } = req.body;

  if (!to || !subject || !html) {
    return res.status(400).json({ error: 'Missing required fields' });
  }

  try {
    // We use the same App Password that works locally, but now on Vercel which allows port 465!
    const transporter = nodemailer.createTransport({
      service: 'gmail',
      host: 'smtp.gmail.com',
      port: 465,
      secure: true,
      auth: {
        user: process.env.VITE_EMAIL_USER || 'umar68408@gmail.com',
        pass: process.env.VITE_EMAIL_PASS
      }
    });

    const mailOptions = {
      from: `"AutoAid" <${process.env.VITE_EMAIL_USER || 'umar68408@gmail.com'}>`,
      to,
      subject,
      text: text || html.replace(/<[^>]*>?/gm, ' ').replace(/\s+/g, ' ').trim(),
      html,
    };

    const info = await transporter.sendMail(mailOptions);
    return res.status(200).json({ success: true, messageId: info.messageId });
  } catch (error) {
    console.error('Vercel SMTP Error:', error);
    return res.status(500).json({ error: error.message });
  }
}
