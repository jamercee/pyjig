#!/usr/bin/env python2.7
# vim: set fileencoding=utf-8
# pylint:disable=line-too-long
r""":mod:`pyjig` - Simple description
#######################################

.. module:: pyjig
   :synopsis: Brief 1 line description
.. moduleauthor:: Jim Carroll <jim@carroll.net>

Provide a detailed summary of the module Break down each subsystem and describe
it's operation in detail

Command line options
********************

*usage:* ``pyjig  [-?] [-d] ...``

Positional arguments
====================

.. option:: XXX

   Option XXX provides ...

Optional argument:
==================

.. option:: ?, -h, --help

   Display help and exit

.. option:: -d, --debug

   Generate diagnotic logging.

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
    key/values passed to cookiecutter."""

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
        r"""Add one or more sourcefiles to a project's ~/src/project_slug/
        directory. The project is determined from the current working
        directory. If we are in If we are not in a project folder, then the
        source file will be put in the current directory."""

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
