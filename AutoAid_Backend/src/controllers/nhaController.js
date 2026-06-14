const { runScraper } = require('../services/nhaScraper');

const getAdvisories = async (req, res) => {
    try {
        const data = await runScraper();
        res.status(200).json({ success: true, data });
    } catch (error) {
        console.error("NHA Scraper Error:", error);
        res.status(500).json({ success: false, error: 'Failed to fetch NHA advisories' });
    }
};

const checkRoute = async (req, res) => {
    try {
        const { startLocation, destination, travelDate } = req.body;
        
        if (!startLocation || !destination) {
            return res.status(400).json({ success: false, error: 'Start and destination are required' });
        }

        const data = await runScraper();
        
        const startLower = startLocation.toLowerCase();
        const destLower = destination.toLowerCase();
        
        // Filter alerts that might be relevant to the route and date
        const routeAlerts = data.filter(alert => {
            const desc = alert.fullText.toLowerCase();
            
            // 1. Check if location matches
            let locationMatch = false;
            if (desc.includes(startLower) || desc.includes(destLower)) {
                locationMatch = true;
            } else if ((startLower.includes('islamabad') && destLower.includes('lahore')) ||
                       (startLower.includes('lahore') && destLower.includes('islamabad'))) {
                if (['M-2 Motorway', 'N-5 National Highway', 'GT Road'].includes(alert.highway)) {
                    locationMatch = true;
                }
            } else if ((startLower.includes('karachi') && destLower.includes('hyderabad')) ||
                       (startLower.includes('hyderabad') && destLower.includes('karachi'))) {
                if (['M-9 Motorway'].includes(alert.highway)) {
                    locationMatch = true;
                }
            } else if ((startLower.includes('gwadar') && destLower.includes('makola')) ||
                       (startLower.includes('makola') && destLower.includes('gwadar'))) {
                if (alert.highway.toLowerCase().includes('coastal')) {
                    locationMatch = true;
                }
            } else if ((startLower.includes('sehwan') && destLower.includes('ratodero')) ||
                       (startLower.includes('ratodero') && destLower.includes('sehwan'))) {
                if (alert.highway.toLowerCase().includes('indus')) {
                    locationMatch = true;
                }
            }
            
            if (!locationMatch) return false;

            // 2. Filter by Date: only show alerts published on the exact travelDate (YYYY-MM-DD)
            if (travelDate && alert.date) {
                try {
                    // Extract the date part YYYY-MM-DD from "YYYY-MM-DD HH:MM:SS"
                    const alertDateString = alert.date.split(' ')[0];
                    if (alertDateString !== travelDate) {
                        return false;
                    }
                } catch (dateErr) {
                    console.warn("Date parsing error on checkRoute:", dateErr.message);
                }
            }

            return true; 
        });

        res.status(200).json({ 
            success: true, 
            routeAlerts,
            alternativeRoutes: [] 
        });
    } catch (error) {
        console.error("Route Check Error:", error);
        res.status(500).json({ success: false, error: 'Failed to check route' });
    }
};

module.exports = {
    getAdvisories,
    checkRoute
};
