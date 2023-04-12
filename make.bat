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
	:dev
    call .\env\Scripts\activate.bat
	python -m genetic_algorithm_neural_network_training
	goto end
)

if "%1" == "data" (
	:data
    call .\env\Scripts\activate.bat
    python -m genetic_algorithm_neural_network_training -c data/in/test-0.ini data/in/test-1.ini data/in/test-2.ini data/in/test-3.ini data/in/test-4.ini data/in/test-5.ini data/in/test-6.ini data/in/test-7.ini data/in/test-8.ini data/in/test-9.ini data/in/test-10.ini data/in/test-11.ini data/in/test-12.ini data/in/test-13.ini data/in/test-14.ini data/in/test-15.ini data/in/test-16.ini data/in/test-17.ini data/in/test-18.ini data/in/test-19.ini data/in/test-20.ini data/in/test-21.ini data/in/test-22.ini data/in/test-23.ini
	goto end
)

if "%1" == "test" (
	:test
    call .\env\Scripts\activate.bat
	python -m tests
	goto end
)

if "%1" == "build" (
	:build
    call .\env\Scripts\activate.bat
	python setup.py sdist
	goto end
)

:end