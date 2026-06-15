import React, { createContext, useContext, useEffect, useState } from 'react';
import { auth } from '../firebase';
import { onAuthStateChanged, signOut } from 'firebase/auth';
import { API_BASE_URL } from '../utils/api';

const AuthContext = createContext();

export const useAuth = () => {
    return useContext(AuthContext);
};

export const AuthProvider = ({ children }) => {
    const [currentUser, setCurrentUser] = useState(null);
    const [loading, setLoading] = useState(true);

    const fetchUserProfile = async (user) => {
        if (user) {
            try {
                const response = await fetch(`${API_BASE_URL}/api/auth/check`, {
                    method: 'GET',
                    credentials: 'include',
                });
                const data = await response.json();
                if (data.success) {
                    setCurrentUser({ ...user, ...data.user });
                } else {
                    setCurrentUser(user);
                }
            } catch (error) {
                console.error("Failed to fetch user profile", error);
                setCurrentUser(user);
            }
        } else {
            setCurrentUser(null);
        }
    };

    useEffect(() => {
        const unsubscribe = onAuthStateChanged(auth, async (user) => {
            await fetchUserProfile(user);
            setLoading(false);
        });

        return unsubscribe;
    }, []);

    const logout = () => {
        return signOut(auth);
    };

    const value = {
        currentUser,
        logout,
        fetchUserProfile
    };

    return (
        <AuthContext.Provider value={value}>
            {!loading && children}
        </AuthContext.Provider>
    );
};
