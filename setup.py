#!/usr/bin/env python

from setuptools import find_packages, setup


classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'License :: OSI Approved :: BSD License',
    'Environment :: Console',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Operating System :: Unix',
    'Operating System :: POSIX',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows']


description = 'testing'

with open('README.md') as f:
    long_description = f.read()

keywords = 'microbiome database analysis bioinformatics',

setup(name='testing',
      version=1,
      license='BSD',
      description=description,
      long_description=long_description,
      keywords=keywords,
      classifiers=classifiers,
      author="Amnon Amir",
      maintainer="Amnon Amir",
      url='na',
      test_suite='nose.collector',
      packages=find_packages(),
      install_requires=[
          'click >= 6',
          'numpy >= 1.11.0',
          'h5py >= 2.6',
          'pandas >= 0.19',
          'biom-format >= 2.1',
      ],
      extras_require={'test': ["nose", "pep8", "flake8"],
                      'coverage': ["coverage"],
                      'doc': ["Sphinx >= 1.4"]}
      )
