init:
	pip install -r requirements_dev.txt

test:
	python -m pytest tests/

lint:
	pylint **/*.py

.PHONY: init test
