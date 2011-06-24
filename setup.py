# Copyright: 2011 by the XStatic authors, see AUTHORS.txt for details.
# License: MIT license, see LICENSE.txt for details.

"""
XStatic - setup.py

Works with: setuptools
"""

from setuptools import setup, find_packages

# The README.txt file should be written in reST so that PyPI can use
# it to generate your project's PyPI page. 
long_description = open('README.txt').read()


setup(
    name='XStatic',
    version='0.0.1a0',
    description='XStatic base package with minimal support code',
    long_description=long_description,
    classifiers=[],
    keywords=[],
    author='Thomas Waldmann',
    author_email='tw@waldmann-edv.de',
    license='MIT license',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],  # there should never be a dependency!
)

