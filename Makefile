.PHONY: docs

flake8:
	flake8 --ignore=E501,F401 stain

docs:
	cd docs && make html