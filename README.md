City Bike Analysis System

Project Overview
This project is a high-performance Data Analysis Platform designed to process and visualize urban bike-sharing datasets. It demonstrates advanced Python concepts, including Software Architecture Patterns, Custom Algorithms, and Data Science Libraries.

Key Features & Technical Stack

Software Architecture (OOP & Patterns)
Domain Modeling: Used Abstract Base Classes (ABC) to define core entities (Station, Trip), ensuring strict interface enforcement.

Factory Design Pattern: Implemented for robust data initialization and decoupling the CSV parsing logic from the business logic.

Strategy Design Pattern: Flexible pricing engine to calculate trip fares based on user types (Subscriber vs. Casual).

Algorithms & PerformanceMerge Sort: 
Custom implementation of the Merge Sort algorithm ($O(n \log n)$) for stable and efficient sorting of massive trip datasets.NumPy Integration: High-speed numerical computing for calculating mean, median, standard deviation, and detecting outliers.

Analytics & Visualization
Matplotlib: Automated generation of professional insights:

Trip duration distribution (Histogram).

Top-performing stations (Bar Charts).

User demographics (Pie Charts).

Project Structure
├── data/               # Raw CSV datasets
├── models/             # OOP Domain Models (Entity, Trip, Station)
├── factories/          # Factory Pattern implementations
├── algorithms/         # Custom Sorting & Benchmarking
├── analytics/          # NumPy-based statistical logic
├── output/             # Generated Reports & Figures
└── main.py             # System Entry Point

Getting Started
1. Prerequisites
Ensure you have Python installed, then install dependencies:
pip install numpy matplotlib pandas

2. Execution
First, generate the synthetic dataset (if needed):
python data_generator.py
Then, launch the interactive analysis system:
python main.py

Sample Results
The system automatically generates a summary_report.txt and saves all visualizations in output/figures/, providing actionable insights into urban mobility patterns.
