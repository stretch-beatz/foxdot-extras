# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().splitlines()

with open('test-requirements.txt') as requirements_file:
    test_requirements = requirements_file.read().splitlines()

setup(
    name='foxdot_extras',
    version='0.1.0',
    description='Collection of add-ons used for stretch___beatz performances. Hopefully there will comiits to FoxDot repo later.',
    author='Martyn Eggleton @ stretch___beatz',
    author_email='martyn.eggleton@gmail.com',
    url='https://github.com/stretch-beatz/foxdot-extras',
    license='MIT',
    py_modules = ['foxdot_extras'],
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={
        # If any package contains *.txt files, include them:
        "": ["*.yml", "*.hbs"],
    },
    python_requires='>=3.7',
    install_requires=requirements,
    tests_require=requirements + test_requirements,
    test_suite='nose2.collector.collector',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent",
    ],
    keywords=["algorave", "python"],
)
