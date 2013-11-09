#!/usr/bin/env python

import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='toodlepip',
    version='0.1.0',
    description='Build and test projects using declarative config, such as .travis.yml',
    long_description=read("README"),
    author='Michael Williamson',
    author_email='mike@zwobble.org',
    url='https://github.com/mwilliamson/toodlepip',
    packages=['toodlepip'],
    scripts=['scripts/toodlepip'],
    install_requires=[
        "spur.local>=0.3.7,<0.4",
        "PyYAML>=3.10,<4.0",
    ],
    keywords="build test continuous integration travis",
)
