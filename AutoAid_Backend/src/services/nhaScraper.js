const { exec } = require('child_process');
const path = require('path');
const fs = require('fs');

let activeScrapePromise = null;

const runScraper = () => {
    const scriptPath = path.resolve(__dirname, '../../scraper/nha_scraper.py');
    const cachePath = path.resolve(__dirname, '../../scraper/nha_cache.json');
    const CACHE_DURATION_MS = 60 * 60 * 1000; // 1 hour
    const now = Date.now();

    // 1. If there's an active scraper process in progress, return that promise
    if (activeScrapePromise) {
        console.log("Scraping already in progress. Reusing active scraper promise...");
        return activeScrapePromise;
    }

    // 2. Check if a valid, unexpired cache exists in JSON file
    if (fs.existsSync(cachePath)) {
        try {
            const cacheContent = fs.readFileSync(cachePath, 'utf8');
            const cacheData = JSON.parse(cacheContent);
            
            if (cacheData && cacheData.lastScrapedTime && (now - cacheData.lastScrapedTime < CACHE_DURATION_MS)) {
                console.log("Using cached NHA advisories (cached less than 1 hour ago)...");
                return Promise.resolve(cacheData.data);
            }
        } catch (err) {
            console.warn("Failed to read or parse cache file, proceeding to scrape:", err.message);
        }
    }

    // 3. Cache is expired or missing. Run the scraper and cache the output
    console.log("Cache expired or missing. Launching NHA scraper...");
    activeScrapePromise = new Promise((resolve, reject) => {
        exec(`python "${scriptPath}"`, (error, stdout, stderr) => {
            // Clear the active scrape promise when finished
            activeScrapePromise = null;

            if (error) {
                console.error(`Scraper execution error: ${error.message}`);
                return reject(error);
            }
            if (stderr) {
                console.warn(`Scraper stderr: ${stderr}`);
            }
            
            try {
                const lines = stdout.trim().split('\n');
                let parsedData = null;
                
                for (let i = lines.length - 1; i >= 0; i--) {
                    if (lines[i].trim().startsWith('{')) {
                        parsedData = JSON.parse(lines[i].trim());
                        break;
                    }
                }

                if (!parsedData) {
                     return reject(new Error('Could not find JSON output from scraper'));
                }

                if (!parsedData.success) {
                    return reject(new Error(parsedData.error || 'Scraper reported failure'));
                }

                // Process and enrich data
                const enrichedData = parsedData.data.map(item => {
                    const cardLines = item.fullText.split('\n').map(l => l.trim()).filter(Boolean);
                    
                    let highway = 'Unknown';
                    let alertDate = '';
                    let alertType = 'General Alert';
                    let condition = item.description;
                    let location = 'Unknown';
                    let direction = '';

                    // Parse the clean structured layout from the NHA card
                    if (cardLines.length >= 8) {
                        highway = cardLines[0];
                        alertDate = cardLines[1];
                        alertType = cardLines[2];
                        condition = cardLines[3];
                        location = cardLines[5];
                        direction = cardLines[7];
                    } else {
                        // Fallback parsing if structure is different
                        const textLower = item.fullText.toLowerCase();
                        if (textLower.includes('m-2') || textLower.includes('m2')) highway = 'M-2 Motorway';
                        else if (textLower.includes('m-1') || textLower.includes('m1')) highway = 'M-1 Motorway';
                        else if (textLower.includes('m-9') || textLower.includes('m9')) highway = 'M-9 Motorway';
                        else if (textLower.includes('n-5') || textLower.includes('n5')) highway = 'N-5 National Highway';
                        else if (textLower.includes('gt road')) highway = 'GT Road';
                        else if (textLower.includes('m-3') || textLower.includes('m3')) highway = 'M-3 Motorway';
                        else if (textLower.includes('m-4') || textLower.includes('m4')) highway = 'M-4 Motorway';

                        if (textLower.includes('rain') || textLower.includes('weather') || textLower.includes('fog')) alertType = 'Weather Alert';
                        else if (textLower.includes('clos') || textLower.includes('block')) alertType = 'Road Closure';
                        else if (textLower.includes('accident') || textLower.includes('crash')) alertType = 'Accident';
                        else if (textLower.includes('construct') || textLower.includes('repair')) alertType = 'Construction';
                    }

                    const descLower = condition.toLowerCase();
                    const recommendAlternative = 
                        alertType.toLowerCase().includes('closed') || 
                        alertType.toLowerCase().includes('closure') || 
                        alertType.toLowerCase().includes('alternate') || 
                        descLower.includes('closed') || 
                        descLower.includes('closure') || 
                        descLower.includes('block') || 
                        descLower.includes('protest');

                    // Mock coordinate mapping based on highway (Ideally use Geocoding API)
                    let lat = 33.6844, lng = 73.0479; // Default Islamabad
                    const hwy = highway.toLowerCase();
                    if (hwy.includes('m-2') || hwy.includes('m2')) { lat = 32.5; lng = 73.5; }
                    else if (hwy.includes('m-1') || hwy.includes('m1')) { lat = 33.8; lng = 72.5; }
                    else if (hwy.includes('m-9') || hwy.includes('m9')) { lat = 25.0; lng = 68.0; }
                    else if (hwy.includes('n-5') || hwy.includes('n5') || hwy.includes('gt road')) { lat = 32.0; lng = 74.0; }
                    else if (hwy.includes('coastal')) { lat = 25.35; lng = 63.48; } // Gwadar/Makola region
                    else if (hwy.includes('indus')) { lat = 27.5; lng = 68.0; } // Indus highway (Sehwan/Ratodero)

                    // Add random offset for distinct markers
                    lat += (Math.random() - 0.5) * 0.3;
                    lng += (Math.random() - 0.5) * 0.3;

                    return {
                        id: item.id,
                        highway,
                        date: alertDate,
                        alertType,
                        condition,
                        location,
                        direction,
                        recommendAlternative,
                        description: `${alertType} - ${condition}`,
                        fullText: item.fullText,
                        timestamp: new Date().toISOString(),
                        coordinates: { lat, lng }
                    };
                });

                // Write the newly scraped data to the cache file
                const newCache = {
                    lastScrapedTime: Date.now(),
                    data: enrichedData
                };
                fs.writeFileSync(cachePath, JSON.stringify(newCache, null, 2), 'utf8');

                resolve(enrichedData);
            } catch (parseError) {
                console.error('Failed to parse scraper output:', stdout);
                reject(new Error(`Failed to parse scraper output: ${parseError.message}`));
            }
        });
    });

    return activeScrapePromise;
};

module.exports = {
    runScraper
};
