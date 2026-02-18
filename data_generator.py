import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

base_path = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_path, 'data')

if not os.path.exists(data_dir):
    os.makedirs(data_dir)
    print(f"Created directory: {data_dir}")

np.random.seed(42)


names = ["Central", "University", "City Hall", "Park", "Square", "Tech Hub", "Old Town", "Harbor", "Arena", "West End", "North Gate", "Museum", "Business", "Lakeside", "Airport"]
stations = []
for i, name in enumerate(names):
    stations.append({
        "station_id": f"ST{100+i}",
        "name": name,  
        "capacity": int(np.random.choice([10, 20, 30])),
        "lat": 48.75,  
        "lon": 9.15    
    })

stations_file = os.path.join(data_dir, "stations.csv")
pd.DataFrame(stations).to_csv(stations_file, index=False)

trips = []
for i in range(1500):
    start_time = datetime(2024, 1, 1) + timedelta(minutes=np.random.randint(0, 500000))
    duration = float(np.random.randint(5, 60))
    trips.append({
        "trip_id": f"TR{10000+i}",
        "user_id": f"USR{np.random.randint(1000, 1100)}",
        "user_type": np.random.choice(["casual", "member"]),
        "bike_id": f"BK{np.random.randint(200, 300)}",
        "bike_type": np.random.choice(["classic", "electric"]),
        "start_station_id": f"ST{np.random.randint(100, 115)}",
        "end_station_id": f"ST{np.random.randint(100, 115)}",
        "start_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
        "end_time": (start_time + timedelta(minutes=duration)).strftime("%Y-%m-%d %H:%M:%S"),
        "duration_minutes": duration,
        "distance_km": round(np.random.uniform(1.0, 10.0), 2),
        "status": "completed"
    })

df_trips = pd.DataFrame(trips)
df_trips.loc[0:9, "duration_minutes"] = np.nan

trips_file = os.path.join(data_dir, "trips.csv")
df_trips.to_csv(trips_file, index=False)

print(f"✅ SUCCESS: Files created in {data_dir}")