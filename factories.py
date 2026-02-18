from models import Station, Trip

class StationFactory:
    @staticmethod
    def create_station(data):
        return Station(
            station_id=data['station_id'],
            name=data['name'],
            latitude=data['lat'],
            longitude=data['lon']
        )

class TripFactory:
    @staticmethod
    def create_trip(data):
        return Trip(
            trip_id=data['trip_id'],
            bike_id=data['bike_id'],
            start_id=data['start_station_id'],
            end_id=data['end_station_id'],
            duration=data['duration_minutes'],
            distance=data['distance_km'],
            user_id=data.get('user_id', 'Unknown')
        )