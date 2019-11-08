#!/usr/bin/env python2.7
# vim: set fileencoding=utf-8
# pylint:disable=line-too-long
r""":mod:`testpyjig` - unittests for pyjig
##########################################

.. module:: testpyjig
   :synopsis: unittests for pyjig
.. moduleauthor:: JimC <jim@carroll.com>

Comprehensive unittests for the pyjig module.

..
   Copyright(c), 2015, Carroll-Net, Inc., All Rights Reserved."""
# pylint:enable=line-too-long
# ----------------------------------------------------------------------------
# Standard library imports
# ----------------------------------------------------------------------------
import ast
import logging
import os
import re
import shutil
import subprocess
import tempfile
import unittest

from pyjig import pyjig

# ----------------------------------------------------------------------------
# Module level initializations
# ----------------------------------------------------------------------------
__version__    = '1.0.1'
__author__     = 'JimC'
__email__      = 'jim@carroll.com'
__status__     = 'Testing'
__copyright__  = 'Copyright(c) 2015, Carroll-Net, Inc., All Rights Reserved.'

LOG = logging.getLogger('testpyjig')


class Testpyjig(unittest.TestCase):
    r"""pyjig unittest test case"""

    # pylint: disable=invalid-name, global-statement

    def setUp(self):
        r"""create temp dir for overrides"""
        self.tmpd = tempfile.mkdtemp()

    def tearDown(self):
        r"""remove the temp dir"""
        shutil.rmtree(self.tmpd, ignore_errors=True)

    def test_inpath(self):
        r"""test find_inpath()"""
        self.assertIsNotNone(pyjig.inpath('python'))
        self.assertIsNotNone(pyjig.inpath('make'))
        self.assertIsNotNone(pyjig.inpath('git'))

    def test_git_init(self):
        r"""test git_init"""

        with open(os.path.join(self.tmpd, 'file.py'), 'wt') as fout:
            fout.write("print 'hello world'\n")

        pyjig.git_init(self.tmpd)

        gdir = os.path.join(self.tmpd, '.git')
        self.assertTrue(os.path.isdir(gdir))

    def test_app_project(self):
        r"""create application project"""

        parser = pyjig.init_parser()

        cwd = os.getcwd()
        try:
            os.chdir(self.tmpd)

            proj = pyjig.Pyjig(parser.parse_args(['--app', 'myapp']))
            self.assertEqual(proj.ptype, 'app')
            self.assertEqual(proj.project_slug, 'myapp')

            proj.create_project(no_input=True)

            # Directories exist?

            self.assertTrue(os.path.isdir('myapp'))
            self.assertTrue(os.path.isdir('myapp/docs'))
            self.assertTrue(os.path.isdir('myapp/src'))
            self.assertTrue(os.path.isdir('myapp/tests'))

            # Files exist?

            self.assertTrue(os.path.isfile('myapp/.gitignore'))
            self.assertTrue(os.path.isfile('myapp/Makefile'))
            self.assertTrue(os.path.isfile('myapp/id.txt'))
            self.assertTrue(os.path.isfile('myapp/pylint.rc'))
            self.assertTrue(os.path.isfile('myapp/setup.cfg'))
            self.assertTrue(os.path.isfile('myapp/tests/__init__.py'))

            # Verify 'id.txt' is for pkg

            extra = ast.literal_eval(open('myapp/id.txt').read())
            self.assertEqual(extra['project_type'], 'app')

            # Perform static analysis & rebuild docs (empty project)

            os.chdir('myapp')
            subprocess.check_call(['make'])
            subprocess.check_call(['make', 'docs'])
        finally:
            os.chdir(cwd)

    def test_pkg_project(self):
        r"""create package project"""

        parser = pyjig.init_parser()

        cwd = os.getcwd()
        try:
            os.chdir(self.tmpd)

            proj = pyjig.Pyjig(parser.parse_args(['--pkg', 'mypkg']))
            self.assertEqual(proj.ptype, 'pkg')
            self.assertEqual(proj.project_slug, 'mypkg')

            proj.create_project(no_input=True)

            # Directories exist?

            self.assertTrue(os.path.isdir('mypkg'))
            self.assertTrue(os.path.isdir('mypkg/docs'))
            self.assertTrue(os.path.isdir('mypkg/src'))
            self.assertTrue(os.path.isdir('mypkg/tests'))

            # Files exist?

            self.assertTrue(os.path.isfile('mypkg/.gitignore'))
            self.assertTrue(os.path.isfile('mypkg/Makefile'))
            self.assertTrue(os.path.isfile('mypkg/id.txt'))
            self.assertTrue(os.path.isfile('mypkg/pylint.rc'))
            self.assertTrue(os.path.isfile('mypkg/setup.cfg'))
            self.assertTrue(os.path.isfile('mypkg/tests/__init__.py'))

            # Verify 'id.txt' is for pkg

            extra = ast.literal_eval(open('mypkg/id.txt').read())
            self.assertEqual(extra['project_type'], 'pkg')

            # Perform static analysis & rebuild docs (empty project)

            os.chdir('mypkg')
            subprocess.check_call(['make'])
            subprocess.check_call(['make', 'docs'])
        finally:
            os.chdir(cwd)

    def test_add_pysource(self):
        r"""test the simple add_pysource()"""

        cwd = os.getcwd()
        try:
            os.chdir(self.tmpd)
            pyjig.add_pysource('source', self.tmpd, no_input=True)
            self.assertIn('source.py', os.listdir('.'))
        finally:
            os.chdir(cwd)

    def test_add_project_sourcefiles(self):
        r"""test adding source files to existing project."""

        parser = pyjig.init_parser()

        cwd = os.getcwd()
        try:
            os.chdir(self.tmpd)

            # Create project

            proj = pyjig.Pyjig(parser.parse_args(['--app', 'myapp']))
            proj.create_project(no_input=True)

            # Add three(3) source files to project

            os.chdir('myapp')
            proj = pyjig.Pyjig(parser.parse_args(['s1.py', 's2.py', 's3.py']))
            proj.add_project_sourcefile(no_input=True)

            apps = os.listdir('src')
            docs = os.listdir('docs')
            tsts = os.listdir('tests')

            for src in ('s1', 's2', 's3'):
                self.assertIn(src + '.py', apps)
                self.assertIn(src + '.rst', docs)
                self.assertIn('test_' + src + '.py', tsts)

                txt = open('docs/%s.rst' % src).read()
                self.assertIn('.. automodule:: %s' % src, txt)

            # Perform static analysis

            subprocess.check_call(['make'])
            subprocess.check_call(['make', 'docs'])
        finally:
            os.chdir(cwd)

    def test_project_mixedcase(self):
        r"""create project name with mixed case"""

        parser = pyjig.init_parser()

        cwd = os.getcwd()
        try:
            os.chdir(self.tmpd)

            proj = pyjig.Pyjig(parser.parse_args(['--app', 'MyApp']))
            self.assertEqual(proj.ptype, 'app')
            self.assertEqual(proj.project_slug, 'MyApp')

            proj.create_project(no_input=True)

            # Directories exist?

            self.assertTrue(os.path.isdir('MyApp'))

            # Perform static analysis

            os.chdir('MyApp')
            subprocess.check_call(['make'])
        finally:
            os.chdir(cwd)

    def test_add_pyextension(self):
        r"""test the simple add_pyextension()"""

        cwd = os.getcwd()
        try:
            os.chdir(self.tmpd)
            pyjig.add_pyextension('mod', self.tmpd, no_input=True)
            self.assertIn('mod_module.cpp', os.listdir('.'))
        finally:
            os.chdir(cwd)

    def test_add_project_extension(self):
        r"""test adding extension file to existing project."""

        # pylint: disable=too-many-locals

        parser = pyjig.init_parser()

        cwd = os.getcwd()
        try:
            os.chdir(self.tmpd)

            # Create project

            proj = pyjig.Pyjig(parser.parse_args(['--pkg', 'mypkg']))
            proj.create_project(no_input=True)

            # Add three(3) extension files to project

            os.chdir('mypkg')
            proj = pyjig.Pyjig(parser.parse_args(['--ext', 'e1']))
            proj.add_project_extension(no_input=True)

            apps = os.listdir('src')
            docs = os.listdir('docs')
            tsts = os.listdir('tests')

            self.assertIn('e1_module.cpp', apps)
            self.assertIn('e1.rst', docs)
            self.assertIn('test_e1.py', tsts)

            txt = open('docs/e1.rst').read()
            self.assertIn('.. automodule:: e1', txt)

            # Build extension

            setup = open('setup.py').readlines()
            import_added = False
            with open('setup.py', 'wt') as fout:
                for line in setup:
                    fout.write(line)
                    if not import_added and re.match('^from setuptools ', line):
                        fout.write("from setuptools import Extension\n")
                        import_added = True
                    if re.search('package_dir', line):
                        fout.write("ext_modules=[Extension('mypkg.e1',\n"
                                   "sources=['src/e1_module.cpp'])],\n")

            subprocess.check_call(['make', 'build'])

            builtdir = ''
            for dname in os.listdir('build'):
                if dname.startswith('lib.'):
                    builtdir = os.path.join('build', dname, 'mypkg')
                    builtdir = builtdir.replace('\\', '/')
                    break

            # Perform static analysis

            pylint = open('pylint.rc').readlines()
            with open('pylint.rc', 'wt') as fout:
                for line in pylint:
                    ma = re.match(r'^extension-pkg-whitelist=(.+)$', line)
                    if ma:
                        ext = ma.group(1).split(',')
                        ext = ','.join(ext.append('e1'))
                        fout.write("extension-pkg-whitelist=%s\n", ext)
                        continue

                    ma = re.match(r'^init-hook', line)
                    if ma:
                        fout.write("init-hook='import os,sys; "
                                   "sys.path.insert(0, "
                                   "os.path.abspath(\"%s\"))'\n" % builtdir)
                        continue
                    fout.write(line)

            subprocess.check_call(['make', 'tests'])
            subprocess.check_call(['make', 'docs'])
        finally:
            os.chdir(cwd)
