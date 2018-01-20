import os
from setuptools import setup
from glob import glob

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "yamljsonmodel",
    version = "0.0.1",
    author = "Tim Potter",
    author_email = "tpot@booleancandy.com.au",
    description = ("Generate JSONModel subclasses from YAML files."),
    license = "Apache-2",
    keywords = "JSONModel YAML",
    url = "http://packages.python.org/yamljsonmodel",
    install_requires = ['jinja2 >= 2.9', 'pyyaml'],
    packages = ['yamljsonmodel', 'tests'],
    scripts = ['scripts/yamljsonmodel'],
    package_data = {
        'yamljsonmodel': ['templates/*/*'],
    },
    long_description = read('README'),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "License :: OSI Approved :: Apache Software License",
    ],
)
