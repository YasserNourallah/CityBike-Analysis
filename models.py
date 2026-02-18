from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, entity_id):
        self.id = entity_id

    @abstractmethod
    def __str__(self):
        pass

class Station(Entity):
    def __init__(self, station_id, name, latitude, longitude):
        super().__init__(station_id)
        self.name = name
        self.lat = float(latitude)
        self.lon = float(longitude)

    def __str__(self):
        return f"Station({self.id}): {self.name}"

class Trip(Entity):
    def __init__(self, trip_id, bike_id, start_id, end_id, duration, distance, user_id):
        super().__init__(trip_id)
        self.bike_id = bike_id
        self.start_id = start_id
        self.end_id = end_id
        self.duration = float(duration)  
        self.distance = float(distance)  
        self.user_id = user_id

    def __str__(self):
        return f"Trip {self.id}: Bike {self.bike_id}, {self.duration} min"