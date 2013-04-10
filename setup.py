#!/usr/bin/env python

import sys
from setuptools import setup
from get_git_version import get_git_version

install_requires = [
    'pycrypto >=2.6',        # TODO do we need this version
    'gmpy >=1.15, <2',       #      ibidem
        ]

setup(
    name='seccure',
    version=get_git_version(),
    description='SECCURE compatible Elliptic Curve cryptography',
    author='Bas Westerbaan',
    author_email='bas@westerbaan.name',
    url='http://github.com/bwesterb/py-seccure',
    packages=['seccure'],
    package_dir={'seccure': 'src'},
    license='GPL 3.0',
    install_requires=install_requires,
    classifiers = [
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Operating System :: POSIX',
            'Topic :: Security',
        ],
    test_suite='seccure.tests',
    ),
