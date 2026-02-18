from abc import ABC, abstractmethod

class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self, duration_minutes):
        pass

class RegularPricing(PricingStrategy):
    def calculate(self, duration_minutes):
        return duration_minutes * 0.50

class SubscriberPricing(PricingStrategy):
    def calculate(self, duration_minutes):
        return 10.0 + (duration_minutes * 0.10)

class TripFareCalculator:
    def __init__(self, strategy: PricingStrategy):
        self.strategy = strategy
        
    def set_strategy(self, strategy: PricingStrategy):
        self.strategy = strategy
        
    def calculate_fare(self, duration):
        return self.strategy.calculate(duration)