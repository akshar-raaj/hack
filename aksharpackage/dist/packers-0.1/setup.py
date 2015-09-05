#from distutils.core import setup
from setuptools import setup, find_packages
setup(
  name = 'packers',
  packages = find_packages(),
  version = '0.1',
  description = 'A random lib',
  author = 'Akshar Raaj',
  author_email = 'akshar@agiliq.com',
  url = 'https://github.com/akshar-raaj/mypackage', # use the URL to the github repo
  download_url = 'https://github.com/akshar-raaj/mypackage/tarball/0.1', # I'll explain this in a second
  keywords = ['testing', 'example'], # arbitrary keywords
  classifiers = [],
)