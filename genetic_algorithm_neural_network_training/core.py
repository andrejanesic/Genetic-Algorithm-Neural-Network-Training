# -*- coding: utf-8 -*-

from .gen_algo import *
from .common import config
import sys
import time


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

        # create population and calculate initial cost
        run = 0
        while run < runs:
            run += 1
            fname = f"{out_file}.run-{run}.csv"
            if out_file != sys.stdout and out_file != sys.stderr:
                try:
                    run_out_file = open(fname, "w")
                    print("Min,Avg", file=run_out_file)
                except:
                    run_out_file = sys.stdout
            else:
                run_out_file = out_file

            pop = gen_pop(pop_size, indiv_l, lb, ub)
            pop = cost_iter(pop)
            pop.sort_values(by=["Cost"], ascending=True, inplace=True)

            # params and first iter
            last_t = time.time()
            winner = pop.iloc[0]
            min_j = winner.loc["Cost"]
            avg_j = pop["Cost"].sum() / len(pop)
            iters = 1
            print(f"Config: {cfg} | Run: {run} | iter: {iters} | ", end="", file=sys.stdout)
            remaining_t = (time.time() - last_t) / 60 * (max_iter - iters) * (runs - run - 1)
            print("Min: %f, Avg: %f | T remaining: %.2fmin" % \
                  (min_j, avg_j, remaining_t), file=sys.stdout)
            last_t = time.time()
            if run_out_file != sys.stdout and run_out_file != sys.stderr:
                print("%f,%f" % (min_j, avg_j), file=run_out_file)

            # evolve until iters used or converged or local minima found
            last_min_j, last_avg_j, identical_iter = min_j, avg_j, 0
            while min_j >= 0 and iters < max_iter and identical_iter < 10:
                pop = evolve(pop, sel_perc, mut_perc, lb, ub, mut_n)
                pop.sort_values(by=["Cost"], ascending=True, inplace=True)
                curr_winner = pop.iloc[0]
                curr_j = curr_winner.loc["Cost"]
                if curr_j < min_j:
                    min_j = curr_j
                    winner = curr_winner
                iters += 1
                avg_j = pop["Cost"].sum() / len(pop)
                print(f"Config: {cfg} | Run: {run} | iter: {iters} | ", end="", file=sys.stdout)
                remaining_t = (time.time() - last_t) / 60 * (max_iter - iters) * (runs - run - 1)
                print("Min: %f, Avg: %f | T remaining: %.2fmin" % \
                    (min_j, avg_j, remaining_t), file=sys.stdout)
                last_t = time.time()
                if run_out_file != sys.stdout and run_out_file != sys.stderr:
                    print("%f,%f" % (min_j, avg_j), file=run_out_file)
                
                if last_min_j == min_j and last_avg_j == avg_j:
                    identical_iter += 1
                else:
                    last_min_j = min_j
                    last_avg_j = avg_j
                    identical_iter = 0
            
            if run_out_file != sys.stdout and run_out_file != sys.stderr:
                run_out_file.close()
                print(f"Wrote results to file: {fname}")
    return 0
