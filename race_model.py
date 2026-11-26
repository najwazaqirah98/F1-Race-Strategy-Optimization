# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:01:27 2026

@author: najwa
"""

# -*- coding: utf-8 -*-

import numpy as np


# =====================================
# TYRE DEGRADATION MODEL
# =====================================

def tyre_degradation(tyre_age, tyre_type):

    if tyre_type == "Soft":

        if tyre_age <= 12:

            return 0.12 * tyre_age

        else:

            return (
                0.12 * 12
                + 0.25 * (tyre_age - 12)
            )

    elif tyre_type == "Medium":

        if tyre_age <= 20:

            return 0.08 * tyre_age

        else:

            return (
                0.08 * 20
                + 0.18 * (tyre_age - 20)
            )

    elif tyre_type == "Hard":

        if tyre_age <= 25:

            return 0.05 * tyre_age

        else:

            return (
                0.05 * 25
                + 0.10 * (tyre_age - 25)
            )

    return 0


# =====================================
# TYRE PACE MODEL
# =====================================

def tyre_base_time(tyre_type):

    if tyre_type == "Soft":

        return -0.4

    elif tyre_type == "Medium":

        return 0.0

    elif tyre_type == "Hard":

        return 0.4

    return 0.0


# =====================================
# MAIN RACE SIMULATION
# =====================================

def simulate_race(

        pit_lap,

        start_tyre="Medium",

        next_tyre="Hard"

):

    TOTAL_LAPS = 56

    PIT_LOSS = 22

    total_time = 0

    # =================================
    # SAFETY CAR
    # =================================

    safety_car_lap = None

    if np.random.rand() < 0.20:

        safety_car_lap = np.random.randint(
            5,
            TOTAL_LAPS - 5
        )

    # =================================
    # RAIN EVENT
    # =================================

    rain_lap = None

    if np.random.rand() < 0.05:

        rain_lap = np.random.randint(
            15,
            45
        )

    # =================================
    # PIT LOSS REDUCTION
    # =================================

    effective_pit_loss = PIT_LOSS

    if safety_car_lap is not None:

        if abs(
            pit_lap - safety_car_lap
        ) <= 2:

            effective_pit_loss = 12

    # =================================
    # RACE LOOP
    # =================================

    for lap in range(TOTAL_LAPS):

        if lap < pit_lap:

            tyre_age = lap
            current_tyre = start_tyre

        else:

            tyre_age = lap - pit_lap
            current_tyre = next_tyre

        # Pace effect

        pace = tyre_base_time(
            current_tyre
        )

        # Degradation effect

        deg = tyre_degradation(
            tyre_age,
            current_tyre
        )

        lap_time = (
            90
            + pace
            + deg
            + np.random.normal(
                0,
                0.2
            )
        )

        # Rain effect

        if rain_lap is not None:

            if lap >= rain_lap:

                lap_time += np.random.uniform(
                    0.2,
                    0.5
                )

        # Safety car effect

        if lap == safety_car_lap:

            lap_time += 5

        total_time += lap_time

    total_time += effective_pit_loss

    return total_time