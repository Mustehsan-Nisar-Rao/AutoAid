import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { FaCheckCircle, FaDownload, FaArrowLeft, FaPrint, FaHome } from 'react-icons/fa';
import { useAuth } from '../context/AuthContext';
import { API_BASE_URL } from '../utils/api';

const ReceiptPage = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const { currentUser } = useAuth();

    const [payment, setPayment] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchPayment = async () => {
            if (!id) return;
            try {
                const res = await fetch(`${API_BASE_URL}/api/payments/${id}`, {
                    credentials: 'include',
                });
                const data = await res.json();
                if (res.ok && data.success) {
                    setPayment(data.payment);
                } else {
                    setError(data.error || 'Could not load receipt.');
                }
            } catch (err) {
                setError('Network error. Could not load receipt.');
            } finally {
                setLoading(false);
            }
        };
        fetchPayment();
    }, [id]);

    const handleDownload = () => {
        window.print();
    };

    const formatDate = (dateStr) => {
        if (!dateStr) return '—';
        return new Date(dateStr).toLocaleString('en-PK', {
            year: 'numeric', month: 'long', day: 'numeric',
            hour: '2-digit', minute: '2-digit',
        });
    };

    if (loading) {
        return (
            <div className="min-h-screen bg-background-light dark:bg-background-dark flex items-center justify-center">
                <div className="flex flex-col items-center gap-4">
                    <div className="w-12 h-12 border-4 border-primary/30 border-t-primary rounded-full animate-spin" />
                    <p className="text-gray-500 dark:text-gray-400">Loading receipt...</p>
                </div>
            </div>
        );
    }

    if (error || !payment) {
        return (
            <div className="min-h-screen bg-background-light dark:bg-background-dark flex items-center justify-center p-6">
                <div className="text-center max-w-sm">
                    <p className="text-red-500 text-xl font-bold mb-2">Receipt Not Found</p>
                    <p className="text-gray-500 mb-6">{error}</p>
                    <button
                        onClick={() => navigate('/')}
                        className="px-6 py-3 bg-primary text-white rounded-xl font-bold hover:bg-primary-dark transition-colors"
                    >
                        Go Home
                    </button>
                </div>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 dark:from-[#0a0f1e] dark:to-[#111827] py-10 px-4 transition-colors duration-300">
            {/* Back Button - hidden on print */}
            <div className="max-w-2xl mx-auto mb-6 flex gap-3 no-print">
                <button
                    onClick={() => navigate(-1)}
                    className="flex items-center gap-2 px-4 py-2 bg-white dark:bg-[#1e293b] text-gray-700 dark:text-gray-300 rounded-xl border border-gray-200 dark:border-gray-700 shadow-sm hover:border-primary/50 transition-all text-sm font-semibold"
                >
                    <FaArrowLeft className="text-xs" /> Back
                </button>
                <button
                    onClick={() => navigate('/')}
                    className="flex items-center gap-2 px-4 py-2 bg-white dark:bg-[#1e293b] text-gray-700 dark:text-gray-300 rounded-xl border border-gray-200 dark:border-gray-700 shadow-sm hover:border-primary/50 transition-all text-sm font-semibold"
                >
                    <FaHome className="text-xs" /> Home
                </button>
            </div>

            {/* Receipt Card */}
            <div
                id="receipt-card"
                className="max-w-2xl mx-auto bg-white dark:bg-[#111827] rounded-3xl shadow-2xl border border-gray-100 dark:border-gray-800 overflow-hidden print-container"
            >
                {/* ─── Header ─── */}
                <div className="bg-gradient-to-r from-primary to-blue-600 p-8 text-white relative overflow-hidden">
                    <div className="absolute inset-0 opacity-10"
                        style={{ backgroundImage: 'radial-gradient(circle at 20% 50%, white 0%, transparent 60%)' }}
                    />
                    <div className="relative z-10 flex items-center gap-5">
                        <div className="w-16 h-16 bg-white/20 backdrop-blur-sm rounded-2xl flex items-center justify-center text-3xl font-black shadow-lg">
                            A
                        </div>
                        <div>
                            <h1 className="text-2xl font-black tracking-tight">AutoAid</h1>
                            <p className="text-primary-100 text-sm opacity-80">Service Receipt</p>
                        </div>
                    </div>
                    <div className="relative z-10 mt-6 flex items-center gap-3">
                        <FaCheckCircle className="text-green-300 text-2xl" />
                        <div>
                            <p className="text-xs opacity-70 uppercase tracking-widest">Status</p>
                            <p className="text-xl font-bold text-green-300">Payment Confirmed</p>
                        </div>
                    </div>
                </div>

                {/* ─── Transaction ID Banner ─── */}
                <div className="bg-gray-50 dark:bg-[#0f172a] border-b border-gray-100 dark:border-gray-800 px-8 py-4 flex items-center justify-between">
                    <div>
                        <p className="text-xs text-gray-500 dark:text-gray-500 uppercase tracking-widest font-semibold mb-0.5">Transaction ID</p>
                        <p className="text-xl font-black text-primary tracking-widest">{payment.transactionId}</p>
                    </div>
                    <span className="px-4 py-2 bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-400 rounded-full text-xs font-bold uppercase tracking-wider border border-green-200 dark:border-green-700">
                        Paid
                    </span>
                </div>

                {/* ─── Details Grid ─── */}
                <div className="p-8 space-y-3">
                    {[
                        { label: 'Receipt Number', value: `#${payment._id?.toString().slice(-8).toUpperCase()}` },
                        { label: 'Customer Name', value: payment.customerName || currentUser?.displayName || '—' },
                        { label: 'Service Provider', value: payment.providerName || '—' },
                        { label: 'Service Type', value: payment.serviceType },
                        { label: 'Payment Method', value: payment.paymentMethod },
                        { label: 'Payment Date', value: formatDate(payment.paidAt) },
                    ].map(({ label, value }) => (
                        <div key={label} className="flex items-start justify-between py-3 border-b border-gray-100 dark:border-gray-800 last:border-0">
                            <span className="text-sm text-gray-500 dark:text-gray-400 font-medium w-40 flex-shrink-0">{label}</span>
                            <span className="text-sm text-gray-900 dark:text-white font-semibold text-right flex-1">{value}</span>
                        </div>
                    ))}

                    {/* Amount highlighted row */}
                    <div className="mt-4 bg-gradient-to-r from-primary/10 to-blue-500/10 dark:from-primary/15 dark:to-blue-600/15 rounded-2xl p-5 border border-primary/20">
                        <div className="flex items-center justify-between">
                            <span className="text-sm text-gray-600 dark:text-gray-400 font-semibold uppercase tracking-wider">Total Paid</span>
                            <span className="text-3xl font-black text-primary">
                                PKR {payment.amount?.toLocaleString()}
                            </span>
                        </div>
                    </div>
                </div>

                {/* ─── Footer Note ─── */}
                <div className="px-8 pb-6 text-center">
                    <p className="text-xs text-gray-400 dark:text-gray-600">
                        This is a simulated receipt generated by AutoAid (Academic FYP Project).<br />
                        No actual financial transaction has taken place.
                    </p>
                </div>

                {/* ─── Download Button - hidden on print ─── */}
                <div className="px-8 pb-8 no-print">
                    <button
                        onClick={handleDownload}
                        className="w-full flex items-center justify-center gap-3 py-4 px-6 rounded-2xl bg-gradient-to-r from-primary to-blue-600 text-white font-bold text-base shadow-lg hover:shadow-primary/30 hover:scale-[1.01] transition-all duration-300"
                    >
                        <FaPrint />
                        Download / Print Receipt
                    </button>
                </div>
            </div>

            {/* Print Styles */}
            <style>{`
                @media print {
                    .no-print { display: none !important; }
                    body { background: white !important; }
                    .print-container {
                        box-shadow: none !important;
                        border-radius: 0 !important;
                        border: none !important;
                        max-width: 100% !important;
                    }
                }
            `}</style>
        </div>
    );
};

export default ReceiptPage;
