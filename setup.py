#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name="imaplib2",
    version="2.33",
    description="A threaded Python IMAP4 client.",
    author="Piers Lauder",
    url="http://github.com/zain/imaplib2",
    packages=find_packages()
)

