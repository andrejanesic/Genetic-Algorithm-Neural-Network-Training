Genetic-Algorithm-Neural-Network-Training
=========================================

Demonstration of how a continuous genetic algorithm can be used to train the parameters of a neural network. Written in Python.

Setup & Commands
----------------

With Docker (Recommended)
+++++++++++++++++++++++++

If you have access to Docker, it is recommended to run the program with its provided Dockerfile. Simply run ``./run [command]``, which will build and run the image. The command can be any of ``dev``, ``test``, ``build``. See the section below on what each command does.

Make Commands & No-Docker Execution
+++++++++++++++++++++++++++++++++++

Please run ``./make`` (Linux) or ``.\make.bat`` (Windows) to set up the package. This will create a new Python `virtual environment <https://docs.python.org/3/library/venv.html>`__ and install the required dependencies.

The following Make commands are available. Use ``make (command)`` syntax on Linux and ``.\make.bat (command)`` syntax on Windows:

- ``init``: Initializes the package by installing the required repositories.

- ``dev``: Runs the program's main package.

- ``test``: Runs the test suite.

- ``build``: Builds the package.

About
-----

Technical
+++++++++

The genetic algorithm is written in Python, whereas the neural network is considered provided, and is written in C. The GA relies on Pandas for easy tabular data operations.

Usage
+++++

The goal of this project is to demonstrate how genetic algorithms (GA)—specifically, a continuous GA—can be used to train the weights of a neural network.

The program receives a set of configuration files. Each configuration file contains parameters which the program uses to evolve the population. With each generation, the program calculates the cost of each individual, and preselects the given portion of the population's top performers.

Arguments & Configuration
+++++++++++++++++++++++++

Each configuration file represents one "experiment". Configuration files are written as INI files, and should contain the following data:

TODO

Authors
-------

.. image:: https://andrejanesic.com/git-signature-sm.png
  :width: 359
  :alt: Andreja Nesic