init:
    python -m venv env
    ./env/Scripts/activate
	pip install -r requirements.txt

dev:
    ./env/Scripts/activate
    python -m genetic_algorithm_neural_network_training

test:
    ./env/Scripts/activate
    python -m tests

build:
    ./env/Scripts/activate
    python setup.py sdist