from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('HISTORY.rst') as f:
    history = f.read()

requirements = [
    'Click>=6.0',
    'oriole>=7.1.0',
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
    version='0.5.0',
    zip_safe=False,
)
