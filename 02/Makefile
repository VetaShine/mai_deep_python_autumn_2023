all: run_program1 run_program2

run_program1: func_json.py
	python3 func_json.py

run_program2: test_decorator.py
	python3 test_decorator.py

lint:
	pylint func_json.py test_decorator.py decorator.py

coverage:
	coverage run -m unittest test_decorator.py
	coverage report -m

clean:
