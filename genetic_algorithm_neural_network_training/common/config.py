# -*- coding: utf-8 -*-

from .args import args
import random
import configparser

__config = None

def config() -> configparser.ConfigParser:
    """
    Returns the program configuration, or loads the configuration if not loaded
    yet and returns.
    """
    global __config

    if __config != None:
        return __config
    
    __config = configparser.ConfigParser()
    __config.read(args().get_config_src())

    # TODO document this
    __config["DEFAULT"] = {
        "pop_size": 30,
        "sol_lb": -10,
        "sol_ub": 10,
        "sel_perc": 40,
        "mut_perc": 10,
        "mut_n": 1,
        "indiv_l": 33,
        "max_iter": 150,
        "out_file": "sys.stdout",
        "runs": 1,
        "random_seed": 123_123_123,
    }

    if not __config.has_section("algo"):
        __config.add_section("algo")
    
    random.seed(__config.getint("algo", "random_seed"))

    return __config