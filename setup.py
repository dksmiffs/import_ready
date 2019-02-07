"""
Describe the import_ready module distro to the Distutils, per the following:
    https://docs.python.org/3/distutils/setupscript.html
"""
from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='import_ready',
    version='0.7.0',
    description='A simple importable Python package',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/dave.k.smith/import_ready',
    author='Dave Smith',
    author_email='dave.k.smith@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='import package huntsville havoc testpypi travisci pytest codecov codacy',
    packages=find_packages(),
)
