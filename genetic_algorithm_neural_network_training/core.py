# -*- coding: utf-8 -*-

from .gen_algo import *
from .common import config
import sys


def main() -> None:
    # TODO add loading of multiple config files

    # get config
    pop_size = config().getint("algo", "pop_size")
    indiv_l = config().getint("algo", "indiv_l")
    lb = config().getint("algo", "sol_lb")
    ub = config().getint("algo", "sol_ub")
    sel_perc = config().getint("algo", "sel_perc") / 100
    mut_perc = config().getint("algo", "mut_perc")
    max_iter = config().getint("algo", "max_iter")
    mut_n = config().getint("algo", "mut_n")
    out_file = config().get("algo", "out_file")
    runs = config().getint("algo", "runs")
    if out_file == "sys.stdout":
        out_file = sys.stdout
    elif out_file == "sys.stderr":
        out_file = sys.stderr
    else:
        try:
            out_file = open(out_file, "a")
        except:
            out_file = sys.stdout

    # create population and calculate initial cost
    pop = gen_pop(pop_size, indiv_l, lb, ub)
    pop = cost_iter(pop)
    pop.sort_values(by=["Cost"], ascending=True, inplace=True)

    # params and first iter
    winner = pop.iloc[0]
    min_j = winner.loc["Cost"]
    avg_j = pop["Cost"].sum() / len(pop)
    iters = 1
    print("%f, %f" % (min_j, avg_j), file=out_file)

    # evolve until iters used or converged
    while min_j >= 0 and iters < max_iter:
        pop = evolve(pop, sel_perc, mut_perc, lb, ub, mut_n)
        pop.sort_values(by=["Cost"], ascending=True, inplace=True)
        curr_winner = pop.iloc[0]
        curr_j = curr_winner.loc["Cost"]
        if curr_j < min_j:
            min_j = curr_j
            winner = curr_winner
        iters += 1
        avg_j = pop["Cost"].sum() / len(pop)
        print("%f, %f" % (min_j, avg_j), file=out_file)

    # TODO save res
    return 0
