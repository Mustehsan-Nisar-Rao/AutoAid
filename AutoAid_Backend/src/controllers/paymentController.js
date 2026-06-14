const Payment = require('../models/Payment');
const ServiceRequest = require('../models/ServiceRequest');
const User = require('../models/User');

// Generate a unique transaction ID: AUTO-XXXXXXXX (8 random digits)
function generateTransactionId() {
    const digits = Math.floor(10000000 + Math.random() * 90000000).toString();
    return `AUTO-${digits}`;
}

// @desc    Create a new simulated payment
// @route   POST /api/payments/create
// @access  Private (User)
exports.createPayment = async (req, res) => {
    try {
        const { serviceRequestId, amount, paymentMethod } = req.body;
        const userId = req.user.uid;

        if (!serviceRequestId || amount == null || !paymentMethod) {
            return res.status(400).json({ error: 'serviceRequestId, amount, and paymentMethod are required' });
        }
        if (isNaN(Number(amount)) || Number(amount) < 0) {
            return res.status(400).json({ error: 'amount must be a valid non-negative number' });
        }

        // Verify the service request exists and is Completed
        const serviceRequest = await ServiceRequest.findById(serviceRequestId);
        if (!serviceRequest) {
            return res.status(404).json({ error: 'Service request not found' });
        }
        if (serviceRequest.status !== 'Completed') {
            return res.status(400).json({ error: 'Payment is only allowed for completed service requests' });
        }
        if (serviceRequest.userId !== userId) {
            return res.status(403).json({ error: 'Not authorized to pay for this request' });
        }

        // Check if payment already exists for this service request
        const existingPayment = await Payment.findOne({ serviceRequestId });
        if (existingPayment) {
            return res.status(409).json({
                error: 'Payment already processed for this service request',
                payment: existingPayment
            });
        }

        // Generate unique transaction ID (retry if collision)
        let transactionId;
        let attempts = 0;
        do {
            transactionId = generateTransactionId();
            attempts++;
        } while (await Payment.findOne({ transactionId }) && attempts < 10);

        const payment = new Payment({
            userId,
            providerId: serviceRequest.providerId,
            serviceRequestId,
            serviceType: serviceRequest.serviceType,
            amount: Number(amount),
            paymentMethod,
            paymentStatus: 'Paid',
            transactionId,
            paidAt: new Date()
        });

        await payment.save();

        res.status(201).json({
            success: true,
            message: 'Payment processed successfully',
            payment
        });
    } catch (error) {
        console.error('Error creating payment:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
};

// @desc    Get payment by ID (for receipt)
// @route   GET /api/payments/:id
// @access  Private
exports.getPaymentById = async (req, res) => {
    try {
        const { id } = req.params;

        const payment = await Payment.findById(id);
        if (!payment) {
            return res.status(404).json({ error: 'Payment not found' });
        }

        // Fetch user (customer) details
        const customer = await User.findOne({ uid: payment.userId });
        // Fetch provider details
        const provider = await User.findById(payment.providerId);

        res.status(200).json({
            success: true,
            payment: {
                ...payment._doc,
                customerName: customer ? customer.fullName : 'Customer',
                providerName: provider ? provider.fullName : 'Service Provider'
            }
        });
    } catch (error) {
        console.error('Error fetching payment:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
};
// @desc    Get Provider Stats
// @route   GET /api/payments/provider/stats
// @access  Private (Provider)
exports.getProviderStats = async (req, res) => {
    try {
        const providerId = req.user._id.toString();

        // Find all paid payments for this provider
        const payments = await Payment.find({ providerId, paymentStatus: 'Paid' });

        const totalEarnings = payments.reduce((sum, p) => sum + p.amount, 0);

        // Group by month
        const monthlyEarnings = {};
        payments.forEach(p => {
            const date = new Date(p.paidAt || p.createdAt);
            const monthYear = date.toLocaleString('default', { month: 'short', year: 'numeric' });
            if (!monthlyEarnings[monthYear]) {
                monthlyEarnings[monthYear] = 0;
            }
            monthlyEarnings[monthYear] += p.amount;
        });

        // Convert to array suitable for charts
        const earningsData = Object.keys(monthlyEarnings).map(month => ({
            month,
            amount: monthlyEarnings[month]
        })).sort((a, b) => new Date(a.month) - new Date(b.month)); // Sort chronological if possible

        res.status(200).json({
            success: true,
            stats: {
                totalEarnings,
                earningsData
            }
        });

    } catch (error) {
        console.error('Error fetching provider stats:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
};
