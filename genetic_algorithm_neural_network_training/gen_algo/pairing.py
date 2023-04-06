# -*- coding: utf-8 -*-

import pandas as pd
from typing import List
import random

def make_pairing(pop: pd.DataFrame) -> List[List[int]]:
    """
    Creates pairs of individuals for breeding. Returns a list of lists, each
    containing only two elements--the index of each individual in the
    breeding pair.
    """

    available = {i for i in range(len(pop))}
    all_pairs = []
    while available:
        i1 = random.choice(available)
        available.remove(i1)
        if len(available) == 0:
            break
        i2 = random.choice(available)
        available.remove(i2)
        all_pairs.append([i1, i2])
    return all_pairs