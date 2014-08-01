#!/usr/bin/env python

from __future__ import absolute_import, division, print_function

import os
import setuptools

base_dir = os.path.dirname(__file__)

about = {}
with open(os.path.join(base_dir, "yaurtww", "__about__.py")) as f:
    exec(f.read(), about)

with open(os.path.join(base_dir, "README.rst")) as f:
    long_description = f.read()

setuptools.setup(
    name=about["__title__"],
    version=about["__version__"],

    description=about["__summary__"],
    long_description=long_description,
    license=about["__license__"],
    url=about["__uri__"],

    author=about["__author__"],
    author_email=about["__email__"],

    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Games/Entertainment :: First Person Shooters"
    ],

    packages=["yaurtww"],
    install_requires=[
        "grequests==0.2.0",
        "docopt==0.6.1"
    ],
    entry_points={
        "console_scripts": ["yaurtww=yaurtww:main"]
    }
)
