#!/usr/bin/env python
# vim: set fileencoding=utf-8
r"""Pyjig distutils

Copyright(c) 2015, Carroll-Net, Inc., All Rights Reserved"""
from setuptools import setup, find_packages

import os
import sys
sys.path.insert(0, os.path.abspath('src'))
import pyjig

try:
    # http://bugs.python.org/issue15881#msg170215
    # pylint: disable=W0611
    import multiprocessing
except ImportError:
    pass

long_description = []
try:
    with open('docs/index.rst') as fin:
        for line in fin:
            if line.startswith('Indicies and tables'):
                break
            long_description.append(line)
except IOError:
    pass

setup(
    # Project meta-data

    name = 'pyjig',
    version = '1.0.1',
    packages = ['pyjig'],
    package_dir = {'': 'src'},
    entry_points = {'console_scripts': ['pyjig = pyjig.pyjig:main',],},
    zip_safe = False,

    # Testing (assumes you have nose installed)

    test_suite      = 'nose.collector',
    setup_requires  = ['nose>=1.0'],

    # Project details

    description = (''),
    long_description = ''.join(long_description),
    author = 'Jim Carroll',
    author_email = 'jim@carroll.net',
    #url = 'http://',
    #download_url = 'http://',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        ],
    license = '',
    )
