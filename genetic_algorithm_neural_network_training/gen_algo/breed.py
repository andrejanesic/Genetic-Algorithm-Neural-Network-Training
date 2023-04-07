# -*- coding: utf-8 -*-

from typing import List
import random
import pandas as pd


def breed(pairs: List[List[int]], pop: pd.DataFrame) -> pd.DataFrame:
    """
    Breeds the given pairs of individuals using heuristic crossover. The first
    parent in the pair is considered better.
    """
    for pair in pairs:
        i1, i2 = pair[0], pair[1]
        x1, x2 = pop.iloc[i1], pop.iloc[i2]
        r = random.random()
        y = r * (x1 - x2) + x1

        # mark for cost recalc
        y.iloc[-1] = float("inf")
        pop.loc[len(pop.index)] = y
    return pop
