# -*- coding: utf-8 -*-

from typing import List, Tuple
import random
import pandas as pd


def breed(pairs: List[Tuple[int, int]], pop: pd.DataFrame) -> pd.DataFrame:
    """
    Breeds the given pairs of individuals using heuristic crossover. The first
    parent in the pair is considered better.
    """
    for pair in pairs:
        i1, i2 = pair
        x1, x2 = pop.iloc[i1], pop.iloc[i2]
        r = random.random()
        y = x1.subtract(x2)
        y = y.multiply(r)
        y = y.add(x1)

        # mark for cost recalc
        y.iloc[-1] = float("inf")
        pop.loc[len(pop.index)] = y
    return pop
