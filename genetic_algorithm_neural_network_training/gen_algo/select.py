# -*- coding: utf-8 -*-

import pandas as pd


def select(pop: pd.DataFrame, n: int) -> pd.DataFrame:
    """
    Selects the top n members of the population, while discarding the rest.
    """

    # first sort by cost, low to high
    pop.sort_values(by=["Cost"], ascending=True, inplace=True)
    to_drop = len(pop) - n
    pop.drop(pop.tail(to_drop).index, inplace=True)
    pop.reset_index(drop=True, inplace=True)
    return pop
