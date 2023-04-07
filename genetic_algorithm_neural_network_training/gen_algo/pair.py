# -*- coding: utf-8 -*-

import pandas as pd
from typing import List
import random


def pair(pop: pd.DataFrame, n: int) -> List[List[int]]:
    """
    Creates pairs of individuals for breeding. Returns a list of lists, each
    containing only two elements--the index of each individual in the
    breeding pair. The first element is the index of the fitter individual.
    Pairings are selected using fitness-weighted roulette.
    """

    pop.sort_values(by=["Cost"], ascending=True, inplace=True)
    # 1 / cost because we want to give lower costs a better score
    roulette = 1.0 / pop["Cost"]
    roulette = pd.DataFrame(roulette)
    roulette.columns = ["Inverted Cost"]
    roulette["Normalized Cost"] = roulette["Inverted Cost"] / roulette["Inverted Cost"].sum()
    roulette.sort_values(by=["Normalized Cost"], ascending=True, inplace=True)
    roulette["P"] = roulette["Normalized Cost"].cumsum()

    def select_random() -> int:
        """
        Create a random number r in [0-1). Add row to roulette df. Find first
        index with probability larger than r. Remove random number.
        """
        r = random.random()
        roulette.loc[len(roulette)] = r
        roulette.sort_values(by=["P"], ascending=False, inplace=True)
        ind = roulette.index[roulette['P'] > r][-1]
        roulette.drop(index=roulette.index[roulette['P'] == r], inplace=True)
        return ind
    
    all_pairs = []
    for _ in range(n):
        i1, i2 = select_random(), select_random()
        x1, x2 = pop.iloc[i1], pop.iloc[i2]
        if x1["Cost"] < x2["Cost"]:
            all_pairs.append([i1, i2])
        else:
            all_pairs.append([i2, i1])
    return all_pairs
