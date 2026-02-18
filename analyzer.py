import pandas as pd
import os
from models import Station, Trip
from factories import StationFactory, TripFactory

class BikeShareSystem:
    def __init__(self):
        self.stations = {}  
        self.trips = []     
        self.raw_trips_df = None

    def load_data(self, stations_path, trips_path):
        print(f"--- Loading Data ---")
        
        abs_stations = os.path.abspath(stations_path)
        abs_trips = os.path.abspath(trips_path)
        
        if not os.path.exists(stations_path):
            raise FileNotFoundError(f"Missing: {abs_stations}")
        if not os.path.exists(trips_path):
            raise FileNotFoundError(f"Missing: {abs_trips}")

        stations_df = pd.read_csv(stations_path)
        trips_df = pd.read_csv(trips_path)
        
        trips_df = trips_df.dropna(subset=['trip_id', 'start_station_id', 'end_station_id'])
        trips_df = trips_df[trips_df['duration_minutes'] > 0]
        
        self.raw_trips_df = trips_df
        self._initialize_objects(stations_df, trips_df)

    def _initialize_objects(self, stations_df, trips_df):
        for _, row in stations_df.iterrows():
            station_obj = StationFactory.create_station(row)
            self.stations[station_obj.id] = station_obj
            
        for _, row in trips_df.iterrows():
            trip_obj = TripFactory.create_trip(row)
            self.trips.append(trip_obj)
        print(f"System Ready: {len(self.stations)} Stations and {len(self.trips)} Trips loaded.")