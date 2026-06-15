const admin = require('firebase-admin');
const dotenv = require('dotenv');

dotenv.config();

// Check if serviceAccountKey is available or use environment variables
// For now, we will use a placeholder or check for a specific env var
// You should replace 'path/to/serviceAccountKey.json' with your actual file path
// or use environment variables to initialize the app.

try {
  // Option 1: Initializing using individual service account env vars
  if (process.env.FIREBASE_PROJECT_ID && process.env.FIREBASE_CLIENT_EMAIL && process.env.FIREBASE_PRIVATE_KEY) {
      admin.initializeApp({
          credential: admin.credential.cert({
              projectId: process.env.FIREBASE_PROJECT_ID,
              clientEmail: process.env.FIREBASE_CLIENT_EMAIL,
              // Replace escaped newlines with actual newlines in private key
              privateKey: process.env.FIREBASE_PRIVATE_KEY.replace(/\\n/g, '\n')
          })
      });
      console.log('Firebase Admin Initialized via env cert credentials');
  } 
  // Option 2: Fallback to applicationDefault (e.g. locally with GOOGLE_APPLICATION_CREDENTIALS)
  else if (process.env.FIREBASE_PROJECT_ID) {
      admin.initializeApp({
          credential: admin.credential.applicationDefault(),
          projectId: process.env.FIREBASE_PROJECT_ID
      });
      console.log('Firebase Admin Initialized via applicationDefault');
  } else {
      console.warn('Firebase credentials not found. Firebase features will not work.');
  }

} catch (error) {
  console.error('Firebase Admin Initialization Error:', error);
}

module.exports = admin;
