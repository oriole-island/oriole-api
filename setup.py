from setuptools import find_packages, setup


install_requires = [
    "pyramid >= 1.9.0",
    "nameko == 2.9.0",
]

setup(
    name='oriole-api',
    version='2.0.0',
    description='Code for oriole-webapi.',
    long_description=open('README.rst').read(),
    author='Eric.Zhou',
    author_email='xiaoxiang.cn@gmail.com',
    url='https://github.com/zhouxiaoxiang/oriole-test',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=True,
    license='Apache License, Version 2.0',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ])
