const express = require('express');
const router = express.Router();
const { createPayment, getPaymentById, getProviderStats } = require('../controllers/paymentController');
const { protect } = require('../middleware/authMiddleware');

// POST /api/payments/create
router.post('/create', protect, createPayment);

// GET /api/payments/provider/stats
router.get('/provider/stats', protect, getProviderStats);

// GET /api/payments/:id
router.get('/:id', protect, getPaymentById);

module.exports = router;
