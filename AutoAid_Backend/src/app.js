const express = require('express');
const dotenv = require('dotenv');
const cors = require('cors');
const connectDB = require('./config/db');
const cookieParser = require('cookie-parser');
const http = require('http');
const { Server } = require('socket.io');
const ServiceRequest = require('./models/ServiceRequest');

// Load env vars
dotenv.config();

const app = express();
const server = http.createServer(app);

// Allowed origins: comma-separated list from env, or default to localhost
const rawOrigins = process.env.CORS_ORIGIN
    ? process.env.CORS_ORIGIN.split(',')
    : ['http://localhost:5173', 'http://localhost:3000'];

const ALLOWED_ORIGINS = rawOrigins.map(origin => origin.trim().replace(/\/$/, ''));

const checkCorsOrigin = (origin, callback) => {
    if (!origin) return callback(null, true);
    const cleanOrigin = origin.replace(/\/$/, '');
    if (
        ALLOWED_ORIGINS.includes(cleanOrigin) ||
        ALLOWED_ORIGINS.includes('*') ||
        cleanOrigin.endsWith('.vercel.app')
    ) {
        return callback(null, true);
    }
    return callback(null, true); // Allow for seamless cross-domain deployment
};

// Configure Socket.IO
const io = new Server(server, {
    cors: {
        origin: checkCorsOrigin,
        credentials: true
    }
});

// Map to store connected providers: { [userId]: socketId }
const connectedProviders = new Map();
// Map to store connected users: { [userId]: socketId }
const connectedUsers = new Map();

io.on('connection', (socket) => {
    console.log('A user connected:', socket.id);

    // Provider joins room/registers with their userId
    socket.on('register_provider', (userId) => {
        if (userId) {
            connectedProviders.set(String(userId), socket.id);
            console.log(`Provider ${userId} registered with socket ${socket.id}`);
        }
    });

    // User registers with their userId
    socket.on('register_user', (userId) => {
        if (userId) {
            connectedUsers.set(String(userId), socket.id);
            console.log(`User ${userId} registered with socket ${socket.id}. Total connected users: ${connectedUsers.size}`);
        }
    });

    socket.on('disconnect', () => {
        console.log('User disconnected:', socket.id);
        // Remove from provider map if applicable
        for (let [userId, socketId] of connectedProviders.entries()) {
            if (socketId === socket.id) {
                connectedProviders.delete(userId);
                console.log(`Provider ${userId} unregistered`);
                break;
            }
        }
        // Remove from user map if applicable
        for (let [userId, socketId] of connectedUsers.entries()) {
            if (socketId === socket.id) {
                connectedUsers.delete(userId);
                console.log(`User ${userId} unregistered`);
                break;
            }
        }
    });

    // Chat Events
    socket.on('join_job_room', (requestId) => {
        if (requestId) {
            socket.join(`job_${requestId}`);
            console.log(`Socket ${socket.id} joined room job_${requestId}`);
        }
    });

    socket.on('send_job_message', async ({ requestId, senderId, senderModel, text }) => {
        try {
            const request = await ServiceRequest.findById(requestId);
            if (request && ['Accepted', 'In Progress'].includes(request.status)) {
                const message = {
                    senderId,
                    senderModel,
                    text,
                    timestamp: new Date(),
                    seen: false
                };
                request.messages.push(message);
                await request.save();
                
                io.to(`job_${requestId}`).emit('new_job_message', message);
            }
        } catch (error) {
            console.error('Error saving message:', error);
        }
    });

    socket.on('mark_messages_seen', async ({ requestId, readerId }) => {
        try {
            const request = await ServiceRequest.findById(requestId);
            if (request) {
                let updated = false;
                request.messages.forEach(msg => {
                    // If message is NOT from the reader, mark as seen
                    if (msg.senderId !== readerId && !msg.seen) {
                        msg.seen = true;
                        updated = true;
                    }
                });
                if (updated) {
                    await request.save();
                    io.to(`job_${requestId}`).emit('messages_updated', request.messages);
                }
            }
        } catch (error) {
             console.error('Error marking messages as seen:', error);
        }
    });

});

// Make io and connectedProviders available to routes
app.set('io', io);
app.set('connectedProviders', connectedProviders);
app.set('connectedUsers', connectedUsers);

// Middleware
app.use(express.json());
app.use(cookieParser());
app.use(cors({
    origin: checkCorsOrigin,
    credentials: true
}));

// Serve static files
app.use('/uploads', express.static('uploads'));

// Routes
app.use('/api/auth', require('./routes/authRoutes'));
app.use('/api/services', require('./routes/serviceRoutes'));
app.use('/api/admin', require('./routes/adminRoutes'));
app.use('/api/contact', require('./routes/contactRoutes'));
app.use('/api/recommend', require('./routes/recommenderRoutes'));
app.use('/api/nha', require('./routes/nhaRoutes'));
app.use('/api/payments', require('./routes/paymentRoutes'));

app.get(['/', '/health', '/api/health'], (req, res) => {
  res.status(200).json({ status: 'ok', message: 'AutoAid Backend is running' });
});

const PORT = process.env.PORT || 3000;

server.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running on port ${PORT} bound to 0.0.0.0`);
  connectDB().catch(err => console.error('Background DB Connection Error:', err.message));
});
