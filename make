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

if [ $1 = "data" ]; then
    ./env/bin/activate
    python -m genetic_algorithm_neural_network_training -c data/in/test-0.ini data/in/test-1.ini data/in/test-2.ini data/in/test-3.ini data/in/test-4.ini data/in/test-5.ini data/in/test-6.ini data/in/test-7.ini data/in/test-8.ini data/in/test-9.ini data/in/test-10.ini data/in/test-11.ini data/in/test-12.ini data/in/test-13.ini data/in/test-14.ini data/in/test-15.ini data/in/test-16.ini data/in/test-17.ini data/in/test-18.ini data/in/test-19.ini data/in/test-20.ini data/in/test-21.ini data/in/test-22.ini data/in/test-23.ini
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