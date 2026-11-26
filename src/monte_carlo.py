# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:09:24 2026

@author: najwa
"""

# -*- coding: utf-8 -*-

import numpy as np

from race_model import simulate_race


def monte_carlo(

        pit_lap,

        n_runs,

        start_tyre,

        next_tyre

):

    results = []

    for i in range(n_runs):

        race_time = simulate_race(

            pit_lap=pit_lap,

            start_tyre=start_tyre,

            next_tyre=next_tyre

        )

        results.append(
            race_time
        )

    return np.array(
        results
    )