# Factory Reallocation & Shipping Optimization Recommendation System

## Overview

This project focuses on improving factory allocation and shipping efficiency for Nassau Candy Distributor. The system analyzes sales, profitability, product demand, and factory performance data to generate data-driven recommendations for factory reassignment and operational optimization.

The objective is to support decision-makers in identifying the most efficient factory-product assignments while maintaining profitability and reducing operational inefficiencies.


## Problem Statement

Nassau Candy Distributor currently relies on static product-to-factory assignments. This approach may lead to:

* Inefficient shipping operations
* Suboptimal factory utilization
* Increased operational costs
* Reduced profitability

This project introduces a recommendation system capable of analyzing historical business data and providing optimization insights through an interactive dashboard.


## Dataset Information

The dataset contains:

* 10,194 records
* Product information
* Sales and profit metrics
* Regional demand data
* Shipping information
* Factory assignments

Key attributes include:

* Product Name
* Region
* Ship Mode
* Sales
* Units
* Cost
* Gross Profit



## Technologies Used

* Python
* Pandas
* NumPy
* Streamlit
* Scikit-Learn



## Features

### Factory Profitability Analysis

Evaluate profitability across manufacturing facilities.

### Region Profitability Analysis

Identify high-performing regions.

### Product Profitability Analysis

Analyze profit contribution of individual products.

### Product Demand Analysis

Evaluate product demand using units sold.

### Recommendation Dashboard

Generate ranked recommendations based on profitability and demand.

### Factory Optimization Simulator

Compare current factory assignments and recommended alternatives.

### What-If Scenario Analysis

Estimate the impact of alternative factory allocation decisions.

### Risk & Impact Panel

Assess reassignment risk levels and confidence scores.



## Dashboard Modules

* Dataset Overview
* Factory Profitability
* Region Profitability
* Product Profitability
* Product Demand
* Recommendation Dashboard
* Factory Optimization Simulator
* Predicted Factory Performance
* What-If Scenario Analysis
* Risk & Impact Assessment



## Project Structure

```text
factory-reallocation-optimization/
│
├── app.py
├── requirements.txt
├── Nassau Candy Distributor.csv
├── Research_Paper.pdf
├── Executive_Summary.pdf
└── README.md
```



## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```



## Key Findings

* Lot's O' Nuts is the highest-performing factory.
* Wicked Choccy's is the second most profitable factory.
* Pacific region contributes the highest regional profit.
* Wonka Bar products generate the majority of profit and demand.
* Low-performing products can be evaluated for reassignment opportunities.



## Future Scope

* Machine Learning-based demand forecasting
* Lead-time prediction models
* Transportation route optimization
* Real-time logistics monitoring
* Advanced factory allocation algorithms

#Deployed Project Link: https://factory-reallocation-optimization.streamlit.app/

## Author

Aditya Jariwala

Data Analytics & Supply Chain Optimization Project
