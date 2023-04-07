# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import List
import argparse

__args = None

class Args:
    """
    Wrapper for passed command-line arguments.
    """

    def __init__(self) -> None:
        self.__configs = None
        self.__cost_exe = None
        pass

    def set_configs(self, configs: List[str]) -> Args:
        self.__configs = configs
        return self

    def get_configs(self) -> List[str]:
        return self.__configs

    def set_cost_exe(self, cost_exe: str) -> Args:
        self.__cost_exe = cost_exe
        return self
    
    def get_cost_exe(self) -> str:
        return self.__cost_exe


def args() -> Args:
    """
    Returns the parsed program arguments, or parses the arguments if not done
    done and then returns.
    """
    global __args

    if __args != None:
        return __args

    parser = argparse.ArgumentParser(
        prog="Genetic Algorithm Neural Network Training",
        description="Demonstration of how a continuous genetic algorithm can be used to train the parameters of a neural network. Written in Python.",
    )

    parser.add_argument(
        "-c",
        "--config",
        action="append",
        nargs='+',
        required=False,
        default=["config.ini"],
        dest="configs",
    )
    
    parser.add_argument(
        "-j",
        "--cost",
        action="store",
        nargs=1,
        required=False,
        default="./nn",
        dest="cost_exe",
    )

    parsed = parser.parse_args()

    __args = Args() \
        .set_configs(parsed.configs) \
        .set_cost_exe(parsed.cost_exe)
    return __args
