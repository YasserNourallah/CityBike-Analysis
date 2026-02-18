import numpy as np

def analyze_durations(trips):
    """
    Using NumPy to calculate statistics for trip durations.
    """
    durations = np.array([trip.duration for trip in trips])
    
    if durations.size == 0:
        return None

    stats = {
        "mean": np.mean(durations),
        "median": np.median(durations),
        "std_dev": np.std(durations),
        "max": np.max(durations),
        "min": np.min(durations)
    }
    return stats

def detect_outliers(trips, threshold=3):
    """
    Detect outliers using the Z-score method.
    Outliers are trips with duration significantly higher/lower than the mean.
    """
    durations = np.array([trip.duration for trip in trips])
    if durations.size == 0:
        return []

    mean = np.mean(durations)
    std = np.std(durations)
    
    z_scores = (durations - mean) / std
    
    outlier_indices = np.where(np.abs(z_scores) > threshold)[0]
    
    return [trips[i] for i in outlier_indices]

def get_station_coordinates(stations_dict):
    """
    Convert station dictionary into a NumPy array of coordinates (lat, lon).
    Useful for distance calculations.
    """
    coords = np.array([[s.lat, s.lon] for s in stations_dict.values()])
    return coords