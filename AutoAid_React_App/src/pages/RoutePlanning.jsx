import React, { useState, useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { 
    FaSearch, FaExclamationTriangle, FaRoad, FaSyncAlt, 
    FaDirections, FaCalendarAlt, FaCheckCircle, FaMapMarkerAlt
} from 'react-icons/fa';
import { useAuth } from '../context/AuthContext';
import { useNotification } from '../context/NotificationContext';

// React-Leaflet imports
import { MapContainer, TileLayer, Marker, Popup, Polyline, useMap } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

// Fix default Leaflet marker icons broken by Webpack/Vite
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
    iconRetinaUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png',
    iconUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png',
    shadowUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png',
});

// Custom Alert Marker Icons
const createAlertIcon = (color) => new L.DivIcon({
    html: `<div style="
        background: ${color};
        border: 2px solid white;
        border-radius: 50%;
        width: 20px; height: 20px;
        display: flex; align-items: center; justify-content: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.4);
    "></div>`,
    className: '',
    iconSize: [20, 20],
    iconAnchor: [10, 10],
    popupAnchor: [0, -10]
});

const severeAlertIcon = createAlertIcon('#EF4444');
const warningAlertIcon = createAlertIcon('#F59E0B');

const startIcon = new L.DivIcon({
    html: `<div style="background: #22c55e; border: 2px solid white; border-radius: 50%; width: 16px; height: 16px; box-shadow: 0 2px 8px rgba(34,197,94,0.6);"></div>`,
    className: '',
    iconSize: [16, 16],
    iconAnchor: [8, 8],
    popupAnchor: [0, -8]
});

const endIcon = new L.DivIcon({
    html: `<div style="background: #00BCD4; border: 2px solid white; border-radius: 50%; width: 16px; height: 16px; box-shadow: 0 2px 8px rgba(0,188,212,0.6);"></div>`,
    className: '',
    iconSize: [16, 16],
    iconAnchor: [8, 8],
    popupAnchor: [0, -8]
});

// Map bounds controller
const FitBounds = ({ routeCoords, startCoords, endCoords, markers }) => {
    const map = useMap();

    useEffect(() => {
        const bounds = L.latLngBounds([]);
        
        if (routeCoords && routeCoords.length > 0) {
            routeCoords.forEach(coord => bounds.extend(coord));
        }
        if (startCoords) bounds.extend([startCoords.lat, startCoords.lng]);
        if (endCoords) bounds.extend([endCoords.lat, endCoords.lng]);
        if (markers && markers.length > 0) {
            markers.forEach(m => {
                if (m.coordinates && m.coordinates.lat) bounds.extend([m.coordinates.lat, m.coordinates.lng]);
            });
        }

        if (bounds.isValid()) {
            map.fitBounds(bounds, { padding: [50, 50], animate: true });
        }
    }, [routeCoords, startCoords, endCoords, markers, map]);

    return null;
};

// Formatting helpers
const formatDistance = (meters) => `${(meters / 1000).toFixed(1)} km`;
const formatDuration = (seconds) => {
    const h = Math.floor(seconds / 3600);
    const m = Math.floor((seconds % 3600) / 60);
    if (h > 0) return `${h}h ${m}m`;
    return `${m}m`;
};

const RoutePlanning = () => {
    const navigate = useNavigate();
    const { currentUser } = useAuth();
    const { error, info, warn } = useNotification();
    
    const [formData, setFormData] = useState({
        startLocation: '',
        endLocation: '',
        travelDate: ''
    });

    const [isSearching, setIsSearching] = useState(false);
    const [showResults, setShowResults] = useState(false);
    const [advisories, setAdvisories] = useState([]);
    const [advisoryError, setAdvisoryError] = useState('');
    const [isRefreshing, setIsRefreshing] = useState(false);
    
    const [alternativeRoutes, setAlternativeRoutes] = useState([]);
    const [mapCenter, setMapCenter] = useState([33.6844, 73.0479]); // Default Islamabad
    const [routeGeometry, setRouteGeometry] = useState([]);
    const [startCoords, setStartCoords] = useState(null);
    const [endCoords, setEndCoords] = useState(null);

    const alertColors = [
        { color: 'border-red-500', iconColor: 'text-red-500' },
        { color: 'border-yellow-500', iconColor: 'text-yellow-500' },
        { color: 'border-blue-500', iconColor: 'text-blue-500' },
        { color: 'border-orange-500', iconColor: 'text-orange-500' },
        { color: 'border-purple-500', iconColor: 'text-purple-500' },
        { color: 'border-teal-500', iconColor: 'text-teal-500' },
    ];

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const geocode = async (query) => {
        const searchQuery = query.toLowerCase().includes('pakistan') ? query : `${query}, Pakistan`;
        const res = await fetch(`https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(searchQuery)}&format=json&limit=1`, {
            headers: { 'Accept-Language': 'en' }
        });
        const data = await res.json();
        if (data && data.length > 0) {
            return { lat: parseFloat(data[0].lat), lng: parseFloat(data[0].lon) };
        }
        throw new Error(`Location not found: ${query}`);
    };

    const fetchOSRMRoute = async (start, end, fetchAlternatives) => {
        const url = `https://router.project-osrm.org/route/v1/driving/${start.lng},${start.lat};${end.lng},${end.lat}?overview=full&geometries=geojson&alternatives=${fetchAlternatives}`;
        const res = await fetch(url);
        const data = await res.json();

        if (data.code !== 'Ok') {
            throw new Error('Could not calculate exact route directions on the map.');
        }

        return data.routes;
    };

    const fetchRouteAdvisories = async () => {
        try {
            // 1. Geocode locations first
            const startC = await geocode(formData.startLocation);
            const endC = await geocode(formData.endLocation);
            
            setStartCoords(startC);
            setEndCoords(endC);

            // 2. Fetch NHA Alerts from Backend
            const response = await fetch('http://localhost:3000/api/nha/route-check', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    startLocation: formData.startLocation,
                    destination: formData.endLocation,
                    travelDate: formData.travelDate
                }),
                credentials: 'include'
            });
            const data = await response.json();

            let fetchedAdvisories = [];
            let hasSevereAlerts = false;

            if (data.success) {
                fetchedAdvisories = data.routeAlerts || [];
                setAdvisories(fetchedAdvisories);
                setAdvisoryError('');
                hasSevereAlerts = fetchedAdvisories.some(a => a.recommendAlternative || a.alertType === 'Road Closure' || a.alertType === 'Accident' || a.alertType === 'Construction');
            } else {
                setAdvisoryError(data.error || 'Failed to fetch route advisories');
                setAdvisories([]);
            }

            // 3. Fetch OSRM Route
            try {
                const routes = await fetchOSRMRoute(startC, endC, hasSevereAlerts);
                
                if (routes.length > 0) {
                    // Main Route
                    const mainRoutePositions = routes[0].geometry.coordinates.map(c => [c[1], c[0]]);
                    setRouteGeometry(mainRoutePositions);
                    
                    // Alternative Routes
                    if (hasSevereAlerts && routes.length > 1) {
                        const alts = routes.slice(1).map((r, idx) => ({
                            id: idx,
                            name: `Alternative Route ${idx + 1}`,
                            description: 'Suggested due to alerts on primary route.',
                            distance: formatDistance(r.distance),
                            time: formatDuration(r.duration),
                            status: 'Recommended',
                            geometry: r.geometry.coordinates.map(c => [c[1], c[0]])
                        }));
                        setAlternativeRoutes(alts);
                    } else {
                        setAlternativeRoutes([]);
                    }
                }
            } catch (routeErr) {
                warn(routeErr.message);
                setRouteGeometry([]);
                setAlternativeRoutes([]);
            }
            
        } catch (error) {
            console.error('Error fetching data:', error);
            error.message.includes('Location not found') 
                ? warn(error.message)
                : setAdvisoryError('Failed to connect to advisory service. Please try again.');
            setAdvisories([]);
            setRouteGeometry([]);
            setStartCoords(null);
            setEndCoords(null);
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        if (!currentUser) {
            info('Please login to use route planning features.');
            return;
        }

        setIsSearching(true);
        setAdvisoryError('');

        await fetchRouteAdvisories();

        setIsSearching(false);
        setShowResults(true);
    };

    const handleRefresh = async () => {
        setIsRefreshing(true);
        await fetchRouteAdvisories();
        setIsRefreshing(false);
    };

    const viewAlternativeRoute = (route) => {
        setRouteGeometry(route.geometry);
        info("Showing alternative route on map");
    };

    const hasMatchedAdvisories = advisories.length > 0;

    return (
        <div className="min-h-screen bg-background-light dark:bg-background-dark pt-24 pb-12 px-4 sm:px-6 lg:px-8 relative overflow-hidden transition-colors duration-300">
            {/* Background Elements */}
            <div className="absolute top-0 left-0 w-full h-full overflow-hidden z-0 pointer-events-none">
                <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-primary/10 rounded-full blur-[120px] animate-pulse"></div>
            </div>

            <div className="max-w-7xl mx-auto relative z-10">
                <div className="mb-8">
                    <h1 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-2">
                        NHA Route Announcements
                    </h1>
                    <p className="text-text-muted">
                        Get real-time updates on roadblocks, construction, and other alerts for your planned route.
                    </p>
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
                    {/* Left Sidebar */}
                    <div className="lg:col-span-4 space-y-6">
                        {/* Plan Your Route Card */}
                        <div className="glassmorphism rounded-2xl p-6 border border-border-dark">
                            <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-6">Plan Your Route</h2>
                            <form onSubmit={handleSubmit} className="space-y-4">
                                <div className="space-y-2">
                                    <label htmlFor="startLocation" className="block text-sm font-medium text-text-muted">
                                        Starting Point
                                    </label>
                                    <div className="relative">
                                        <input
                                            type="text"
                                            id="startLocation"
                                            name="startLocation"
                                            required
                                            placeholder="e.g., Islamabad"
                                            value={formData.startLocation}
                                            onChange={handleChange}
                                            className="block w-full px-4 py-3 bg-surface-light dark:bg-surface-dark border border-gray-200 dark:border-border-dark rounded-xl text-gray-900 dark:text-white placeholder-gray-500 dark:placeholder-text-muted focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition-all"
                                        />
                                    </div>
                                </div>

                                <div className="space-y-2">
                                    <label htmlFor="endLocation" className="block text-sm font-medium text-text-muted">
                                        Destination
                                    </label>
                                    <div className="relative">
                                        <input
                                            type="text"
                                            id="endLocation"
                                            name="endLocation"
                                            required
                                            placeholder="e.g., Lahore"
                                            value={formData.endLocation}
                                            onChange={handleChange}
                                            className="block w-full px-4 py-3 bg-surface-light dark:bg-surface-dark border border-gray-200 dark:border-border-dark rounded-xl text-gray-900 dark:text-white placeholder-gray-500 dark:placeholder-text-muted focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition-all"
                                        />
                                    </div>
                                </div>

                                <div className="space-y-2">
                                    <label htmlFor="travelDate" className="block text-sm font-medium text-text-muted">
                                        Travel Date
                                    </label>
                                    <div className="relative">
                                        <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                                            <FaCalendarAlt className="text-text-muted" />
                                        </div>
                                        <input
                                            type="date"
                                            id="travelDate"
                                            name="travelDate"
                                            required
                                            value={formData.travelDate}
                                            onChange={handleChange}
                                            className="block w-full pl-10 pr-4 py-3 bg-surface-light dark:bg-surface-dark border border-gray-200 dark:border-border-dark rounded-xl text-gray-900 dark:text-white placeholder-gray-500 dark:placeholder-text-muted focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition-all"
                                        />
                                    </div>
                                </div>

                                <button
                                    type="submit"
                                    disabled={isSearching}
                                    className="w-full flex flex-col items-center justify-center gap-1 py-3 px-6 rounded-xl bg-primary hover:bg-primary/90 text-white font-bold transition-all duration-300 mt-4"
                                >
                                    <div className="flex items-center gap-2">
                                        {isSearching ? (
                                            <FaSyncAlt className="animate-spin" />
                                        ) : (
                                            <FaSearch />
                                        )}
                                        {isSearching ? 'Processing Route...' : 'Find Announcements'}
                                    </div>
                                    {isSearching && (
                                        <span className="text-[10px] text-white/80 font-normal">
                                            (Note: Fresh scrape may take more than a minute)
                                        </span>
                                    )}
                                </button>
                            </form>
                        </div>

                        {/* Route Safety Status */}
                        {showResults && !isSearching && (
                            <div className={`glassmorphism rounded-2xl p-6 border ${hasMatchedAdvisories ? 'border-red-500/50 bg-red-500/5' : 'border-green-500/50 bg-green-500/5'}`}>
                                <div className="flex items-center gap-4">
                                    {hasMatchedAdvisories ? (
                                        <FaExclamationTriangle className="text-3xl text-red-500" />
                                    ) : (
                                        <FaCheckCircle className="text-3xl text-green-500" />
                                    )}
                                    <div>
                                        <h2 className={`text-xl font-bold ${hasMatchedAdvisories ? 'text-red-500' : 'text-green-500'}`}>
                                            {hasMatchedAdvisories ? 'Route Affected' : 'Route Clear'}
                                        </h2>
                                        <p className="text-sm text-text-muted mt-1">
                                            {hasMatchedAdvisories ? 'There are active travel advisories for your route.' : 'No active NHA alerts found for your journey.'}
                                        </p>
                                    </div>
                                </div>
                            </div>
                        )}

                        {/* Real-Time NHA Alerts Card */}
                        <div className="glassmorphism rounded-2xl p-6 border border-border-dark min-h-[400px]">
                            <div className="flex items-center justify-between mb-6">
                                <h2 className="text-xl font-bold text-gray-900 dark:text-white">Route Alerts</h2>
                                {showResults && (
                                    <button
                                        onClick={handleRefresh}
                                        disabled={isRefreshing}
                                        className="text-text-muted hover:text-primary transition-colors"
                                        title="Refresh advisories"
                                    >
                                        <FaSyncAlt className={`text-sm ${isRefreshing ? 'animate-spin' : ''}`} />
                                        <span className="sr-only">Refresh</span>
                                    </button>
                                )}
                            </div>

                            <div className="space-y-4">
                                {isSearching ? (
                                    <div className="text-center py-10">
                                        <FaSyncAlt className="text-3xl mx-auto mb-3 text-primary animate-spin" />
                                        <p className="text-text-muted">Fetching latest NHA advisories...</p>
                                        <p className="text-text-muted/60 text-xs mt-2 italic px-4">
                                            Note: If a fresh scrape is needed, it may take more than a minute to complete.
                                        </p>
                                    </div>
                                ) : showResults ? (
                                    <>
                                        {advisoryError && (
                                            <div className="bg-red-500/10 border border-red-500/30 rounded-xl p-4 text-red-400 text-sm">
                                                <p className="font-medium">⚠️ {advisoryError}</p>
                                            </div>
                                        )}
                                        {advisories.length > 0 ? (
                                            advisories.map((advisory, index) => {
                                                const colorSet = alertColors[index % alertColors.length];
                                                return (
                                                    <div
                                                        key={advisory.id}
                                                        className={`bg-white/50 dark:bg-[#121A2A]/50 rounded-xl p-4 border-l-4 ${colorSet.color} hover:bg-white dark:hover:bg-[#121A2A] shadow-sm transition-all cursor-pointer`}
                                                    >
                                                        <div className="flex items-start gap-3 w-full">
                                                            <FaExclamationTriangle className={`${colorSet.iconColor} mt-1 flex-shrink-0`} />
                                                            <div className="w-full">
                                                                <div className="flex justify-between items-start">
                                                                    <h3 className="text-gray-900 dark:text-white font-bold text-sm">
                                                                        {advisory.alertType || 'Alert'}
                                                                    </h3>
                                                                    {advisory.date && (
                                                                        <span className="text-[10px] text-text-muted">{advisory.date}</span>
                                                                    )}
                                                                </div>
                                                                <p className="text-primary text-xs font-bold mt-0.5">
                                                                    {advisory.highway || advisory.title}
                                                                </p>
                                                                <p className="text-text-muted text-xs leading-relaxed mt-1">
                                                                    <strong>Condition:</strong> {advisory.condition || advisory.description}
                                                                </p>
                                                                {advisory.location && advisory.location !== 'Unknown' && (
                                                                    <p className="text-text-muted text-[11px] mt-0.5">
                                                                        <strong>Location:</strong> {advisory.location}
                                                                    </p>
                                                                )}
                                                                {advisory.direction && (
                                                                    <p className="text-text-muted text-[11px] mt-0.5">
                                                                        <strong>Direction:</strong> {advisory.direction}
                                                                    </p>
                                                                )}
                                                                {advisory.recommendAlternative && (
                                                                    <div className="mt-2 text-[10px] font-bold text-red-500 bg-red-500/10 py-1 px-2.5 rounded-md inline-block">
                                                                        ⚠️ Recommendation: Take Alternative Route
                                                                    </div>
                                                                )}
                                                            </div>
                                                        </div>
                                                    </div>
                                                );
                                            })
                                        ) : (
                                            !advisoryError && (
                                                <div className="text-center py-10 text-green-500">
                                                    <FaCheckCircle className="text-4xl mx-auto mb-3" />
                                                    <p>Route appears clear based on latest NHA travel advisories.</p>
                                                </div>
                                            )
                                        )}
                                        {advisories.length > 0 && (
                                            <p className="text-[10px] text-text-muted/40 text-center mt-2">
                                                Source: NHMP Travel Advisory Portal
                                            </p>
                                        )}
                                    </>
                                ) : (
                                    <div className="text-center py-10 text-text-muted/50">
                                        <FaRoad className="text-4xl mx-auto mb-3 opacity-30" />
                                        <p>Enter route details to view alerts</p>
                                    </div>
                                )}
                            </div>
                        </div>
                    </div>

                    {/* Right Content */}
                    <div className="lg:col-span-8 space-y-6">
                        {/* Map Container */}
                        <div className="glassmorphism rounded-2xl overflow-hidden border border-gray-200 dark:border-border-dark h-[500px] relative bg-surface-light dark:bg-surface-dark group z-0">
                            <MapContainer 
                                center={mapCenter} 
                                zoom={6} 
                                style={{ height: '100%', width: '100%' }}
                                className="z-0"
                            >
                                {/* Dark Mode OpenStreetMap Tiles via CartoDB */}
                                <TileLayer
                                    url="https://{s}.basemaps.cartocdn.com/rastertiles/dark_all/{z}/{x}/{y}{r}.png"
                                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
                                />
                                
                                {startCoords && (
                                    <Marker position={[startCoords.lat, startCoords.lng]} icon={startIcon}>
                                        <Popup>Starting Point: {formData.startLocation}</Popup>
                                    </Marker>
                                )}
                                
                                {endCoords && (
                                    <Marker position={[endCoords.lat, endCoords.lng]} icon={endIcon}>
                                        <Popup>Destination: {formData.endLocation}</Popup>
                                    </Marker>
                                )}

                                {routeGeometry.length > 0 && (
                                    <Polyline 
                                        positions={routeGeometry} 
                                        color="#00BCD4" 
                                        weight={5} 
                                        opacity={0.8} 
                                    />
                                )}

                                {advisories.map((alert, idx) => {
                                    if (!alert.coordinates || !alert.coordinates.lat) return null;
                                    const isSevere = alert.alertType === 'Road Closure' || alert.alertType === 'Accident';
                                    return (
                                        <Marker 
                                            key={idx} 
                                            position={[alert.coordinates.lat, alert.coordinates.lng]}
                                            icon={isSevere ? severeAlertIcon : warningAlertIcon}
                                        >
                                            <Popup>
                                                <div style={{ fontFamily: 'Inter, sans-serif', maxWidth: '220px' }}>
                                                    <h3 style={{ margin: '0 0 4px 0', fontSize: '13px', fontWeight: 'bold', color: '#1a1a2e' }}>
                                                        {alert.alertType}
                                                    </h3>
                                                    <p style={{ margin: '0 0 4px 0', fontSize: '11px', fontWeight: 'bold', color: '#00BCD4' }}>
                                                        {alert.highway || alert.title}
                                                    </p>
                                                    <p style={{ margin: '0 0 4px 0', fontSize: '11px', color: '#555' }}>
                                                        <strong>Condition:</strong> {alert.condition}
                                                    </p>
                                                    {alert.location && alert.location !== 'Unknown' && (
                                                        <p style={{ margin: '0 0 4px 0', fontSize: '10px', color: '#666' }}>
                                                            <strong>Loc:</strong> {alert.location}
                                                        </p>
                                                    )}
                                                    {alert.recommendAlternative && (
                                                        <p style={{ margin: '4px 0 0 0', fontSize: '10px', fontWeight: 'bold', color: '#ef4444' }}>
                                                            ⚠️ Recommendation: Take Alternative Route
                                                        </p>
                                                    )}
                                                </div>
                                            </Popup>
                                        </Marker>
                                    );
                                })}

                                <FitBounds 
                                    routeCoords={routeGeometry} 
                                    startCoords={startCoords} 
                                    endCoords={endCoords} 
                                    markers={advisories} 
                                />
                            </MapContainer>
                        </div>

                        {/* Suggested Alternative Routes */}
                        <div className="glassmorphism rounded-2xl p-6 border border-border-dark">
                            <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-6">Suggested Alternative Routes</h2>
                            
                            <div className="space-y-4">
                                {showResults ? (
                                    alternativeRoutes.length > 0 ? (
                                        alternativeRoutes.map((route) => (
                                            <div key={route.id} className="bg-white/50 dark:bg-[#121A2A]/50 rounded-xl p-5 border border-gray-200 dark:border-border-dark/50 hover:border-primary/30 transition-all shadow-sm">
                                                <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                                                    <div>
                                                        <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-1">{route.name}</h3>
                                                        <p className="text-text-muted text-sm">{route.description}</p>
                                                    </div>
                                                    
                                                    <div className="flex items-center gap-6">
                                                        <div className="text-right">
                                                            <div className="text-gray-900 dark:text-white font-bold text-lg">{route.distance}</div>
                                                            <div className="text-text-muted text-xs">Distance</div>
                                                        </div>
                                                        <div className="text-right">
                                                            <div className="font-bold text-lg text-green-400">
                                                                {route.time}
                                                            </div>
                                                            <div className="text-text-muted text-xs">Est. Time</div>
                                                        </div>
                                                        <button 
                                                            onClick={() => viewAlternativeRoute(route)}
                                                            className="px-4 py-2 bg-[#1E293B] hover:bg-primary hover:text-white text-text-muted rounded-lg text-sm font-medium transition-all flex items-center gap-2"
                                                        >
                                                            <FaDirections />
                                                            View
                                                        </button>
                                                    </div>
                                                </div>
                                            </div>
                                        ))
                                    ) : (
                                        <div className="text-center py-8 text-text-muted/50">
                                            <p>No alternative routes generated. Primary route seems best.</p>
                                        </div>
                                    )
                                ) : (
                                    <div className="text-center py-8 text-text-muted/50">
                                        <p>Search for a route to see alternatives</p>
                                    </div>
                                )}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default RoutePlanning;
