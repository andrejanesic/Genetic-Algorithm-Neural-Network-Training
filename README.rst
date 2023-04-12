Genetic-Algorithm-Neural-Network-Training
=========================================

Demonstration of how a continuous genetic algorithm can be used to train the parameters of a neural network. Written in Python.

Setup & Commands
----------------

With Docker (Recommended)
+++++++++++++++++++++++++

If you have access to Docker, it is recommended to run the program with its provided Dockerfile. Simply run ``./run``, which will build and run the image with the ``data`` command, creating sample data and printing output to ``data/out``.

Make Commands & No-Docker Execution
+++++++++++++++++++++++++++++++++++

Please run ``./make`` (Linux) or ``.\make.bat`` (Windows) to set up the package. This will create a new Python `virtual environment <https://docs.python.org/3/library/venv.html>`__ and install the required dependencies.

The following Make commands are available. Use ``make (command)`` syntax on Linux and ``.\make.bat (command)`` syntax on Windows:

- ``init``: Initializes the package by installing the required repositories.

- ``dev``: Runs the program's main package.

- ``data``: Runs the program's main package with the ``data/in`` configuration(s).

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

Each configuration file represents one "experiment". Configuration files are written as INI files, with one section ("algo"), with the following parameters:

..  code-block:: ini
    :caption: Configuration file template.
    :linenos:

    [algo]
    pop_size = 10 ; Population size
    sol_lb = -10 ; Expected lower limit of the solution
    sol_ub = 10 ; Expected upper limit of the solution
    sel_perc = 50 ; Selection percentage of the population
    mut_perc = 10 ; Percentage of the population to mutate
    mut_n = 1 ; Number of mutations in each mutated individual
    indiv_l = 33 ; Number of genes in individual
    max_iter = 150 ; Maximum iterations
    out_file = test-0 ; Name of the file to output results to, excluding extension
    runs = 3 ; Number of runs for each test
    random_seed = 123123123 ; Random seed


If not specified, the algorithm will use the following configuration:

..  code-block:: ini
    :caption: Default configuration
    :linenos:

    [algo]
    pop_size: 30
    sol_lb: -5
    sol_ub: 5
    sel_perc: 50
    mut_perc: 10
    mut_n: 1
    indiv_l: 33
    max_iter: 150
    out_file: sys.stdout
    runs: 3
    random_seed: 123_123_123

Authors
-------

.. image:: https://andrejanesic.com/git-signature-sm.png
  :width: 359
  :alt: Andreja Nesic