#!/usr/bin/env python2.7
# vim: set fileencoding=utf-8
# pylint:disable=line-too-long
r"""Pyjig - Quickly create python projects from templates
#########################################################

:Author: Jim Carroll <jim@carroll.net>
:Description: Quickly create python projects from templates

Pyjig quickly creates new python projects using pre-created templates. Projects
can be simple scripts, distutils packages or full blown applications.  Pyjig
can even add python source modules and c extensions to existing projects.

Pyjig is a wrapper around `Cookiecutter <http://cookiecutter.rtfd.org>`_,
which is a command-line utility that creates projects from ``cookiecutters``
(project templates). Templates are downloaded from public repos (such as
github.com and bitbucket.org). Templates are written in `Jinja
<http://jina.pocoo.org>`_.

Pyjig uses four public repos hosted with github:

+---------------------------------------------------+----------------------------------+
| Repo                                              | Description                      |
+===================================================+==================================+
| https://github.com/jamercee/cookiecutter-pyapp    | Python application type projects |
+---------------------------------------------------+----------------------------------+
| https://github.com/jamercee/cookiecutter-pypkg    | Python package type projects     |
+---------------------------------------------------+----------------------------------+
| https://github.com/jamercee/cookiecutter-pysource | Create python source             |
+---------------------------------------------------+----------------------------------+
| https://github.com/jamercee/cookiecutter-pyext    | Create python extension          |
+---------------------------------------------------+----------------------------------+

****************
Pyjig Background
****************

Project Motivation
==================

Using python requires developers to employ a full ecosystem of tools. At
Carroll-Net, all projects require the following tools; `pylint
<http://www.pylint.org>`_ and `flake8 <https://pypi.python.org/pypi/flake8>`_
for static code analysis, `sphinx <http://sphinx-doc.org>`_ for project
documents and `git <http://git-scm.com>`_ for revision control.  And this
requires setting up directories, config files, a unittest infrastructure and a
comprehensive Makefile for automating the daily build, test and install tasks.

With all these steps, it's easy to miss one, or to make a typo when copying
from another project which then causes developers to spend time debugging.
What was needed was a way to ensure uniform deployment and configuration of our
python architecture and toolchain.

Pyjig Name
==========

Pyjig borrows it's name from the concept of a jig which is a tool used in metal
and woodworking. A jig is a template that allows one to make duplicates of
pieces.  The simplest example is a key duplication machine, which uses one key
as the guide to make copies.

****************
Projects Details
****************

Created Project Layout
======================

Each new project will create the following directories and files::

   myproj               <-- Project root
   |   .gitignore
   |   id.txt
   |   Makefile
   |   pylint.rc
   |   setup.cfg
   |   setup.py
   |
   +---.git             <-- Git repository
   |       ...
   |
   +---docs             <-- Sphinx documentation
   |       conf.py
   |       index.rst
   |       make.bat
   |       Makefile
   |
   +---src              <-- Project source code
   |       __init__.py
   |
   \---tests            <-- Unittest infrastructure
           __init__.py

Each project root folder includes a copy of ``id.txt``. This file is a copy of
the cookiecutter settings that were in effect when the project was created. It
acts as sentinel for project root identification and should not be removed or
renamed.


Makefile generation
===================

Each project will have a cutomized ``Makefile`` installed in the project's
root directory. It's syntax is written to support `GNU Make
<http://gnu.org/software/make>`_. It comes with the following pre-built recipes

+-------------+-----------------------------------------------------------------------+
| Recipe      | Description                                                           |
+=============+=======================================================================+
| comp        | Perform static analysis (default target)                              |
+-------------+-----------------------------------------------------------------------+
| tests       | Run unittests after in-lace build                                     |
+-------------+-----------------------------------------------------------------------+
| docs        | Generate html documentation                                           |
+-------------+-----------------------------------------------------------------------+
| dist        | Build python software distributions                                   |
+-------------+-----------------------------------------------------------------------+
| build       | Build everything needed to install                                    |
+-------------+-----------------------------------------------------------------------+
| install     | Perform static analysis, run unittests and install to site-packages   |
+-------------+-----------------------------------------------------------------------+
| viewdocs    | Rebuild html docs & launch browser                                    |
+-------------+-----------------------------------------------------------------------+
| clean       | Meta-recipe to invoke ``clean-build``, ``clean-pyc``, ``clean-docs``  |
+-------------+-----------------------------------------------------------------------+
| clean-build | Remove all built outputs                                              |
+-------------+-----------------------------------------------------------------------+
| clean-pyc   | Remove python built elements (\*.pyc, \*.pyo, etc...)                 |
+-------------+-----------------------------------------------------------------------+
| debug       | Generate Makefile diagnostic output                                   |
+-------------+-----------------------------------------------------------------------+
| help        | Display Makefile help                                                 |
+-------------+-----------------------------------------------------------------------+

Static Analysis
===============

Python's flexible syntax means that coding errors are difficult to detect until
runtime. Static analysis tries to solve this by scanning code for coding
errors, bugs and bad style. It is an invaluable technique that has saved us
untold hours in debugging.

We first started using `pylint <http://www.pylint.org>`_. Then later on we
added a second static analysis tool `flake8
<https://pypi.python.org/pypi/flake8>`_. Each tool has it's strengths and we've
found the combination of both has provided material reduction in time spent
debugging.

Each of these two tools requires some tweaking before they will generate useful
advice.  Pyjig will handle configuring sane defaults for new projects to get
them up to speed quickly.

To perform static analysis of code, from within the project's root folder run
``make comp``.

.. note::

   The ``Makefile`` recipe detects changes in ``*.py`` with reference to ``*.pyc``.
   If the ``*.pyc`` is missing or older than it's ``*.py``, a static analysis
   pass will be done, and if the pass does not generate errors or warnings, the
   ``*.pyc`` will be re-built.

Code Documentation
==================

Carroll-Net has adopted `Sphinx <http://sphinx-doc.org>`_ as our documentation
generator for python projects. Sphinx converts `reStructuredText
<https://en.wikipedia.org/wiki/ReStructuredText>`_ into HTML websites. Sphinx
can extract documentation from source modules and automatically generate
browesable websites.

There are two Makefile recipes related to documentation; ``make docs`` which
will rebuild documentation and ``make viewdocs`` which will rebuild docs and
launch a webbrowser to read the rebuilt docs.

Two good references for authoring reST documents are

   * https://docs.python.org/devguide/documenting.html
   * https://pythonhosted.org/an_example_pypi_project/sphinx.html

Version Control
===============

Carroll-Net has adopted Git as our version control system for software. Git is
a fast, reliable distributed revision control system. Originally developed for
Linux kernel development it is now the most widely used source code management
tool.

Pyjig will initialize a git repository for each new project it creates using
your local sytem defaults (see `git config ...
<http://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration>`_.). And each
time you use Pyjig to add to an existing project, pyjig will add the source to
the repo.

Pyjig will not create the repo if invoked with ``--excludegit`` or if the
dirctory is a subdirectory of an existing git repository. It detects
repository membership by invoking `git status
<http://git-scm.com/docs/git-status>`_.

***********
Pyjig Usage
***********

Installation
============

Pyjig is hosted on git hub at https://github.com/jamercee/pyjig

Installation using git::

   git clone https://github.com/jamercee/pyjig
   cd pyjig
   python setup.py install

Pyjig can also be installed with pip::

   pip install pyjig

Command line options
====================

*usage:* ``pyjig  [-?] [-d] [--pkg PKG] [--app APP] [--ext EXT [EXT ...]] [-x] [source [source ..]]``

Positional arguments
--------------------

source

   Add one or more source file(s) to project. If the current directry is not part of an
   existing project, the source file will be created, but no project related activities
   will be taken (no unittest generation, no sphix-docs generation, not added to git...)

Optional argument:
------------------

-?, -h, --help        Display help and exit.

-d, --debug           Generate diagnotic output.

--pkg PKG             Create a distutils package project.

--app APP             Create an application type project.

--ext EXT [EXT ...]   Add an extension module(s) to the existing project.

-x, --exludegit       Do not initialize git repo and do not add new source to git repo.


Example Usage
=============

In the examples that follow, the ``--quiet`` flag is used to accept the default
cookiecutter answers (and to keep our example brief).  Some of the default
answers may not be appropriate for your project until you configure
cookiecutter. An example of how todo this is also provided.

New package project with python source files
--------------------------------------------

Typically, the workflow is to create a new project and then to add source files
to it. For example, to create a new package called ``mypkg`` and to the then
add three source files, you would do the following::

   $ pyjig --quiet --pkg mypkg
   $ cd mypkg
   $ pyjig --quiet s1 s2 s3

   $ git status --short
   A  docs/s1.rst
   A  docs/s2.rst
   A  docs/s3.rst
   A  src/s1.py
   A  src/s2.py
   A  src/s3.py
   A  tests/tests1.py
   A  tests/tests2.py
   A  tests/tests3.py

New application project with python source
------------------------------------------

Application projects are similar to package projects with the main difference
being how the ``setup.py`` is created. Application projects use the setuptools
``entry_points`` attribute to cause the install to create a python command
script::

   $ pyjig --quiet --app myapp
   $ cd myapp
   $ pyjig --quiet mycmd

   $ git status --short
   A  docs/mycmd.rst
   A  src/mycmd.py
   A  tests/testmycmd.py

Create a single python source file
----------------------------------

If you only need to create a python source file without the application or
package ecosystem, you can just use the source command. A simple example::

   $ pyjig -q source

This will create a single ``source.py`` in your current directory.


New project with C++ extension
------------------------------

C++ Extensions enable developers to extend the Python interpreter with new
modules. Pyjig comes with support for creating new projects with these
extensions. To create a new C++ Extension you would typically do::

   $ pyjig --quiet --pkg mymod
   $ cd mymod
   $ pyjig --quiet --ext e1

   $ git status --short
   A  docs/e1.rst
   A  src/e1_module.cpp
   A  tests/teste1.py

Pyjig will not add the new module to the ``setup.py`` file. This is an
important step that needs to be done by the developer to cause the
module to be rebuilt. The instructions for how todo this are included as a
comment at the top of the newly created module file::

   $ head -n 15 src/e1_module.cpp
   /*
   This module needs to be manually added to your setup.py. Consider
   adding the following lines:

       from setuptools import Extension

       module = Extension('mymod.e1',
                   sources = ['src/e1_module.cpp'],
                   )

       setup(...
           ext_modules = [ module ],
           )
   */

Defining New Types with C++ Extension
-------------------------------------

Extensions can be used to create new types that can be manipulated from Python
code, much like strings and lists in core Python. The pyjig C++ Extension
system has specialized sections that can be included to create these types. You
cannot create these modules using ``--quiet`` as it requies the developer to
specify the name of the new type during the cookicutter build step. Here's an
example::

   $ pyjig --quiet --pkg mytype
   $ cd mytype
   $ pyjig --ext mytype
   >>> Option: Add extension module 'mytype'.
   You've cloned C:\cygwin64\home\jimc\.cookiecutters\cookiecutter-pyext before.
   Is it okay to delete and re-clone it? [yes]:
   Cloning into 'cookiecutter-pyext'...
   remote: Counting objects: 29, done.
   remote: Compressing objects: 100% (21/21), done.
   remote: Total 29 (delta 13), reused 24 (delta 8), pack-reused 0
   Unpacking objects: 100% (29/29), done.
   Checking connectivity... done.
   module [mytype]:
   module_short_description [short module description]:
   project [mytype]:
   new_type []: Mytype         <--- Give your new type a name here
   version [1.0]:
   release [1.0.1]:
   python [python2.7]:
   author [Jim Carroll]:
   email [jim@carroll.net]:
   year [2015]:
   copyright [Copyright(c) 2015, Carroll-Net, Inc., All Rights Reserved]:

In the example above, the fifth question allows the developer to give their new
type a name. Any non-default answer will cause additional code to be included
in the project to create new custom types.

.. note::
   Remember to add the new module to ``setup.py``


Override cookiecutter defaults
------------------------------

Cookiecutter projects are bundled with a collection of key/value pairs delivered
in a JSON file. You can override the defaults by creating your own
``~/.cookiecutterrc`` file.

.. note::
   To see where you should create your ``.cookiecutterrc`` file, execue the command
   ``python -c "import os; print os.path.expanduser('~/.cookiecutterrc')"``

Each pyjig project has a collection of common key/value settings. Add these
settings to your ``.cookiecutterrc`` file to create overrides::

   default_context:
       author: "Bob Jones"
       email: "bob@jones.com"
       copyright: "Copyright(c) {{cookiecutter.year}}, Jones, Inc., All Rights Reserved"

..
   Copyright(c), 2015, Carroll-Net, Inc., All Rights Reserved."""
# pylint:enable=line-too-long
# ----------------------------------------------------------------------------
# Standard library imports
# ----------------------------------------------------------------------------
from cookiecutter.main import cookiecutter
import argparse
import ast
import datetime
import logging
import os
import shutil
import subprocess
import sys
import tempfile

# ----------------------------------------------------------------------------
# Module level initializations
# ----------------------------------------------------------------------------
__version__    = '1.0.14'
__author__     = 'Jim Carroll'
__email__      = 'jim@carroll.net'
__copyright__  = 'Copyright(c) 2015, Carroll-Net, Inc, All Rights Reserved.'

LOG = logging.getLogger('pyjig')

# Convenience handle to open instance of null device, used to
# discard stdout

DNULL = open(os.devnull, 'wb')


# pylint: disable=too-many-branches

def init_parser():
    r"""Initialize and return :py:class:ArgumentParser.

    .. note::
       This function exists seperate from main() to allow for unittesting."""

    parser = argparse.ArgumentParser(
        add_help=False,
        description='Template driven new project creation.')

    parser.add_argument(
        '-?', '-h', '--help', dest='help',
        action='store_true', default=False,
        help='Show this help message and exit')
    parser.add_argument(
        '-d', '--debug',
        action='store_true', default=False,
        help='Generate diagnostic ouput.')
    parser.add_argument(
        '--pkg',
        nargs=1,
        help='Create a package type project')
    parser.add_argument(
        '--app',
        nargs=1,
        help='Create an application type project')
    parser.add_argument(
        '--ext',
        nargs='+',
        help='Add extension module(s) to existing project')
    parser.add_argument(
        '-x', '--excludegit',
        action='store_true', default=False,
        help='Do not initialize a git repository.')
    parser.add_argument(
        '-q', '--quiet',
        action='store_true', default=False,
        help='Quiet, do not prompt, accept defaults.')
    parser.add_argument(
        'source',
        nargs='*',
        help='Add source file(s) to project')

    return parser


def inpath(exe):
    r"""Search path for executable *exe* and return fully qualified pathname of
    first matching executable or None of no match was found."""

    sep = ':'

    if os.name == 'nt':
        exe = exe + '.exe' if not exe.endswith('.exe') else exe
        sep = ';'

    for pth in os.environ['PATH'].split(sep):
        fname = os.path.join(pth, exe)
        if os.path.isfile(fname):
            return fname

    return None


def git_init(sdir):
    r"""Initialize git repository in directory *sdir*"""

    cwd = os.getcwd()
    try:
        run = subprocess.check_call

        os.chdir(sdir)
        try:
            run(['git', 'status'], stderr=DNULL)
            LOG.info('>>> Git already initialized, step skipped.')
            return
        except subprocess.CalledProcessError:
            pass

        run(['git', 'init'], stdout=DNULL)
        run(['git', 'add', '.'], stdout=DNULL)
        run(['git', 'commit', '-m', 'Initial check in.'], stdout=DNULL)
    finally:
        os.chdir(cwd)


def find_project_root():
    r"""Find the project's root folder by scanning up from the current working
    directory for the ``id.txt`` file. Returns the directory of the project's
    root, or None if not match was found."""

    idpth = os.path.join(os.getcwd(), 'id.txt')

    while not os.path.isfile(idpth):

        curdir = os.path.dirname(idpth)
        parent = os.path.dirname(curdir)

        # Reached top of filesystem?

        if curdir == parent:
            return None

        idpth = os.path.join(parent, 'id.txt')

    return os.path.dirname(idpth)


def add_pyextension(module, tgtdir, no_input=False, extra=None):
    r"""Add new extension *module* to *tgtdir*. If *no_input* is ``True``, user
    will be prompted to answer questions. *extra* is a dictionary of optional
    key/values passed to cookiecutter as default overrides. If the key
    'project_type' exists in extra, then any ``*.rst`` files will be installed
    in ``tgtdir/../docs`` and any ``test*.py`` will be installed in
    ``tgtdir/../tests``."""

    extra = extra or {}

    module = os.path.splitext(module)[0]

    extra['module'] = module
    extra['year'] = datetime.date.today().year

    cwd = os.getcwd()
    tmpd = tempfile.mkdtemp()
    try:
        os.chdir(tmpd)
        cookiecutter('gh:jamercee/cookiecutter-pyext',
                     extra_context=extra, no_input=no_input)

        # Look for C++ first, then fallback to .C

        src = os.path.join(module, module + '_module.cpp')
        tgt = os.path.join(tgtdir, module + '_module.cpp')
        if not os.path.exists(src):
            src = os.path.join(module, module + '.c')
            tgt = os.path.join(tgtdir, module + '.c')

        if os.path.exists(tgt):
            LOG.info(">>> Skipped overwritting target %s", tgt)
            return

        LOG.debug("copy %s -> %s", src, tgt)
        shutil.copyfile(src, tgt)

        # Is this a project?

        if 'project_type' in extra:
            # Copy doc *.rst
            docdir = os.path.abspath(os.path.join(tgtdir, '../docs'))
            if os.path.isdir(docdir):
                src = os.path.join(module, module + '.rst')
                tgt = os.path.join(docdir, module + '.rst')
                if os.path.isfile(src) and not os.path.exists(tgt):
                    LOG.debug("copy %s -> %s", src, tgt)
                    shutil.copyfile(src, tgt)
            # Copy unittest
            tstdir = os.path.abspath(os.path.join(tgtdir, '../tests'))
            if os.path.isdir(tstdir):
                src = os.path.join(module, 'test_' + module + '.py')
                tgt = os.path.join(tstdir, 'test_' + module + '.py')
                if os.path.isfile(src) and not os.path.exists(tgt):
                    LOG.debug("copy %s -> %s", src, tgt)
                    shutil.copyfile(src, tgt)

    finally:
        os.chdir(cwd)
        shutil.rmtree(tmpd, ignore_errors=True)


def add_pysource(module, tgtdir, no_input=False, extra=None):
    r"""Add new source *module* to *tgtdir*. If *no_input* is ``True``, user
    will be prompted to answer questions. *extra* is a dictionary of optional
    key/values passed to cookiecutter as default overrides. If the key
    'project_type' exists in extra, then any ``*.rst`` files will be installed
    in ``tgtdir/../docs`` and any ``test*.py`` will be installed in
    ``tgtdir/../tests``."""

    extra = extra or {}

    module = os.path.splitext(module)[0]
    extra['module'] = module
    extra['year'] = datetime.date.today().year

    cwd = os.getcwd()
    tmpd = tempfile.mkdtemp()
    try:
        os.chdir(tmpd)
        cookiecutter('gh:jamercee/cookiecutter-pysource',
                     extra_context=extra, no_input=no_input)
        src = os.path.join(module, module + '.py')
        tgt = os.path.join(tgtdir, module + '.py')

        if os.path.exists(tgt):
            LOG.info(">>> Skipped overwritting target %s", tgt)
            return

        LOG.debug("copy %s -> %s", src, tgt)
        shutil.copyfile(src, tgt)

        # Is this a project?

        if 'project_type' in extra:
            LOG.debug("Recognized as a project_type")
            # Copy doc *.rst
            docdir = os.path.abspath(os.path.join(tgtdir, '../docs'))
            if os.path.isdir(docdir):
                src = os.path.join(module, module + '.rst')
                tgt = os.path.join(docdir, module + '.rst')
                if os.path.isfile(src) and not os.path.exists(tgt):
                    LOG.debug("copy %s -> %s", src, tgt)
                    shutil.copyfile(src, tgt)
            # Copy unittest
            tstdir = os.path.abspath(os.path.join(tgtdir, '../tests'))
            if os.path.isdir(tstdir):
                src = os.path.join(module, 'test_' + module + '.py')
                tgt = os.path.join(tstdir, 'test_' + module + '.py')
                if os.path.isfile(src) and not os.path.exists(tgt):
                    LOG.debug("copy %s -> %s", src, tgt)
                    shutil.copyfile(src, tgt)
    finally:
        os.chdir(cwd)
        shutil.rmtree(tmpd, ignore_errors=True)


class Pyjig(object):
    r"""Template driven project creation."""

    def __init__(self, args):
        self.args = args
        self.ptype = None
        self.project_name = None
        self.project_slug = None

        if self.args.app:
            self.ptype = 'app'
            self.project_name = self.args.app[0]
            self.project_slug = self.project_name.replace(' ', '_')
            self.pdir = os.path.realpath(self.project_slug)
        elif self.args.pkg:
            self.ptype = 'pkg'
            self.project_name = self.args.pkg[0]
            self.project_slug = self.project_name.replace(' ', '_')
            self.pdir = os.path.realpath(self.project_slug)
        else:
            self.pdir = find_project_root()
            if self.pdir:
                idfn = os.path.join(self.pdir, 'id.txt')
                if os.path.isfile(idfn):
                    extra = ast.literal_eval(open(idfn).read())
                    self.ptype = extra['project_type']
                    self.project_name = extra['project_name']
                    self.project_slug = extra['project_slug']
                else:
                    self.pdir = None

    def create_project(self, no_input=False):
        r"""Create a new project of either 'app' or 'pkg' type"""

        no_input = no_input or self.args.quiet

        extra = {
            'project_type': self.ptype,
            'project_name': self.project_name,
            'year': datetime.date.today().year,
            }

        if self.args.app:
            cookiecutter('gh:jamercee/cookiecutter-pyapp',
                         extra_context=extra, no_input=no_input)
        elif self.args.pkg:
            cookiecutter('gh:jamercee/cookiecutter-pypkg',
                         extra_context=extra, no_input=no_input)

        else:
            raise RuntimeError('unknown project type')

        if not self.args.excludegit:
            git_init(self.pdir)

    def add_project_extension(self, no_input=False):
        r"""Add one or more extension modules to a project's ``~/src/``
        directory. The project is determined from the current working
        directory. If we are not in a project folder, then the extension file will
        be put in the current directory."""

        no_input = no_input or self.args.quiet

        if self.pdir:
            idfn = os.path.join(self.pdir, 'id.txt')
            extra = ast.literal_eval(open(idfn).read())
            tgtdir = os.path.join(self.pdir, 'src')
            extra['project'] = self.project_slug
        else:
            extra = {}
            tgtdir = os.getcwd()

        extra['year'] = datetime.date.today().year

        for ext in self.args.ext:
            add_pyextension(ext, tgtdir, no_input, extra)

        if self.pdir:
            subprocess.check_call(['git', 'add', '.'])

    def add_project_sourcefile(self, no_input=False):
        r"""Add one or more sourcefiles to a project's ``~/src/``
        directory. The project is determined from the current working
        directory. If we are not in a project folder, then the source file will
        be put in the current directory."""

        no_input = no_input or self.args.quiet

        if self.pdir:
            idfn = os.path.join(self.pdir, 'id.txt')
            extra = ast.literal_eval(open(idfn).read())
            tgtdir = os.path.join(self.pdir, 'src')
            extra['project'] = self.project_slug
        else:
            extra = {}
            tgtdir = os.getcwd()

        extra['year'] = datetime.date.today().year

        for source in self.args.source:
            add_pysource(source, tgtdir, no_input, extra)

        if self.pdir:
            subprocess.check_call(['git', 'add', '.'])


def main():
    r"""main process driver"""

    logging.basicConfig(level=logging.INFO, format='%(message)s')

    parser = init_parser()
    args = parser.parse_args()

    if args.help:
        parser.print_help()
        return 0

    if args.debug:
        LOG.info('>>> Option: Debug enabled')
        LOG.setLevel(logging.DEBUG)
    if args.excludegit:
        LOG.info('>>> Option: Do not initialize git repo.')
    if args.quiet:
        LOG.info('>>> Options: Quiet, do not prompt, accept defaults.')
    if args.app:
        LOG.info(">>> Option: Create new application'%s'.", args.app[0])
    if args.pkg:
        LOG.info(">>> Option: Create new package '%s'.", args.pkg[0])
    if args.ext:
        LOG.info(">>> Option: Add extension module '%s'.", args.ext[0])
    if args.source:
        LOG.info(">>> Option: Add new sourcefile(s) '%s'.",
                 ','.join(args.source))

    # Validate arguments

    if not any((args.app, args.pkg, args.ext, args.source)):
        LOG.error('>>> Must either create app/mod or add source.')
        parser.print_help()
        return -1
    if args.app and args.pkg:
        LOG.error('>>> Cannot select both --app and --pkg')
        return -1

    # Validate environment

    try:
        for exe in ('cookiecutter', 'flake8', 'git', 'make', 'nosetests',
                    'pylint', 'sphinx-build'):
            if not inpath(exe):
                raise RuntimeError("missing required componet %s" % exe)
    except RuntimeError as exc:
        LOG.error(exc)
        return -1

    proj = Pyjig(args)

    if args.app or args.pkg:
        proj.create_project()

    if args.ext:
        proj.add_project_extension()

    elif args.source:
        proj.add_project_sourcefile()


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print('CTRL-C')
        sys.exit(0)
