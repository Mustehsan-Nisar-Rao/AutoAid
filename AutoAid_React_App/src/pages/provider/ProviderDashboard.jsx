import React, { useState, useEffect } from 'react';
import { useAuth } from '../../context/AuthContext';
import { useNotification } from '../../context/NotificationContext';
import { FaWallet, FaCheckCircle, FaStar, FaToggleOn, FaToggleOff } from 'react-icons/fa';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { API_BASE_URL } from '../../utils/api';

const ProviderDashboard = () => {
    const { currentUser, fetchUserProfile } = useAuth();
    const { error, info } = useNotification();
    const [isAvailable, setIsAvailable] = useState(false);
    const [isLoading, setIsLoading] = useState(false);

    const [statsData, setStatsData] = useState({ totalEarnings: 0, earningsData: [] });

    useEffect(() => {
        if (currentUser) {
            setIsAvailable(currentUser.isAvailable || false);
            fetchProviderStats();
        }
    }, [currentUser]);

    const fetchProviderStats = async () => {
        try {
            const response = await fetch(`${API_BASE_URL}/api/payments/provider/stats`, {
                credentials: 'include'
            });
            const data = await response.json();
            if (data.success) {
                setStatsData(data.stats);
            }
        } catch (error) {
            console.error('Error fetching provider stats:', error);
        }
    };

    const updateStatus = async (status, location = null) => {
        setIsLoading(true);
        try {
            const body = { isAvailable: status };
            if (location) {
                body.location = location;
            }

            const response = await fetch(`${API_BASE_URL}/api/auth/status`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(body),
                credentials: 'include'
            });

            const data = await response.json();
            if (data.success) {
                setIsAvailable(data.user.isAvailable);
                // Update context so the new status persists across page navigation
                if (currentUser) {
                    fetchUserProfile(currentUser); 
                }
            } else {
                error('Failed to update status: ' + data.error);
                // Revert state if failed
                setIsAvailable(!status); 
            }
        } catch (err) {
            console.error('Error updating status:', err);
            error('An error occurred while updating status');
            setIsAvailable(!status);
        } finally {
            setIsLoading(false);
        }
    };

    const handleToggle = () => {
        const newStatus = !isAvailable;
        
        if (newStatus) {
            // Turning ON -> Get Location
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    (position) => {
                        const { latitude, longitude } = position.coords;
                        updateStatus(true, { lat: latitude, lng: longitude });
                    },
                    (err) => {
                        console.error("Error getting location:", err);
                        info("We need your location to set you Online. Please enable location access.");
                    }
                );
            } else {
                error("Geolocation is not supported by this browser.");
            }
        } else {
            // Turning OFF
            updateStatus(false);
        }
    };

  const stats = [
    { 
        label: 'Total Earnings', 
        value: `PKR ${statsData.totalEarnings.toLocaleString()}`, 
        icon: <FaWallet />, 
        color: 'text-green-400', 
        bg: 'bg-green-400/10' 
    },
    { 
        label: 'Jobs Completed', 
        value: currentUser?.providerDetails?.completedJobsCount || '0', 
        icon: <FaCheckCircle />, 
        color: 'text-blue-400', 
        bg: 'bg-blue-400/10' 
    },
    { 
        label: 'Average Rating', 
        value: currentUser?.providerDetails?.averageRating?.toFixed(1) || '0.0', 
        icon: <FaStar />, 
        color: 'text-yellow-400', 
        bg: 'bg-yellow-400/10' 
    },
  ];


  return (
    <div className="space-y-6 animate-fade-in">
      {/* Header Section */}
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-3xl font-bold text-gray-900 dark:text-white">Dashboard</h1>
          <p className="text-gray-600 dark:text-gray-400">Welcome back, {currentUser?.fullName || 'Provider'}</p>
        </div>
        
        <div className="flex items-center gap-4 bg-white dark:bg-surface-dark p-3 rounded-xl border border-gray-200 dark:border-gray-700 shadow-sm transition-colors duration-300">
          <span className={`text-sm font-medium ${isAvailable ? 'text-green-500' : 'text-gray-500'}`}>
            {isLoading ? 'Updating...' : (isAvailable ? 'You are Online' : 'You are Offline')}
          </span>
          <button 
            onClick={handleToggle}
            disabled={isLoading}
            className={`text-3xl transition-colors duration-300 ${isAvailable ? 'text-green-500' : 'text-gray-400 dark:text-gray-500'} ${isLoading ? 'opacity-50 cursor-not-allowed' : ''}`}
          >
            {isAvailable ? <FaToggleOn /> : <FaToggleOff />}
          </button>
        </div>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {stats.map((stat, index) => (
          <div key={index} className="bg-white dark:bg-surface-dark p-6 rounded-xl border border-gray-200 dark:border-gray-700 shadow-lg hover:border-primary/50 transition-colors duration-300">
            <div className="flex justify-between items-start">
              <div>
                <p className="text-gray-600 dark:text-gray-400 text-sm mb-1">{stat.label}</p>
                <h3 className="text-2xl font-bold text-gray-900 dark:text-white">{stat.value}</h3>
              </div>
              <div className={`p-3 rounded-lg ${stat.bg} ${stat.color} text-xl`}>
                {stat.icon}
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Earnings Chart */}
      <div className="bg-white dark:bg-surface-dark rounded-xl border border-gray-200 dark:border-gray-700 overflow-hidden shadow-lg transition-colors duration-300">
        <div className="p-6 border-b border-gray-200 dark:border-gray-700">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">Monthly Earnings</h2>
        </div>
        <div className="p-6 h-80 w-full">
            {statsData.earningsData.length === 0 ? (
                <div className="h-full flex items-center justify-center text-gray-500">No earnings data available yet.</div>
            ) : (
                <ResponsiveContainer width="100%" height="100%">
                    <BarChart data={statsData.earningsData}>
                        <CartesianGrid strokeDasharray="3 3" stroke="#333" vertical={false} />
                        <XAxis 
                            dataKey="month" 
                            stroke="#888" 
                            fontSize={12} 
                            tickLine={false} 
                            axisLine={false}
                        />
                        <YAxis 
                            stroke="#888" 
                            fontSize={12} 
                            tickLine={false} 
                            axisLine={false}
                            tickFormatter={(value) => `PKR ${value}`}
                        />
                        <Tooltip 
                            cursor={{ fill: 'rgba(255, 255, 255, 0.05)' }}
                            contentStyle={{ backgroundColor: '#1a1c1e', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', fontSize: '12px' }}
                            itemStyle={{ color: '#10b981' }}
                            formatter={(value) => [`PKR ${value.toLocaleString()}`, 'Amount']}
                        />
                        <Bar 
                            dataKey="amount" 
                            fill="#10b981" 
                            radius={[4, 4, 0, 0]} 
                            barSize={40}
                        />
                    </BarChart>
                </ResponsiveContainer>
            )}
        </div>
      </div>
    </div>
  );
};

export default ProviderDashboard;
