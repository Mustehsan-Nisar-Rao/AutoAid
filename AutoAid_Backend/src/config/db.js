const mongoose = require('mongoose');
const dotenv = require('dotenv');

dotenv.config();

const connectDB = async () => {
  try {
    const conn = await mongoose.connect(process.env.MONGO_URI || 'mongodb+srv://autoaidDb:8765@1234@autoaid-database-cluste.7c93xlw.mongodb.net/');

    console.log(`MongoDB Connected: ${conn.connection.host}`);

    // Drop legacy Firebase uid index if it still exists in the collection
    try {
      await mongoose.connection.db.collection('users').dropIndex('uid_1');
      console.log('Legacy MongoDB index "uid_1" dropped successfully.');
    } catch (indexErr) {
      // Index might already be dropped or does not exist
    }
  } catch (error) {
    console.error(`Error: ${error.message}`);
    process.exit(1);
  }
};

module.exports = connectDB;
