#!/bin/bash

if [ "$#" -eq 0 ] || [ $1 = "init" ]; then
    python -m venv env
    chmod +x env/bin/*
    ./env/bin/activate
    pip install -r requirements.txt
    exit 0
fi

if [ $1 = "dev" ]; then
    ./env/bin/activate
    python -m genetic_algorithm_neural_network_training
    exit 0
fi

if [ $1 = "test" ]; then
    ./env/bin/activate
    python -m tests
    exit 0
fi

if [ $1 = "build" ]; then
    ./env/bin/activate
    python setup.py sdist
    exit 0
fi

echo "Command not recognized"
exit 1