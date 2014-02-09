#!/usr/bin/env python

import os
from distutils.core import setup
import sys

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


_install_requires = [
    "spur.local>=0.3.7,<0.4",
    "PyYAML>=3.10,<4.0",
    "mayo>=0.2.3,<0.3",
    "tempman>=0.1.2,<0.2",
    "pyxdg>=0.25,<1.0",
]

if sys.version_info[:2] < (2, 7):
    _install_requires.append("argparse==1.2.1")


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
    install_requires=_install_requires,
    keywords="build test continuous integration travis",
)
