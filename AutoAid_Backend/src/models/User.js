const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const UserSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true,
  },
  password: {
    type: String,
    required: true,
    select: false, // Don't return password by default in queries
  },
  fullName: {
    type: String,
    required: true,
  },
  role: {
    type: String,
    enum: ['user', 'provider', 'admin', 'superadmin'],
    default: 'user',
  },
  contactNumber: {
    type: String,
    required: true,
  },
  location: {
    type: String,
  },
  isVerified: {
    type: Boolean,
    default: false,
  },
  status: {
    type: String,
    enum: ['active', 'pending', 'suspended'],
    default: 'active'
  },
  isAvailable: {
    type: Boolean,
    default: false
  },
  currentLocation: {
    lat: Number,
    lng: Number
  },
  isAdminApproved: {
    type: Boolean,
    default: false
  },
  providerDetails: {
    serviceType: String,
    age: Number,
    dob: Date,
    gender: String,
    profileImage: String,
    cnicImage: String,
    licenseImage: String,
    chargesPerHour: {
        type: Number,
        min: 200,
        max: 1000
    },
    petrolPrice: {
        type: Number,
    },
    dieselPrice: {
        type: Number,
    },
    vehicleDetails: {
        number: String,
        make: String,
        model: String
    },
    averageRating: {
        type: Number,
        default: 0
    },
    totalRatings: {
        type: Number,
        default: 0
    },
    completedJobsCount: {
        type: Number,
        default: 0
    }
  },
  createdAt: {
    type: Date,
    default: Date.now,
  },
});

// Hash password before saving
UserSchema.pre('save', async function (next) {
  if (!this.isModified('password')) return next();
  const salt = await bcrypt.genSalt(10);
  this.password = await bcrypt.hash(this.password, salt);
  next();
});

// Compare entered password with hashed password
UserSchema.methods.matchPassword = async function (enteredPassword) {
  return await bcrypt.compare(enteredPassword, this.password);
};

module.exports = mongoose.model('User', UserSchema);
