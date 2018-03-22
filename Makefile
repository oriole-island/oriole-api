.PHONY: clean clean-test clean-pyc clean-build docs help

test:
	py.test

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

test-all:
	tox

coverage:
	coverage run --source oriole_test -m pytest
	coverage report -m
	coverage html

docs:
	rm -f docs/oriole_test.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ oriole_test
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

servedocs: docs
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: clean
	twine upload dist/*

dist: clean 
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist
