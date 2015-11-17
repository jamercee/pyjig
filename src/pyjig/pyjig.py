#!/usr/bin/env python2.7
# vim: set fileencoding=utf-8
# pylint:disable=line-too-long
r""":mod:`pyjig` - Quickly create python projects from templates
################################################################

.. module:: pyjig
   :synopsis: Quickly create python projects from templates
.. moduleauthor:: Jim Carroll <jim@carroll.net>

Pyjig quickly creates new python projects using pre-created templates. Projects
can be simple scripts, distutils packages or full blown applications.  Pyjig
can even add python source modules to existing projects.

Pyjig is a wrapper around `Cookiecutter <http://cookiecutter.rtfd.org>`_,
which is a command-line utility that creates projects from ``cookiecutters``
(project templates). Templates are downloaded from public repos (such as
github.com and bitbucket.org). Templates are written in `Jinja
<http://jina.pocoo.org>`_.

Pyjig uses three public repos:

+---------------------------------------------------+----------------------------------+
| Repo                                              | Description                      |
+===================================================+==================================+
| https://github.org/jamercee/cookiecutter-pyapp    | Python application type projects |
+---------------------------------------------------+----------------------------------+
| https://github.org/jamercee/cookiecutter-pypkg    | Python package type projects     |
+---------------------------------------------------+----------------------------------+
| https://github.org/jamercee/cookiecutter-pysource | Crete python source file(s)      |
+---------------------------------------------------+----------------------------------+

Project Motivation
------------------

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

Project Layout
--------------

Each new project will create the following directories and files::

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

Each project will have a customized ``Makefile`` installed in the project's
root directory. It's syntax is written to support `GNU Make
<http://gnu.org/software/make>`_. It comes with the following pre-built recipes

+-------------+-----------------------------------------------------------------------+
| Recipe      | Description                                                           |
+=============+=======================================================================+
| comp        | Perform static analysis (default target)                              |
+-------------+-----------------------------------------------------------------------+
| tests       | Run unittests                                                         |
+-------------+-----------------------------------------------------------------------+
| docs        | Generate html documentation                                           |
+-------------+-----------------------------------------------------------------------+
| dist        | Build python package                                                  |
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
---------------

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
------------------

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

Verision Control
----------------

Carroll-Net has adopted `Git <http://git-scm.org>`_ as our version control
system for software. Git is a fast, reliable distributed revision control
system. Originally developed for Linux kernel development it is now the most
widely used source code management tool.

Pyjig will initialize a git repository for each new project it creates using
your local sytem defaults (see `git config ...
<http://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration>`_.). And each
time you use Pyjig to add python source to an existing project, pyjig will add
the source to the repo.

Pyjig will not create the repo is invoked with ``--excludegit`` or of the
dirctory is a subdirectory of an existing git repository. It detects
repository membership by invoking `git status
<http://git-scm.com/docs/git-status>`_.

Pyjig Name
----------

Pyjig borrows it's name from the concept of a jig which is a tool used in metal
and woodworking. A jig is a template that allows one to make duplicates of
pieces.  The simplest example is a key duplication machine, which uses one key
as the guide to make copies.

Command line options
********************

*usage:* ``pyjig  [-?] [-d] [--pkg PKG] [--app APP] [-x] [source [source ..]]``

Positional arguments
====================

.. option:: source

   Add one or more source file(s) to project. If the current directry is not part of an
   existing project, the source file will be created, but no project related activities
   will be taken (no unittest generation, no sphix-docs generation, not added to git...)

Optional argument:
==================

.. option:: ?, -h, --help

   Display help and exit

.. option:: -d, --debug

   Generate diagnotic output.

.. option:: --pkg PKG

   Create a distutils package project.

.. option:: --app APP

   Create an application type project.

.. option:: -x, --excludegit

   Do not initialize git repo and do not add new source to git repo.

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
__version__    = '1.0.1'
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
        '-x', '--excludegit',
        action='store_true', default=False,
        help='Do not initialize a git repository.')
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

    cwd = os.getcwdu()
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

    idpth = os.path.join(os.getcwdu(), 'id.txt')

    while not os.path.isfile(idpth):

        curdir = os.path.dirname(idpth)
        parent = os.path.dirname(curdir)

        # Reached top of filesystem?

        if curdir == parent:
            return None

        idpth = os.path.join(parent, 'id.txt')

    return os.path.dirname(idpth)


def add_pysource(module, tgtdir, no_input=False, extra=None):
    r"""Add new source *module* to *tgtdir*. If *no_input* is ``True``, user
    will be prompted to answer questions. *extra* is a dictionary of optional
    key/values passed to cookiecutter as default overrides. If the key
    'project_type' exists in extra, then any ``*.rst`` files will be installed
    in ``tgtdir/../../docs`` and any ``test*.py`` will be installed in
    ``tgtdir/../../tests``."""

    extra = extra or {}

    if module.endswith('.py'):
        module = module[:-3]
    extra['module'] = module
    extra['year'] = datetime.date.today().year

    cwd = os.getcwdu()
    tmpd = tempfile.mkdtemp()
    try:
        os.chdir(tmpd)
        cookiecutter('gh:jamercee/cookiecutter-pysource',
                     extra_context=extra, no_input=no_input)
        src = os.path.join(module, module + '.py')
        tgt = os.path.join(tgtdir, module + '.py')
        shutil.copyfile(src, tgt)

        # Is this a project?

        if 'project_type' in extra:
            # Copy doc *.rst
            docdir = os.path.abspath(os.path.join(tgtdir, '../../docs'))
            if os.path.isdir(docdir):
                src = os.path.join(module, module + '.rst')
                tgt = os.path.join(docdir, module + '.rst')
                if os.path.isfile(src):
                    shutil.copyfile(src, tgt)
            # Copy unittest
            tstdir = os.path.abspath(os.path.join(tgtdir, '../../tests'))
            if os.path.isdir(tstdir):
                print('tstdir %s EXISTS' % tstdir)
                src = os.path.join(module, 'test' + module + '.py')
                tgt = os.path.join(tstdir, 'test' + module + '.py')
                print('does src %s exist?' % src)
                if os.path.isfile(src):
                    print("YES")
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
            self.project_slug = self.project_name.lower().replace(' ', '_')
            self.pdir = os.path.realpath(self.project_slug)
        elif self.args.pkg:
            self.ptype = 'pkg'
            self.project_name = self.args.pkg[0]
            self.project_slug = self.project_name.lower().replace(' ', '_')
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

    def add_project_sourcefile(self, no_input=False):
        r"""Add one or more sourcefiles to a project's ``~/src/project_slug/``
        directory. The project is determined from the current working
        directory. If we are not in a project folder, then the source file will
        be put in the current directory."""

        if self.pdir:
            idfn = os.path.join(self.pdir, 'id.txt')
            extra = ast.literal_eval(open(idfn).read())
            tgtdir = os.path.join(self.pdir, 'src', extra['project_slug'])
        else:
            extra = {}
            tgtdir = os.getcwdu()

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
    if args.app:
        LOG.info(">>> Option: Create new application'%s'.", args.app[0])
    if args.pkg:
        LOG.info(">>> Option: Create new package '%s'.", args.pkg[0])
    if args.source:
        LOG.info(">>> Option: Add new sourcefile(s) '%s'.",
                 ','.join(args.source))

    # Validate arguments

    if not args.app and not args.pkg and not args.source:
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

    if args.source:
        proj.add_project_sourcefile()


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print('CTRL-C')
        sys.exit(0)
