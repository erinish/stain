.PHONY: build
build:
	rm -rf dist build
	/usr/bin/env python3 setup.py sdist bdist_wheel

clean:
	rm -rf dist build

.PHONY: tests
tests:
	/usr/bin/env python3 tests/test.py

flake8:
	flake8 --ignore=E501,F401 stain

.PHONY: docs
docs:
	cd docs && make html
