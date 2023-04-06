# -*- coding: utf-8 -*-

import pandas as pd
from ..common import PopulationCost


def make_selection(pop: pd.DataFrame, p: float) -> pd.DataFrame:
    """
    Selects the top p part of the population (for example, p = 0.50). This
    creates a selection of breeding candidates, and also creates space for new
    individuals after breeding is complete. The
    """

    # first sort by cost, low to high
    pop.sort_values(by=['Cost'], ascending=False, inplace=True)
    return pop.head(len(pop) * p)