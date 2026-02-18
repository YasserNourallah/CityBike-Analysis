import matplotlib.pyplot as plt
import os

def plot_top_stations(station_counts, output_dir='output/figures'):
    """
    Creates a bar chart for the top 5 busiest stations.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    names = list(station_counts.keys())[:5]
    counts = list(station_counts.values())[:5]
    
    plt.figure(figsize=(10, 6))
    plt.bar(names, counts, color='skyblue', edgecolor='navy')
    plt.title('Top 5 Busiest Stations', fontsize=14)
    plt.xlabel('Station Name', fontsize=12)
    plt.ylabel('Number of Trips', fontsize=12)
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/top_stations.png")
    plt.show()

def plot_duration_histogram(durations, output_dir='output/figures'):
    """
    Creates a histogram to show the distribution of trip durations.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    plt.figure(figsize=(10, 6))
    plt.hist(durations, bins=20, color='salmon', edgecolor='black', alpha=0.7)
    plt.title('Distribution of Trip Durations', fontsize=14)
    plt.xlabel('Duration (Minutes)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig(f"{output_dir}/duration_dist.png")
    plt.show()