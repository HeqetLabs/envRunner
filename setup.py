#!/usr/bin/env python
from setuptools import setup

setup(name='envRunner',
    version='0.2.0',
    description='Run a command with environment variables set from a url or file',
    author='Sean Reed',
    author_email='sean@reed.pub',
    url='https://github.com/HeqetLabs/envRunner',
    install_requires=['docopt', 'requests', 'PyYAML'],
    long_description_markdown_filename='README.md',
    scripts=['envRunner'],
    keywords=['environment', 'runner'],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
