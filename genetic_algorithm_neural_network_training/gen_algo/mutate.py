# -*- coding: utf-8 -*-

import pandas as pd
import random


def mutate(pop: pd.DataFrame, mut_perc: int, lb: int, ub: int, mut_count: int) -> pd.DataFrame:
    """
    Mutates the gene by setting it to a random, uniformly-chosen number in the
    given range. Starts from the mut_perc percentage individual, counting from
    the back. Resets the index.
    """
    pop.sort_values(by=["Cost"], ascending=True, inplace=True)
    pop.reset_index(drop=True, inplace=True)
    genes = len(pop.head(1))
    for i in range(int(len(pop) * (1 - mut_perc / 100)), len(pop)):
        for _ in range(mut_count):
            val = random.uniform(lb, ub)
            gen = random.choice(range(genes))
            pop.iloc[i, gen] = val

        # mark for cost recalc
        pop.iloc[i, -1] = float("inf")
    return pop
