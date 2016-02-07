#!/usr/bin/env python

from distutils.core import setup



data_files = [('share/pywrapper_config',['pywrapper_config.py','README.md','LICENSE'])]


setup(name='pywrapper_config',
      version='0.3',
      description='Wrapper to ConfigParser',
      author='Ernesto Crespo',
      author_email='ecrespo@gmail.com',
      url='https://github.com/ecrespo/pywrapper-config',
      packages=['pywrapper_config'],
      license = "GPLv3",
      platforms=['i386','AMD64'],
      py_modules = ['pywrapper_config'],
      data_files =data_files,
      requires = ['ConfigParser'],
     )