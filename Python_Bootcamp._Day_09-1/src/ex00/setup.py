from distutils.core import setup, Extension

module1 = Extension('calculator', sources=['calculator.c'])

setup(name='calculator',
      version='1.0',
      description='Calculator module',
      ext_modules=[module1])
