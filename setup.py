#!/usr/bin/env python
# vim: set fileencoding=utf-8
r"""Pyjig distutils

Copyright(c) 2015, Carroll-Net, Inc., All Rights Reserved"""
from setuptools import setup, find_packages

import os
import sys
sys.path.insert(0, os.path.abspath('src'))
import pyjig.pyjig

try:
    # http://bugs.python.org/issue15881#msg170215
    # pylint: disable=W0611
    import multiprocessing
except ImportError:
    pass

long_description = pyjig.pyjig.__doc__

setup(
    # Project meta-data

    name = 'pyjig',
    version = pyjig.pyjig.__version__,
    packages = ['pyjig'],
    package_dir = {'': 'src'},
    entry_points = {'console_scripts': ['pyjig = pyjig.pyjig:main',],},
    zip_safe = False,

    # Testing (assumes you have nose installed)

    test_suite      = 'nose.collector',
    tests_require   = ['nose>=1.3.4'],

    install_requires  = [
        'markupsafe>=0.23',
        'jinja2>=2.7.3',

        'ruamel.yaml>=0.10.12',
        'cookiecutter>=1.3',

        'sphinx>=1.3.1',
        'pylint>=1.4.4',
        'flake8>=2.4.1',
        'nose>=1.3.4',
        ],

    # Project details

    description = ('Quickly create python projects from templates.'),
    long_description = ''.join(long_description),
    author = 'Jim Carroll',
    author_email = 'jim@carroll.net',
    url = 'https://github.com/jamercee/pyjig',
    download_url = 'https://github.com/jamercee/pyjig',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Software Distribution',
        ],
    license = 'Pyjig is licensed under the 3-clause BSD License',

    platforms = 'any',
    )
