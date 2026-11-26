# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:04:09 2026

@author: najwa
"""

# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from race_model import simulate_race
from monte_carlo import monte_carlo


# ===================================
# SINGLE RACE TEST
# ===================================

time = simulate_race(
    pit_lap=20,
    start_tyre="Medium",
    next_tyre="Hard"
)

print("Race Time =", time)

# ===================================
# MONTE CARLO
# ===================================

results = monte_carlo(
    pit_lap=20,
    n_runs=10000,
    start_tyre="Medium",
    next_tyre="Hard"
)

print()
print("Average =", np.mean(results))
print("Best =", np.min(results))
print("Worst =", np.max(results))
print("STD =", np.std(results))

# ===================================
# SAVE MONTE CARLO RESULTS
# ===================================

df_montecarlo = pd.DataFrame({

    "RaceTime": results

})

df_montecarlo.to_csv(

    "MonteCarloResults.csv",

    index=False

)

print("MonteCarloResults.csv saved")

# ===================================
# HISTOGRAM
# ===================================

plt.figure(figsize=(8,5))

plt.hist(
    results,
    bins=50
)

plt.xlabel("Race Time (s)")
plt.ylabel("Frequency")
plt.title("Monte Carlo F1 Simulation")

plt.grid(True)

plt.savefig(

    "MonteCarloHistogram.png",

    dpi=300,

    bbox_inches='tight'

)

plt.show()

print("MonteCarloHistogram.png saved")

strategies = [

    ("Soft", "Hard"),
    ("Soft", "Medium"),
    ("Medium", "Hard")

]

strategy_results = []

print("\n===== STRATEGY COMPARISON =====")

for start_tyre, next_tyre in strategies:

    best_lap = 0
    best_time = 999999

    for pit in range(10,40):

        results = monte_carlo(
            pit_lap=pit,
            n_runs=1000,
            start_tyre=start_tyre,
            next_tyre=next_tyre
        )

        avg_time = np.mean(results)

        if avg_time < best_time:

            best_time = avg_time
            best_lap = pit

    print(
        f"{start_tyre} -> {next_tyre}"
    )

    print(
        f"Best Lap = {best_lap}"
    )

    print(
        f"Average Time = {best_time:.2f} s"
    )

    print()
    
    strategy_results.append([

    start_tyre,

    next_tyre,

    best_lap,

    best_time

])

df_strategy = pd.DataFrame(

    strategy_results,

    columns=[

        "StartTyre",

        "NextTyre",

        "BestPitLap",

        "AverageRaceTime"

    ]

)

df_strategy.to_csv(

    "StrategyComparison.csv",

    index=False

)

print("StrategyComparison.csv saved")

# ===================================
# PIT STOP OPTIMIZATION
# ===================================

pit_list = []
avg_times = []

for pit in range(10,40):

    results = monte_carlo(
        pit_lap=pit,
        n_runs=1000,
        start_tyre="Medium",
        next_tyre="Hard"
    )

    pit_list.append(pit)
    avg_times.append(np.mean(results))

best_index = np.argmin(avg_times)

df_pit = pd.DataFrame({

    "PitLap": pit_list,

    "AverageRaceTime": avg_times

})

df_pit.to_csv(

    "PitOptimizationData.csv",

    index=False

)

print("PitOptimizationData.csv saved")

print()
print("Best Pit Lap =", pit_list[best_index])
print("Average Time =", avg_times[best_index])

plt.figure(figsize=(10,6))

plt.plot(
    pit_list,
    avg_times,
    marker='o'
)

plt.scatter(

    pit_list[best_index],

    avg_times[best_index],

    color='red',

    s=120,

    label='Optimal Pit Stop'

)

plt.legend()

plt.xlabel("Pit Stop Lap")
plt.ylabel("Average Race Time (s)")
plt.title("Pit Stop Optimization")

plt.grid(True)

plt.savefig(

    "PitStopOptimization.png",

    dpi=300,

    bbox_inches='tight'

)

plt.show()

print("PitStopOptimization.png saved")