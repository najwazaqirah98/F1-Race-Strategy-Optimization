# -*- coding: utf-8 -*-
"""
Genetic Algorithm for F1 Race Strategy Optimization
"""

import numpy as np
import pandas as pd
import pygad
import matplotlib.pyplot as plt

from monte_carlo import monte_carlo


# ==========================================
# FITNESS FUNCTION
# ==========================================

def fitness_func(ga_instance, solution, solution_idx):

    tyre_map = {
        0: "Soft",
        1: "Medium",
        2: "Hard"
    }

    start_tyre = tyre_map[int(solution[0])]
    pit_lap = int(solution[1])
    next_tyre = tyre_map[int(solution[2])]

    # avoid unrealistic strategy
    if start_tyre == next_tyre:
        return 0.0000001

    results = monte_carlo(
        pit_lap=pit_lap,
        n_runs=200,      # kecilkan dulu untuk debugging
        start_tyre=start_tyre,
        next_tyre=next_tyre
    )

    avg_time = np.mean(results)

    fitness = 1 / avg_time

    return fitness


# ==========================================
# GENETIC ALGORITHM
# ==========================================

ga_instance = pygad.GA(

    num_generations=30,

    num_parents_mating=10,

    sol_per_pop=30,

    num_genes=3,

    fitness_func=fitness_func,

    gene_space=[

        [0, 1, 2],       # Start Tyre

        range(10, 40),   # Pit Lap

        [0, 1, 2]        # Next Tyre

    ],

    mutation_num_genes=1,

    crossover_type="single_point",

    mutation_type="random",

    parent_selection_type="sss",

    keep_parents=2
)

# ==========================================
# RUN GA
# ==========================================

print("Running Genetic Algorithm...")
print()

ga_instance.run()

print("GA Completed!")
print()

# ==========================================
# BEST SOLUTION
# ==========================================

solution, fitness, solution_idx = ga_instance.best_solution()

tyre_map = {
    0: "Soft",
    1: "Medium",
    2: "Hard"
}

best_start_tyre = tyre_map[int(solution[0])]
best_pit_lap = int(solution[1])
best_next_tyre = tyre_map[int(solution[2])]

print("========== BEST STRATEGY ==========")

print("Start Tyre :", best_start_tyre)

print("Pit Lap    :", best_pit_lap)

print("Next Tyre  :", best_next_tyre)

print("Fitness    :", fitness)

# ==========================================
# VALIDATION
# ==========================================

results = monte_carlo(
    pit_lap=best_pit_lap,
    n_runs=1000,
    start_tyre=best_start_tyre,
    next_tyre=best_next_tyre
)

print()
print("===== VALIDATION =====")

print("Average Race Time =", np.mean(results))

print("Best Race Time    =", np.min(results))

print("Worst Race Time   =", np.max(results))

print("STD               =", np.std(results))

ga_results = pd.DataFrame({

    "StartTyre":[best_start_tyre],

    "PitLap":[best_pit_lap],

    "NextTyre":[best_next_tyre],

    "AverageRaceTime":[np.mean(results)],

    "BestRaceTime":[np.min(results)],

    "WorstRaceTime":[np.max(results)],

    "STD":[np.std(results)]

})

ga_results.to_csv(

    "GA_BestStrategy.csv",

    index=False

)

print()
print("GA_BestStrategy.csv saved")

# ==========================================
# FITNESS CURVE
# ==========================================

plt.figure(figsize=(8,5))

plt.plot(
    ga_instance.best_solutions_fitness,
    linewidth=2
)

plt.xlabel("Generation")

plt.ylabel("Fitness")

plt.title("GA Convergence Curve")

plt.grid(True)

plt.savefig(

    "GA_ConvergenceCurve.png",

    dpi=300,

    bbox_inches='tight'

)

plt.show()

print("GA_ConvergenceCurve.png saved")

print()

print("===== BRUTE FORCE COMPARISON =====")

print("Brute Force Strategy:")
print("Medium -> Hard")
print("Pit Lap = 24")
print("Average Time = 5124.58")

print()

print("GA Strategy:")
print(
    f"{best_start_tyre} -> {best_next_tyre}"
)

print(
    f"Pit Lap = {best_pit_lap}"
)

print(
    f"Average Time = {np.mean(results):.2f}"
)

improvement = (
    5124.58
    - np.mean(results)
)

print()

print(
    "Difference =",
    round(improvement,3),
    "seconds"
)