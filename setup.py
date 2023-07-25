import os

from setuptools import setup, find_packages

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as fh:
    long_description = '\n' + fh.read()

setup(
    name='pretty-utils',
    version='1.1.12',
    license='Apache-2.0',
    author='SecorD',
    description='Convenient functions in one package',
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy'],
    keywords=['utils'],
    classifiers=[
        'Programming Language :: Python :: 3.8'
    ]
)
