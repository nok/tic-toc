# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


setup(
    name='tic-toc',
    packages=find_packages(exclude=["tests.*", "tests", "examples", "examples.*"]),
    data_files=["readme.md", "license.txt"],
    include_package_data=True,
    version='0.1.0',
    description='Measure and track the wall and CPU time of defined scopes.',
    author='Darius Morawiec',
    author_email='ping@nok.onl',
    url='https://github.com/nok/tic-toc/tree/stable',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[],
    keywords=['time', 'timeit'],
    license='MIT',
)
