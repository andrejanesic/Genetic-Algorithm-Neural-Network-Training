# -*- coding: utf-8 -*-

import pandas as pd
from typing import List
from random import uniform


def get_cols(n_genes: int) -> List[str]:
    """
    Generates a list of columns to be used in the population DataFrame.
    """

    cols = [i + 1 for i in range(n_genes)]
    cols.append("Cost")
    return cols


def gen_indiv(n_genes: int, lower_bound: int, upper_bound: int) -> List[float]:
    """
    Creates an individual with a set of genes. The individual is part of the
    population. Gene values are real numbers, generated in a random uniform
    manner in the (lower_bound, upper_bound) range.
    """

    i = [uniform(lower_bound, upper_bound) for _ in range(n_genes)]
    i.append(float("inf"))
    return i


def gen_pop(
    n_individuals: int, n_genes: int, lower_bound: int, upper_bound: int
) -> pd.DataFrame:
    """
    Creates a population. A population consists of individuals (number of
    individuals is represented by n_individuals. Each individual is generated
    using gen_indiv, with the given parameters.
    """

    df = pd.DataFrame(columns=get_cols(n_genes))
    for _ in range(n_individuals):
        df.loc[len(df)] = gen_indiv(n_genes, lower_bound, upper_bound)
    return df
