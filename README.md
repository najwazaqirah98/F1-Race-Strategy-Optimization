# 🏎️ Formula One Race Strategy Optimization Using Monte Carlo Simulation and Genetic Algorithm

## Overview

This project presents an interactive Formula One race strategy decision support system developed using Python, Monte Carlo Simulation, and Genetic Algorithms (GA). The framework is designed to evaluate and optimize race strategies under uncertain racing conditions by integrating tyre performance modelling, Safety Car deployment, weather uncertainty, and stochastic race events.

The primary objective is to identify the optimal combination of tyre compounds and pit stop timing that minimizes total race time while accounting for uncertainty commonly observed in Formula One racing.

---

## Dashboard Preview

> Add your Streamlit dashboard screenshot inside the `figures` folder and update the filename below.

```text
figures/Dashboard.png
```

---

## Research Objective

The objectives of this project are to:

- Develop a Formula One race simulation model using a lap-by-lap approach.
- Model tyre performance based on tyre pace and degradation characteristics.
- Incorporate uncertainty through Safety Car deployment and weather events.
- Evaluate race strategies using Monte Carlo Simulation.
- Optimize pit stop timing using brute-force search.
- Identify near-optimal race strategies using Genetic Algorithms.
- Develop an interactive dashboard for strategy analysis and decision support.

---

## Key Features

### ✅ Race Simulation Model

- Lap-by-lap race simulation
- Race time calculation
- Pit stop modelling
- Strategy evaluation

### ✅ Tyre Performance Modelling

- Soft, Medium, and Hard compounds
- Tyre pace model
- Piecewise tyre degradation model
- Tyre cliff behaviour

### ✅ Uncertainty Modelling

- Driver performance variability
- Safety Car probability model
- Rain event modelling
- Random race disturbances

### ✅ Monte Carlo Simulation

- Statistical race analysis
- Large-scale simulation runs
- Performance distribution analysis
- Mean, best, worst, and standard deviation metrics

### ✅ Optimization

- Brute-force optimization
- Pit stop optimization
- Genetic Algorithm optimization
- Strategy comparison analysis

### ✅ Interactive Dashboard

- Single Strategy Analysis
- Strategy Comparison
- Pit Stop Optimization
- Genetic Algorithm Optimization
- Interactive visualization

---

## Methodology

The overall workflow of the system is shown below:

```text
Input Parameters
        │
        ▼
Race Simulation Model
        │
        ▼
Tyre Performance Model
        │
        ▼
Uncertainty Modelling
(Safety Car + Weather)
        │
        ▼
Monte Carlo Simulation
        │
        ▼
Strategy Evaluation
        │
 ┌──────┴────────┐
 ▼               ▼
Brute Force   Genetic Algorithm
Optimization  Optimization
        │
        ▼
Optimal Strategy
```

---

## Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Simulation and optimization |
| NumPy | Numerical computation |
| Pandas | Data processing |
| Matplotlib | Data visualization |
| Streamlit | Interactive dashboard |
| PyGAD | Genetic Algorithm implementation |

---

## Project Structure

```text
F1-Race-Strategy-Optimization

├── src
│   ├── race_model.py
│   ├── monte_carlo.py
│   ├── main.py
│   └── genetic_algorithm.py
│
├── figures
│   ├── Dashboard.png
│   ├── MonteCarloHistogram.png
│   ├── PitStopOptimization.png
│   └── GA_ConvergenceCurve.png
│
├── results
│   ├── MonteCarloResults.csv
│   ├── StrategyComparison.csv
│   ├── PitOptimizationData.csv
│   └── GA_BestStrategy.csv
│
├── README.md
├── LICENSE
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/najwazaqirah98/F1-Race-Strategy-Optimization.git
```

Navigate into the project folder:

```bash
cd F1-Race-Strategy-Optimization
```

Install required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit dashboard:

```bash
streamlit run app.py
```

---

## Future Improvements

Potential future extensions include:

- Multi-stop strategy optimization
- Fuel consumption modelling
- Dynamic weather forecasting
- Driver aggressiveness modelling
- Reinforcement Learning optimization
- Real-world Formula One telemetry integration

---

## Research Contribution

This project contributes an interactive Formula One race strategy decision support system that combines tyre performance modelling, uncertainty modelling, Monte Carlo Simulation, and Genetic Algorithm optimization. The framework provides a practical approach for evaluating and optimizing race strategies under uncertain race conditions while offering an intuitive dashboard for visualization and analysis.

---

## Author

**Najwa Zaqirah Taufik**

---

## License

This project is released for academic and research purposes.
