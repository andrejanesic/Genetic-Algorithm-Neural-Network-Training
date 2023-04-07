# -*- coding: utf-8 -*-

import pandas as pd
from .select import *
from .pair import *
from .breed import *
from .mutate import *
from .cost import *


def evolve(pop: pd.DataFrame, p: float, mut_perc: int, lb: int, ub: int, mut_count: int) -> pd.DataFrame:
    """
    Evolves the population, creating a new generation and inserting into the
    population. The cost is calculated for each new/modified individual.
    """
    n = len(pop)
    candidates = select(pop, int(p * n))
    pairs = pair(candidates, n)
    breeded = breed(pairs, pop)
    mutated = mutate(breeded, mut_perc, lb, ub, mut_count)
    next_gen = cost_iter(mutated)
    next_gen = select(next_gen, n)
    assert(len(next_gen) == n)
    return next_gen
