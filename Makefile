# ----------------------------------------------------------------------------
# Define system macros
# ----------------------------------------------------------------------------
ifeq ($(OS), Windows_NT)
	OSTYPE := Windows
	PYTHON := C:/Python27/python.exe
	PYLINT := C:/Python27/Scripts/pylint.exe
	FLAKE := C:/Python27/Scripts/flake8.exe
else
	OSTYPE := $(shell uname)
	PYTHON := pthon2.7
	PYLINT := pylint
	FLAKE := flake8
endif

# ----------------------------------------------------------------------------
# Define $(BROWSER) for reading documentation with web browser
# ----------------------------------------------------------------------------
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

# ----------------------------------------------------------------------------
# Rule to compile python *.py -> *.pyc
# ----------------------------------------------------------------------------
%.pyc:	%.py
	@echo Check $<
	@$(PYLINT) -rn --rcfile pylint.rc $<
	@$(FLAKE) $<
	@$(PYTHON) -c 'import py_compile; py_compile.compile("$<")'

# ----------------------------------------------------------------------------

SOURCE := $(wildcard src/pyjig/*.py) $(wildcard tests/*.py)
TGTS := $(patsubst %.py, %.pyc,$(SOURCE))

.PHONY: clean clean-build clean-docs clean-pyc comp debug docs help 

all: comp

help:
	@echo "comp - perform static analysis (default target)"
	@echo "tests - run unittests"
	@echo "docs - generate documentation"
	@echo "dist - build package"
	@echo "install - install package to site-packages"
	@echo "release - publish to pypi"
	@echo "clean - remove all built components"
	@echo "clean-build - remove all built outputs"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "debug - generate Makefile diagnostic output"

comp: $(TGTS)

tests: comp
	@$(PYTHON) setup.py test

docs:
	@$(MAKE) -C docs html
	@$(PYTHON) setup.py --long-description > README.rst

viewdocs: docs
	@$(BROWSER) docs/_build/html/index.html

dist: comp
	@$(PYTHON) setup.py sdist

install:
	@$(PYTHON) setup.py install

release: clean
	@$(PYTHON) setup.py sdist upload

clean: clean-build clean-pyc clean-docs

clean-build:
	-rm -fr build/ dist/ .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

clean-pyc:
	find . -name '*.py[co]' -exec rm -f {} +
	find . -name '*.pln' -exec rm -f {} +
	find . -name '~*' -exec rm -f {} +
	find . -name '__pycache__' -exec -fr {} +

clean-docs:
	$(MAKE) -C docs clean
	
debug:
	@echo OSTYPE:: $(OSTYPE)
	@echo PYTHON:: $(PYTHON)
	@echo PYLINT:: $(PYLINT)
	@echo FLAKE:: $(FLAKE)
	@echo Source files found::
	@echo $(SOURCE)
	@echo Targets to build::
	@echo $(TGTS)

