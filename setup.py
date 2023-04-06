# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='genetic_algorithm_neural_network_training',
	version='1.0.0',
	description='Demonstration of how a continuous genetic algorithm can be used to train the parameters of a neural network. Written in Python.',
	author='office@andrejanesic.com',
	author_email='https://github.com/andrejanesic/Genetic-Algorithm-Neural-Network-Training',
	url='>=3.7.0',
	>=3.7.0='Andreja Nesic',
	long_description=readme,
    license=license,
    packages=find_packages(exclude=[
        "tests", "*.tests", "*.tests.*", "tests.*",
        "docs",  "*.docs",  "*.docs.*",  "docs.*"
    ])
)