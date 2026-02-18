import sys
import os
from analyzer import BikeShareSystem
from algorithms import benchmark_sort
from numerical import analyze_durations
from visualization import plot_top_stations, plot_duration_histogram
from pricing import TripFareCalculator, RegularPricing, SubscriberPricing
from utils import format_currency, ensure_dir

def main_menu():
    print("\n" + "="*30)
    print("   CITY BIKE ANALYSIS SYSTEM   ")
    print("="*30)
    print("1. View Global Statistics & Pricing (NumPy + Strategy)")
    print("2. Plot Trip Distributions (Matplotlib)")
    print("3. Analyze Top 5 Stations")
    print("4. Exit")
    return input("Select an option (1-4): ")

def main():
    ensure_dir('output/figures')
    
    system = BikeShareSystem()
    
    try:
        print(" Loading system data...")
        system.load_data('data/stations.csv', 'data/trips.csv')
        
        print(" Sorting trips using Merge Sort...")
        system.trips = benchmark_sort(system.trips, key_func=lambda x: x.duration, label="Merge Sort")

        while True:
            choice = main_menu()
            
            if choice == '1':
                stats = analyze_durations(system.trips)
                print("\n --- Global Statistics ---")
                for key, value in stats.items():
                    print(f"{key.capitalize()}: {value:.2f} min")

                print("\n --- Estimated Revenue Analysis ---")
                reg_calc = TripFareCalculator(RegularPricing())
                sub_calc = TripFareCalculator(SubscriberPricing())
                
                avg_duration = stats['mean']
                reg_fare = reg_calc.calculate_fare(avg_duration)
                sub_fare = sub_calc.calculate_fare(avg_duration)
                
                print(f"Regular Fare (Avg Trip):    {format_currency(reg_fare)}")
                print(f"Subscriber Fare (Avg Trip): {format_currency(sub_fare)}")
                print("-" * 30)

            elif choice == '2':
                durations = [t.duration for t in system.trips]
                plot_duration_histogram(durations)
                print(f" Chart saved to: output/figures/duration_dist.png")

            elif choice == '3':
                counts = {}
                for t in system.trips:
                    station_name = system.stations[t.start_id].name if t.start_id in system.stations else "Unknown"
                    counts[station_name] = counts.get(station_name, 0) + 1
                
                sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
                plot_top_stations(sorted_counts)
                print(f" Chart saved to: output/figures/top_stations.png")

            elif choice == '4':
                print("Exiting system. Goodbye!")
                break
            else:
                print(" Invalid choice. Please enter 1-4.")

    except Exception as e:
        print(f" Critical Error: {e}")

if __name__ == "__main__":
    main()
