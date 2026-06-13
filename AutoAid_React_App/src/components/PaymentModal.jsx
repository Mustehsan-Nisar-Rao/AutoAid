import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { FaTimes, FaCheckCircle, FaSpinner, FaEdit } from 'react-icons/fa';

const PAYMENT_METHODS = [
    { id: 'JazzCash', label: 'JazzCash', icon: '🟠', desc: 'Mobile wallet payment' },
    { id: 'Easypaisa', label: 'Easypaisa', icon: '🟢', desc: 'Telenor mobile payment' },
    { id: 'Cash on Service', label: 'Cash on Service', icon: '💵', desc: 'Pay directly to provider' },
];

/**
 * PaymentModal Component
 * Props:
 *   isOpen           {bool}
 *   onClose          {fn}
 *   serviceRequestId {string}
 *   serviceType      {string}
 *   providerName     {string}
 *   amount           {number}  — pre-calculated suggested amount
 *   currentUser      {object}  Firebase user
 */
const PaymentModal = ({
    isOpen,
    onClose,
    serviceRequestId,
    serviceType,
    providerName,
    amount,
    currentUser
}) => {
    const navigate = useNavigate();
    const [selectedMethod, setSelectedMethod] = useState('');
    const [finalAmount, setFinalAmount] = useState(amount || 0);
    const [editingAmount, setEditingAmount] = useState(false);
    const [loading, setLoading] = useState(false);
    const [paid, setPaid] = useState(false);
    const [paidAmount, setPaidAmount] = useState(0);
    const [transactionId, setTransactionId] = useState('');
    const [paymentId, setPaymentId] = useState('');
    const [paymentError, setPaymentError] = useState('');

    if (!isOpen) return null;

    const handleConfirmPayment = async () => {
        if (!selectedMethod) {
            setPaymentError('Please select a payment method.');
            return;
        }
        if (!serviceRequestId) {
            setPaymentError('Service request ID is missing. Please try again.');
            return;
        }
        const amountToSend = Number(finalAmount) || 0;
        setPaymentError('');
        setLoading(true);
        try {
            const res = await fetch('http://localhost:3000/api/payments/create', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                credentials: 'include',
                body: JSON.stringify({
                    serviceRequestId,
                    amount: amountToSend,
                    paymentMethod: selectedMethod,
                }),
            });
            const data = await res.json();
            if (res.ok && data.success) {
                setTransactionId(data.payment.transactionId);
                setPaymentId(data.payment._id);
                setPaidAmount(data.payment.amount);
                setPaid(true);
            } else if (res.status === 409 && data.payment) {
                // Already paid
                setTransactionId(data.payment.transactionId);
                setPaymentId(data.payment._id);
                setPaidAmount(data.payment.amount);
                setPaid(true);
            } else {
                setPaymentError(data.error || 'Payment failed. Please try again.');
            }
        } catch (err) {
            console.error('Payment error:', err);
            setPaymentError('Network error. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    const handleViewReceipt = () => {
        navigate(`/receipt/${paymentId}`);
        onClose();
    };

    return (
        <div
            style={{
                position: 'fixed', inset: 0,
                background: 'rgba(0,0,0,0.75)',
                backdropFilter: 'blur(8px)',
                display: 'flex', alignItems: 'center', justifyContent: 'center',
                zIndex: 99999, padding: '16px',
                animation: 'fadeInOverlay 0.25s ease-out',
            }}
            onClick={(e) => { if (e.target === e.currentTarget && !paid) onClose(); }}
        >
            <div style={{
                background: 'linear-gradient(145deg, #0f172a, #1e293b)',
                borderRadius: '24px',
                width: '100%', maxWidth: '460px',
                boxShadow: '0 32px 80px rgba(0,0,0,0.7), 0 0 0 1px rgba(6,182,212,0.15)',
                border: '1px solid rgba(255,255,255,0.08)',
                overflow: 'hidden',
                animation: 'slideUpModal 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)',
            }}>
                {/* ─── Header ─── */}
                <div style={{
                    background: 'linear-gradient(135deg, #06b6d4, #3b82f6)',
                    padding: '24px 24px 20px',
                    position: 'relative',
                }}>
                    {!paid && (
                        <button
                            onClick={onClose}
                            style={{
                                position: 'absolute', top: '16px', right: '16px',
                                background: 'rgba(255,255,255,0.15)', border: 'none',
                                borderRadius: '50%', width: '32px', height: '32px',
                                color: 'white', cursor: 'pointer', fontSize: '14px',
                                display: 'flex', alignItems: 'center', justifyContent: 'center',
                            }}
                        >
                            <FaTimes />
                        </button>
                    )}
                    <div style={{ fontSize: '28px', marginBottom: '8px' }}>💳</div>
                    <h2 style={{ margin: 0, color: 'white', fontSize: '20px', fontWeight: 800 }}>
                        {paid ? 'Payment Successful' : 'Complete Payment'}
                    </h2>
                    <p style={{ margin: '4px 0 0', color: 'rgba(255,255,255,0.75)', fontSize: '13px' }}>
                        {paid ? 'Your transaction has been processed' : 'Secure & simulated payment'}
                    </p>
                </div>

                <div style={{ padding: '24px' }}>
                    {paid ? (
                        /* ─── Success View ─── */
                        <div style={{ textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '16px' }}>
                            <div style={{
                                width: '72px', height: '72px',
                                background: 'rgba(16,185,129,0.15)',
                                borderRadius: '50%', display: 'flex',
                                alignItems: 'center', justifyContent: 'center',
                                animation: 'popIn 0.4s ease-out',
                            }}>
                                <FaCheckCircle style={{ color: '#10b981', fontSize: '36px' }} />
                            </div>

                            <div style={{ background: 'rgba(6,182,212,0.08)', borderRadius: '14px', padding: '16px 24px', width: '100%', border: '1px solid rgba(6,182,212,0.15)' }}>
                                <p style={{ margin: '0 0 4px', fontSize: '12px', color: '#64748b', fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.05em' }}>Transaction ID</p>
                                <p style={{ margin: 0, fontSize: '22px', fontWeight: 800, color: '#06b6d4', letterSpacing: '0.03em' }}>{transactionId}</p>
                            </div>

                            <div style={{ width: '100%', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                                {[
                                    { label: 'Service', value: serviceType },
                                    { label: 'Provider', value: providerName },
                                    { label: 'Amount Paid', value: `PKR ${paidAmount?.toLocaleString()}` },
                                ].map(({ label, value }) => (
                                    <div key={label} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '10px 14px', background: 'rgba(255,255,255,0.03)', borderRadius: '10px', border: '1px solid rgba(255,255,255,0.06)' }}>
                                        <span style={{ fontSize: '13px', color: '#64748b' }}>{label}</span>
                                        <span style={{ fontSize: '13px', fontWeight: 700, color: '#f1f5f9' }}>{value}</span>
                                    </div>
                                ))}
                            </div>

                            <div style={{ width: '100%', display: 'flex', flexDirection: 'column', gap: '10px', marginTop: '4px' }}>
                                <button
                                    onClick={handleViewReceipt}
                                    style={{
                                        width: '100%', padding: '14px',
                                        background: 'linear-gradient(135deg, #06b6d4, #3b82f6)',
                                        border: 'none', borderRadius: '12px',
                                        color: 'white', fontWeight: 700, fontSize: '15px',
                                        cursor: 'pointer', transition: 'all 0.2s',
                                    }}
                                >
                                    📄 View Receipt
                                </button>
                                <button
                                    onClick={onClose}
                                    style={{
                                        width: '100%', padding: '12px',
                                        background: 'transparent',
                                        border: '1px solid rgba(255,255,255,0.1)', borderRadius: '12px',
                                        color: '#94a3b8', fontWeight: 600, fontSize: '14px',
                                        cursor: 'pointer',
                                    }}
                                >
                                    Close
                                </button>
                            </div>
                        </div>
                    ) : (
                        /* ─── Payment Form View ─── */
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
                            {/* Order Summary */}
                            <div style={{ background: 'rgba(255,255,255,0.03)', borderRadius: '14px', padding: '16px', border: '1px solid rgba(255,255,255,0.07)' }}>
                                <p style={{ margin: '0 0 12px', fontSize: '11px', color: '#64748b', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.05em' }}>Order Summary</p>
                                {[
                                    { label: 'Service', value: serviceType },
                                    { label: 'Provider', value: providerName || '—' },
                                ].map(({ label, value }) => (
                                    <div key={label} style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
                                        <span style={{ fontSize: '13px', color: '#64748b' }}>{label}</span>
                                        <span style={{ fontSize: '13px', color: '#f1f5f9', fontWeight: 600 }}>{value}</span>
                                    </div>
                                ))}
                                {/* Editable Amount Row */}
                                <div style={{ borderTop: '1px solid rgba(255,255,255,0.08)', marginTop: '10px', paddingTop: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                    <span style={{ fontSize: '14px', color: '#94a3b8', fontWeight: 600 }}>Total Amount</span>
                                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                        {editingAmount ? (
                                            <input
                                                type="number"
                                                value={finalAmount}
                                                onChange={e => setFinalAmount(Number(e.target.value))}
                                                onBlur={() => setEditingAmount(false)}
                                                autoFocus
                                                min={0}
                                                style={{
                                                    width: '100px', padding: '4px 8px',
                                                    background: '#0f172a', border: '1.5px solid #06b6d4',
                                                    borderRadius: '8px', color: '#06b6d4',
                                                    fontSize: '18px', fontWeight: 800, textAlign: 'right',
                                                    outline: 'none',
                                                }}
                                            />
                                        ) : (
                                            <span style={{ fontSize: '20px', fontWeight: 800, color: '#06b6d4' }}>
                                                PKR {finalAmount.toLocaleString()}
                                            </span>
                                        )}
                                        <button
                                            onClick={() => setEditingAmount(e => !e)}
                                            title="Edit amount"
                                            style={{
                                                background: 'rgba(6,182,212,0.1)', border: '1px solid rgba(6,182,212,0.2)',
                                                borderRadius: '6px', color: '#06b6d4', cursor: 'pointer',
                                                padding: '4px 6px', display: 'flex', alignItems: 'center',
                                            }}
                                        >
                                            <FaEdit style={{ fontSize: '11px' }} />
                                        </button>
                                    </div>
                                </div>
                                <p style={{ margin: '6px 0 0', fontSize: '11px', color: '#475569', textAlign: 'right' }}>
                                    ✏️ Tap edit to adjust the amount if needed
                                </p>
                            </div>

                            {/* Payment Method Selection */}
                            <div>
                                <p style={{ margin: '0 0 12px', fontSize: '11px', color: '#64748b', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.05em' }}>Payment Method</p>
                                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                                    {PAYMENT_METHODS.map(method => (
                                        <button
                                            key={method.id}
                                            onClick={() => setSelectedMethod(method.id)}
                                            style={{
                                                display: 'flex', alignItems: 'center', gap: '14px',
                                                padding: '14px 16px',
                                                background: selectedMethod === method.id
                                                    ? 'rgba(6,182,212,0.12)'
                                                    : 'rgba(255,255,255,0.03)',
                                                border: selectedMethod === method.id
                                                    ? '1.5px solid #06b6d4'
                                                    : '1.5px solid rgba(255,255,255,0.07)',
                                                borderRadius: '12px',
                                                cursor: 'pointer',
                                                transition: 'all 0.2s',
                                                textAlign: 'left',
                                                width: '100%',
                                            }}
                                        >
                                            <span style={{ fontSize: '24px', lineHeight: 1 }}>{method.icon}</span>
                                            <div style={{ flex: 1 }}>
                                                <p style={{ margin: 0, fontSize: '14px', fontWeight: 700, color: '#f1f5f9' }}>{method.label}</p>
                                                <p style={{ margin: '2px 0 0', fontSize: '12px', color: '#64748b' }}>{method.desc}</p>
                                            </div>
                                            <div style={{
                                                width: '18px', height: '18px',
                                                borderRadius: '50%',
                                                border: selectedMethod === method.id ? '5px solid #06b6d4' : '2px solid #334155',
                                                background: selectedMethod === method.id ? 'white' : 'transparent',
                                                flexShrink: 0,
                                                transition: 'all 0.2s',
                                            }} />
                                        </button>
                                    ))}
                                </div>
                            </div>

                            {/* Error */}
                            {paymentError && (
                                <p style={{ color: '#f87171', fontSize: '13px', margin: 0, padding: '10px 14px', background: 'rgba(239,68,68,0.1)', borderRadius: '10px', border: '1px solid rgba(239,68,68,0.2)' }}>
                                    ⚠️ {paymentError}
                                </p>
                            )}

                            {/* Confirm Button */}
                            <button
                                onClick={handleConfirmPayment}
                                disabled={loading || !selectedMethod}
                                style={{
                                    width: '100%', padding: '15px',
                                    background: loading || !selectedMethod
                                        ? 'rgba(100,116,139,0.3)'
                                        : 'linear-gradient(135deg, #06b6d4, #3b82f6)',
                                    border: 'none', borderRadius: '14px',
                                    color: 'white', fontWeight: 800, fontSize: '16px',
                                    cursor: loading || !selectedMethod ? 'not-allowed' : 'pointer',
                                    transition: 'all 0.2s',
                                    display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '10px',
                                }}
                            >
                                {loading ? (
                                    <>
                                        <FaSpinner style={{ animation: 'spin 1s linear infinite' }} />
                                        Processing...
                                    </>
                                ) : (
                                    '✓ Confirm Payment'
                                )}
                            </button>

                            <p style={{ margin: 0, textAlign: 'center', fontSize: '11px', color: '#475569' }}>
                                🔒 This is a simulated academic payment. No real charges apply.
                            </p>
                        </div>
                    )}
                </div>
            </div>

            <style>{`
                @keyframes fadeInOverlay {
                    from { opacity: 0; }
                    to { opacity: 1; }
                }
                @keyframes slideUpModal {
                    from { opacity: 0; transform: translateY(30px) scale(0.95); }
                    to { opacity: 1; transform: translateY(0) scale(1); }
                }
                @keyframes popIn {
                    0% { transform: scale(0); opacity: 0; }
                    70% { transform: scale(1.15); }
                    100% { transform: scale(1); opacity: 1; }
                }
                @keyframes spin {
                    from { transform: rotate(0deg); }
                    to { transform: rotate(360deg); }
                }
            `}</style>
        </div>
    );
};

export default PaymentModal;
