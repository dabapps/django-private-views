#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from distutils.core import setup
import privateviews

version = privateviews.__version__

if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    print "You probably want to also tag the version now:"
    print "  git tag -a %s -m 'version %s'" % (version, version)
    print "  git push --tags"
    sys.exit()

setup(
    name='django-private-views',
    version=version,
    description='Site-wide login protection',
    author='Julien Phalip',
    url='https://github.com/dabapps/privateviews',
    packages=['privateviews', ],
    install_requires=[],
    license='BSD',
)
