# -*- coding: utf-8 -*-

from ..common import args
from typing import List
import pandas as pd
import subprocess
import re


def cost(indiv: List[float]) -> float:
    """
    Cost function for the genetic algorithm. Calls the neural network with the
    individual data to get the result. The smaller the cost, the better.
    """

    comm = [args().get_cost_exe()]
    comm.extend([str(g) for g in indiv])
    comm = [" ".join(comm)]
    result = subprocess.run(comm, stdout=subprocess.PIPE, shell=True)
    res = result.stdout.decode('utf-8')
    res = re.search(r'(\-?[\d\.]+)', res).group(1)
    cost = abs(float(res))
    return cost

def cost_iter(pop: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the cost for each member of the population with float("inf")
    in cost column.
    """

    for i in range(len(pop)):
        if pop.iloc[i, -1] != float("inf"):
            continue
        l = pop.iloc[i, :-1].values.flatten().tolist()
        c = cost(l)
        pop.iloc[i, -1] = c
    return pop