# -*- coding: utf-8 -*-

from __future__ import annotations
import argparse

__args = None

class Args:
    """
    Wrapper for passed command-line arguments.
    """

    def __init__(self) -> None:
        self.__config_src = None
        pass

    def set_config_src(self, config_src: str) -> Args:
        self.__config_src = config_src
        return self

    def get_config_src(self) -> str:
        return self.__config_src


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
        action="store",
        nargs=1,
        required=False,
        default="config.ini",
        dest="config_src",
    )

    parsed = parser.parse_args()

    __args = Args() \
        .set_config_src(parsed.config_src)
    return __args
