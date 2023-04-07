# -*- coding: utf-8 -*-

import pandas as pd
from .select import *
from .pair import *
from .breed import *
from .mutate import *
from .cost import *


def evolve(pop: pd.DataFrame, p: float, elites: int, lb: int, ub: int, mut_count: int) -> pd.DataFrame:
    """
    Evolves the population, creating a new generation and inserting into the
    population. The cost is calculated for each new/modified individual.
    """
    n = len(pop)
    selected = select(pop, p)
    pairs = pair(selected, n - len(selected))
    breeded = breed(pairs, selected)
    mutated = mutate(breeded, elites, lb, ub, mut_count)
    next_gen = cost_iter(mutated)
    assert(len(next_gen) == n)
    return next_gen
