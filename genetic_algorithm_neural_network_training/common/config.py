# -*- coding: utf-8 -*-

from .args import args
from typing import Optional
import random
import configparser

__config = None

def config(config_src: Optional[str]) -> configparser.ConfigParser:
    """
    Returns the program configuration, or loads the configuration if not loaded
    yet and returns.
    """
    global __config

    if config_src == None and __config != None:
        return __config
    
    __config = configparser.ConfigParser()
    __config.read(config_src)

    __config["DEFAULT"] = {
        "pop_size": 30,
        "sol_lb": -5,
        "sol_ub": 5,
        "sel_perc": 50,
        "mut_perc": 10,
        "mut_n": 1,
        "indiv_l": 33,
        "max_iter": 150,
        "out_file": "sys.stdout",
        "runs": 3,
        "random_seed": 123_123_123,
    }

    if not __config.has_section("algo"):
        __config.add_section("algo")
    
    random.seed(__config.getint("algo", "random_seed"))

    return __config