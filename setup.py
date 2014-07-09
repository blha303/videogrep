try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    with open('README.md') as readme:
        long_description = readme.read()
except IOError, ImportError:
    long_description =''

'''

Do not use 'djds23' in the final version.
Before pulling this needs to be changed.

'''

setup(name='videogrep',
      version = '0.4',
      description = 'Python utility for creating video out of their subtitle files',
      long_description = long_description,
      download_url = 'https://github.com/djds23/videogrep/archive/master.zip',
      author = 'Sam Lavigne',
      author_email = 'splavigne@gmail.com',
      test_requires = ['pytest==2.5.2'],
      packages = ['videogrep','videogrep.tools','videogrep.tests'],
      scripts = ['videogrep_cli.py'])
