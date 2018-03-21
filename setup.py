#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'pip==9.0.2',
    'wheel==0.30.0',
    'watchdog==0.8.3',
    'tox==2.9.1',
    'coverage==4.5.1',
    'Sphinx==1.7.1',
    'twine==1.11.0',
    'pytest==3.4.2',
    'pytest-runner==4.2',
    'pytest-html==1.16.0',
    'bumpversion==0.5.3',
]


setup(
    author="Eric.Zhou",
    author_email='xiaoxiang.cn@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    description="Support tdd for oriole-service.",
    entry_points={
        'console_scripts': [
            'oriole_test=oriole_test.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='oriole-test',
    name='oriole-test',
    packages=find_packages(include=['oriole_test']),
    test_suite='tests',
    url='https://github.com/zhouxiaoxiang/oriole-test',
    version='0.2.1',
    zip_safe=False,
)
