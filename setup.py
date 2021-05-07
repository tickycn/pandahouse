#!/usr/bin/env python

import versioneer
from os.path import exists
from setuptools import setup


setup(name='pandahouse',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Pandas interface for Clickhouse HTTP API',
      url='http://github.com/kszucs/pandahouse',
      maintainer='Krisztian Szucs',
      maintainer_email='szucs.krisztian@gmail.com',
      license='BSD',
      keywords='',
      packages=['pandahouse'],
      tests_require=['pytest'],
      setup_requires=['pytest-runner'],
      install_requires=['pandas', 'requests', 'toolz'],
      long_description=(open('README.rst').read() if exists('README.rst')
                        else ''),
      zip_safe=False)
