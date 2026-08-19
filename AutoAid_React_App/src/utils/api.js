// Central API base URL configuration
// In development: uses localhost
// In production: uses the VITE_API_URL env variable set on Vercel

export const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:3000';
