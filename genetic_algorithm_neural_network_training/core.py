# -*- coding: utf-8 -*-

from .gen_algo import *
from .common import config
import sys


def main() -> None:
    configs = args().get_configs()
    for cfg in configs:

        # get config
        pop_size = config(cfg).getint("algo", "pop_size")
        indiv_l = config(cfg).getint("algo", "indiv_l")
        lb = config(cfg).getint("algo", "sol_lb")
        ub = config(cfg).getint("algo", "sol_ub")
        sel_perc = config(cfg).getint("algo", "sel_perc") / 100
        mut_perc = config(cfg).getint("algo", "mut_perc") / 100
        max_iter = config(cfg).getint("algo", "max_iter")
        mut_n = config(cfg).getint("algo", "mut_n")
        out_file = config(cfg).get("algo", "out_file")
        runs = config(cfg).getint("algo", "runs")
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
        run = 0
        while run < runs:
            run += 1
            if out_file != sys.stdout and out_file != sys.stderr:
                run_out_file = open(f"{out_file}-{run + 1}.csv", "w")
            else:
                run_out_file = out_file

            pop = gen_pop(pop_size, indiv_l, lb, ub)
            pop = cost_iter(pop)
            pop.sort_values(by=["Cost"], ascending=True, inplace=True)

            # params and first iter
            winner = pop.iloc[0]
            min_j = winner.loc["Cost"]
            avg_j = pop["Cost"].sum() / len(pop)
            iters = 1
            print("%f, %f" % (min_j, avg_j), file=run_out_file)

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
                print("%f, %f" % (min_j, avg_j), file=run_out_file)
            
            if run_out_file != sys.stdout and run_out_file != sys.stderr:
                run_out_file.close()
    return 0
