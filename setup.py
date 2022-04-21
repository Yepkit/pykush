#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals

from setuptools import setup, find_packages

version = '0.3.5'

setup(
    name='yepkit-pykush',
    version=version,
    description='Yepkit YKUSH Python API and command line tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='ckuesters',
    author_email='ckuesters@yepkit.com',
    license='MIT',
    keywords=['yepkit', 'ykush', 'pykush'],
    url='https://github.com/yepkit/pykush',
    packages=find_packages(),
    install_requires=[
        'hidapi>=0.7.99',
    ],
    entry_points={
        'console_scripts': [
            'pykush=pykush.pykush:main'
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Topic :: Utilities",
        "Topic :: System :: Hardware :: Hardware Drivers",
    ],
)
