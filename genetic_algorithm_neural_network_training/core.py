# -*- coding: utf-8 -*-

from .gen_algo import *
from .common import config

def main() -> None:

    pop = gen_pop(
        config().getint("app", "pop_size"),
        config().getint("app", "indiv_l"),
        config().getint("app", "sol_ub"),
        config().getint("app", "sol_lb")
    )
    
    return 0
