#!/usr/bin/env python
from setuptools import setup

setup(name='envRunner',
    version='0.1',
    description='Run a command with environment variables set from a url or file',
    author='Sean Reed',
    author_email='sean@reed.pub',
    url='https://github.com/HeqetLabs/envRunner',
    install_requires=['docopt', 'requests', 'PyYAML', 'wsgiref'],
    scripts=['envRunner'],
    keywords=['environment', 'runner'],
)
