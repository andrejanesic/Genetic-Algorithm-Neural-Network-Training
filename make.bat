@ECHO OFF

if "%1" == "" goto init

if "%1" == "init" (
	:init
    python -m venv env
    call .\env\Scripts\activate.bat
	pip install -r requirements.txt
	goto end
)

if "%1" == "dev" (
	:init
    call .\env\Scripts\activate.bat
	python -m genetic_algorithm_neural_network_training
	goto end
)

if "%1" == "test" (
	:init
    call .\env\Scripts\activate.bat
	python -m tests
	goto end
)

if "%1" == "build" (
	:init
    call .\env\Scripts\activate.bat
	python setup.py sdist
	goto end
)

:end