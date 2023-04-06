# -*- coding: utf-8 -*-

from ..common import args
from typing import List
import subprocess

def cost(indiv: List[int]) -> float:
    """
    Cost function for the genetic algorithm. Calls the neural network with the
    individual data to get the result.
    """

    comm = [args().get_cost_exe()]
    comm.extend(indiv)
    proc = subprocess.Popen(comm, stdout=subprocess.PIPE, shell=True)
    (cost, err) = proc.communicate()
    return cost