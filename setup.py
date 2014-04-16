#!/usr/bin/python

from distutils.core import setup
from distutils.extension import Extension


_gender = Extension('gender._gender', ['gender.i', 'gender.c'],
                    swig_opts=['-modern', '-Wall', '-outdir','gender'])

setup(name='get-gender',
      version='0.1',
      description='''

      ''',
      author='Alexander Weigl',
      author_email='spamling@web.de',
      url='http://github.com/areku/get-gender',
      packages = ['gender'],
      ext_modules = [_gender]
     )
