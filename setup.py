#!/usr/bin/env python

import re

from setuptools import find_packages, setup

# Get version without importing, which avoids dependency issues
def get_version():
    with open('tweeli/version.py') as version_file:
        return re.search(r"""__version__\s+=\s+(['"])(?P<version>.+?)\1""",
                version_file.read()).group('version')

# Get README.md file
def read_me():
    with open("README.md", "r") as fh:
        return fh.read()

setup(name="tweeli",
      version=get_version(),
      description="You can using Twitter in CLI mode",
      license="MIT",
      author="Mohammad Taheri",
      author_email="admirer135@yahoo.com",
      long_description=read_me(),
      long_description_content_type="text/markdown",
      url="http://github.com/smmtaheri/tweeli",
      packages=find_packages(),
      install_requires=[
          "tweepy>=3.0.0",
      ],
      keywords="twitter CLI library",
      python_requires='>=2.7',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Topic :: Software Development :: Libraries',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
      ],
      )
