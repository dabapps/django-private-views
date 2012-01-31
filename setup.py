#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from distutils.core import setup

import privateviews


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    sys.exit()


required = []

setup(
    name='privateviews',
    version=privateviews.__version__,
    long_description=open('README.md').read(),
    author='Julien Phalip',
    url='https://github.com/dabapps/privateviews',
    packages=['privateviews', ],
    install_requires=required,
    license='BSD',
)
