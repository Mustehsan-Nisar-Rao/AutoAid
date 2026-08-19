import React, { createContext, useContext, useEffect, useState } from 'react';
import { API_BASE_URL } from '../utils/api';

const AuthContext = createContext();

export const useAuth = () => {
    return useContext(AuthContext);
};

export const AuthProvider = ({ children }) => {
    const [currentUser, setCurrentUser] = useState(null);
    const [loading, setLoading] = useState(true);

    const fetchUserProfile = async () => {
        try {
            const response = await fetch(`${API_BASE_URL}/api/auth/check`, {
                method: 'GET',
                credentials: 'include',
            });
            if (response.ok) {
                const data = await response.json();
                if (data.success) {
                    setCurrentUser(data.user);
                } else {
                    setCurrentUser(null);
                }
            } else {
                setCurrentUser(null);
            }
        } catch (error) {
            console.error("Failed to fetch user profile", error);
            setCurrentUser(null);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchUserProfile();
    }, []);

    const logout = async () => {
        try {
            await fetch(`${API_BASE_URL}/api/auth/logout`, {
                method: 'POST',
                credentials: 'include',
            });
            setCurrentUser(null);
        } catch (error) {
            console.error('Logout error:', error);
        }
    };

    const value = {
        currentUser,
        setCurrentUser,
        logout,
        fetchUserProfile
    };

    return (
        <AuthContext.Provider value={value}>
            {loading ? (
                <div className="flex items-center justify-center min-h-screen bg-slate-900 text-white font-sans">
                    <div className="flex flex-col items-center space-y-4">
                        <div className="w-12 h-12 border-4 border-blue-500 border-t-transparent rounded-full animate-spin"></div>
                        <p className="text-sm font-semibold tracking-wider text-slate-300">Loading AutoAid...</p>
                    </div>
                </div>
            ) : children}
        </AuthContext.Provider>
    );
};
