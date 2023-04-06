# -*- coding: utf-8 -*-

from .args import args
import random
import configparser

__config = None

def config() -> configparser.ConfigParser:
    """
    Returns the program configuration, or loads the configuration if not done
    yet and then returns.
    """
    global __config

    if __config != None:
        return __config
    
    __config = configparser.ConfigParser()
    __config.read(args().get_config_src())

    # TODO document this
    __config["DEFAULT"] = {
        "pop_size": 20,
        "mating_rate": 80,
        "mutat_rate": 20,
        "sel_rate": 20,
        "random_seed": random.randint(0, 1_000_000_000),
    }

    if not __config.has_section("app"):
        __config.add_section("app")

    return __config["app"]