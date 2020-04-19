init:
	pip install -r requirements_dev.txt

test:
	pytest

lint:
	pylint **/*.py

.PHONY: init test
