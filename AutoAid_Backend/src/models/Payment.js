const mongoose = require('mongoose');

const PaymentSchema = new mongoose.Schema({
    userId: {
        type: String, // Firebase UID
        required: true,
        ref: 'User'
    },
    providerId: {
        type: String, // Provider's MongoDB ObjectId as string
        required: true,
        ref: 'User'
    },
    serviceRequestId: {
        type: mongoose.Schema.Types.ObjectId,
        required: true,
        ref: 'ServiceRequest'
    },
    serviceType: {
        type: String,
        required: true
    },
    amount: {
        type: Number,
        required: true,
        min: 0
    },
    paymentMethod: {
        type: String,
        enum: ['JazzCash', 'Easypaisa', 'Cash on Service'],
        required: true
    },
    paymentStatus: {
        type: String,
        enum: ['Pending', 'Paid', 'Failed', 'Refunded'],
        default: 'Paid'
    },
    transactionId: {
        type: String,
        required: true,
        unique: true
    },
    paidAt: {
        type: Date,
        default: Date.now
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model('Payment', PaymentSchema);
