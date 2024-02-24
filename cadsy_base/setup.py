from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'PG13 repo'
LONG_DESCRIPTION = 'A package that allows to censor streams of video and camera data.'

# Setting up
setup(
    name="cadsy",
    version=VERSION,
    author="aswin",
    author_email="<aswin@aswin.aswin>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[]
)
