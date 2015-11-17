pyjig - Quickly create python projects from templates
=====================================================

Pyjig quickly creates new python projects using pre-created templates.
Projects can be simple scripts, distutils packages or full blown
applications. Pyjig can even add python source modules to existing
projects.

Pyjig is a wrapper around [Cookiecutter](http://cookiecutter.rtfd.org),
which is a command-line utility that creates projects from
`cookiecutters` (project templates). Templates are downloaded from
public repos (such as github.com and bitbucket.org). Templates are
written in [Jinja](http://jina.pocoo.org).

Pyjig uses three public repos:

  ------------------------------------------------------------------------
  Repo                                        Description
  ------------------------------------------- ----------------------------
  <https://github.org/jamercee/cookiecutter-p Python application type
  yapp>                                       projects

  <https://github.org/jamercee/cookiecutter-p Python package type projects
  ypkg>                                       

  <https://github.org/jamercee/cookiecutter-p Crete python source file(s)
  ysource>                                    
  ------------------------------------------------------------------------

Project Motivation
------------------

Using python requires developers to employ a full ecosystem of tools. At
Carroll-Net, all projects require the following tools;
[pylint](http://www.pylint.org) and
[flake8](https://pypi.python.org/pypi/flake8) for static code analysis,
[sphinx](http://sphinx-doc.org) for project documents and
[git](http://git-scm.com) for revision control. And this requires
setting up directories, config files, a unittest infrastructure and a
comprehensive Makefile for automating the daily build, test, install
tasks.

With all these steps, it's easy to miss one, or to make a typo when
copying from another project which then caused developers to spend time
debugging. What was needed was a way to ensure uniform deployment and
configuration of our python architecture and toolchain.

Project Layout
--------------

Each new project will create the following directories and files:

    myproj               Project root
    +
    |
    |   .gitignore
    |   id.txt
    |   Makefile
    |   pylint.rc
    |   setup.cfg
    |   setup.py
    |
    +---.git             Git repository
    |       ...
    |
    +---docs             Sphinx documentation
    |       conf.py
    |       index.rst
    |       make.bat
    |       Makefile
    |
    +---src              Project source code
    |   \---myproj
    |           __init__.py
    |
    \---tests            Unittest infrastructure
            __init__.py

Makefile generation
-------------------

Each project will have a customized `Makefile` installed in the
project's root directory. It's syntax is written to support [GNU
Make](http://gnu.org/software/make). It comes with the following
pre-built recipes

  ------------------------------------------------------------------------
  Recipe      Description
  ----------- ------------------------------------------------------------
  comp        Perform static analysis (default target)

  tests       Run unittests

  docs        Generate html documentation

  dist        Build python package

  install     Perform static analysis, run unittests and install to
              site-packages

  viewdocs    Rebuild html docs & launch browser

  clean       Meta-recipe to invoke `clean-build`, `clean-pyc`,
              `clean-docs`

  clean-build Remove all built outputs

  clean-pyc   Remove python built elements (\*.pyc, \*.pyo, etc...)

  debug       Generate Makefile diagnostic output

  help        Display Makefile help
  ------------------------------------------------------------------------

Static Analysis
---------------

Python's flexible syntax means that coding errors are difficult to
detect until runtime. Static analysis tries to solve this by scanning
code for coding errors, bugs and bad style. It is an invaluable
technique that has saved us untold hours in debugging.

We first started using [pylint](http://www.pylint.org). Then later on we
added a second static analysis tool
[flake8](https://pypi.python.org/pypi/flake8). Each tool has it's
strengths and we've found the combination of both has provided material
reduction in time spent debugging.

Each of these two tools requires some tweaking before they will generate
useful advice. Pyjig will handle configuring sane defaults for new
projects to get them up to speed quickly.

To perform static analysis of code, from within the project's root
folder run `make comp`.

> **note**
>
> The `Makefile` recipe detects changes in `*.py` with reference to
> `*.pyc`. If the `*.pyc` is missing or older than it's `*.py`, a static
> analysis pass will be done, and if the pass does not generate errors
> or warnings, the `*.pyc` will be re-built.

Code Documentation
------------------

Carroll-Net has adopted [Sphinx](http://sphinx-doc.org) as our
documentation generator for python projects. Sphinx converts
[reStructuredText](https://en.wikipedia.org/wiki/ReStructuredText) into
HTML websites. Sphinx can extract documentation from source modules and
automatically generate browesable websites.

There are two Makefile recipes related to documentation; `make docs`
which will rebuild documentation and `make viewdocs` which will rebuild
docs and launch a webbrowser to read the rebuilt docs.

Two good references for authoring reST documents are

> -   <https://docs.python.org/devguide/documenting.html>
> -   <https://pythonhosted.org/an_example_pypi_project/sphinx.html>

Verision Control
----------------

Carroll-Net has adopted [Git](http://git-scm.org) as our version control
system for software. Git is a fast, reliable distributed revision
control system. Originally developed for Linux kernel development it is
now the most widely used source code management tool.

Pyjig will initialize a git repository for each new project it creates
using your local sytem defaults (see [git config
...](http://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).).
And each time you use Pyjig to add python source to an existing project,
pyjig will add the source to the repo.

Pyjig will not create the repo is invoked with `--excludegit` or of the
dirctory is a subdirectory of an existing git repository. It detects
repository membership by invoking [git
status](http://git-scm.com/docs/git-status).

Pyjig Name
----------

Pyjig borrows it's name from the concept of a jig which is a tool used
in metal and woodworking. A jig is a template that allows one to make
duplicates of pieces. The simplest example is a key duplication machine,
which uses one key as the guide to make copies.

### Command line options

*usage:*
`pyjig  [-?] [-d] [--pkg PKG] [--app APP] [-x EXCLUDEGIT] [source [source ..]]`

#### Positional arguments

#### Optional argument:
