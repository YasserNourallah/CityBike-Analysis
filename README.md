# 🚲 City Bike Analysis System

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📝 Project Overview
This platform is a comprehensive **Data Analysis System** designed to process, analyze, and visualize urban bike-sharing datasets. It is built as a modular framework to demonstrate advanced Python concepts, software design patterns, and efficient algorithmic implementations.

---

## ✨ Technical Stack & Features

### 🏗️ Software Architecture (OOP & Patterns)
* **Domain Modeling:** Implemented **Object-Oriented Programming (OOP)** with **Abstract Base Classes (ABC)** to define core entities like `Station` and `Trip`.
* **Factory Design Pattern:** Used for robust data initialization, decoupling CSV parsing from the core business logic for better maintainability.
* **Strategy Design Pattern:** Built a flexible pricing engine to handle different user types (`Member` vs. `Casual`) without modifying the core `Trip` class.

### ⚡ Algorithms & High Performance
* **Merge Sort Algorithm:** A custom, manual implementation of the **Merge Sort** ($O(n \log n)$) to ensure stable and efficient sorting of large trip datasets.
* **Numerical Computing (NumPy):** Leveraged **NumPy Arrays** and vectorized operations for fast statistical calculations (Mean, Median, Std Dev, and Outlier Detection).

### 📊 Automated Analytics & Visualization
* **Matplotlib Integration:** Automated generation of professional insights saved directly to `output/figures/`:
    * Trip Duration Distributions (Histograms).
    * Top-performing Stations (Bar Charts).
    * User Type Demographics (Pie Charts).
* **Summary Reporting:** Generates an automated `summary_report.txt` containing key KPIs and data cleaning logs.

---

## 📂 Project Structure
```bash
├── data/               # Raw CSV datasets (trips.csv, maintenance.csv)
├── models/             # OOP Domain Models (Entity, Trip, Station)
├── factories/          # Factory Pattern implementations
├── algorithms/         # Custom Sorting (Merge Sort) & Benchmarking
├── analytics/          # NumPy-based statistical logic
├── output/             # Generated Reports & Figures
└── main.py             # System Entry Point & Interactive CLI


