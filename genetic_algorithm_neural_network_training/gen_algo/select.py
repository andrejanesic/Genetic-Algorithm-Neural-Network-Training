# -*- coding: utf-8 -*-

import pandas as pd


def select(pop: pd.DataFrame, p: float) -> pd.DataFrame:
    """
    Selects the top p part of the population (for example, p = 0.50). This
    creates a selection of breeding candidates, and also creates space for new
    individuals.
    """

    # first sort by cost, low to high
    pop.sort_values(by=["Cost"], ascending=True, inplace=True)
    to_drop = int((1 - p) * len(pop))
    pop.drop(pop.tail(to_drop).index, inplace=True)
    pop.reset_index(drop=True, inplace=True)
    return pop
