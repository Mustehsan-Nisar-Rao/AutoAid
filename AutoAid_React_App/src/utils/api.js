// Central API base URL configuration
// In development: defaults to localhost
// In production: uses VITE_API_URL or live Render backend URL
export const API_BASE_URL =
  import.meta.env.VITE_API_URL ||
  (import.meta.env.PROD ? 'https://autoaid-backend-kppu.onrender.com' : 'http://localhost:3000');
