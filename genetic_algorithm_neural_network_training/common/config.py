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
        "pop_size": 10,
        "co_rate": 80,
        "mut_rate": 20,
        "sel_rate": 20,
        "sol_lb": -3,
        "sol_ub": 3,
        "indiv_l": 33,
        "max_iter": 150,
        "random_seed": 123_123_123,
    }

    if not __config.has_section("app"):
        __config.add_section("app")
    
    random.seed(__config.getint("app", "random_seed"))

    return __config