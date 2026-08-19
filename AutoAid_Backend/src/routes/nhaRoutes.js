const express = require('express');
const router = express.Router();
const { getAdvisories, checkRoute } = require('../controllers/nhaController');

router.get('/advisories', getAdvisories);
router.post('/route-check', checkRoute);

module.exports = router;
