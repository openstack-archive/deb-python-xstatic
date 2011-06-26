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
    version='0.0.1',
    description='XStatic base package with minimal support code',
    long_description=long_description,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Archiving :: Packaging',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Software Distribution',
        ],
    keywords="static file resource python packages setuptools pypi require",
    author='Thomas Waldmann',
    author_email='tw@waldmann-edv.de',
    url='http:/bitbucket.org/thomaswaldmann/xstatic',
    license='MIT license',
    packages=find_packages(),
    namespace_packages=['xstatic', 'xstatic.pkg', ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],  # there should never be a dependency!
)

