import codecs
import io
import os
import re

from setuptools import setup, find_packages

SETUP_DIR = os.path.dirname(os.path.abspath(__file__))


def read(*parts):
    with codecs.open(os.path.join(SETUP_DIR, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def readfile(filename, split=False):
    with io.open(filename, encoding="utf-8") as stream:
        if split:
            return stream.read().split("\n")
        return stream.read()


readme = readfile("README.rst", split=True)[3:]  # Skip title
source_license = readfile("LICENSE")
requires = [
    # minimal requirements listing
    "segmentationstitcher",
    "cmlibs.maths >= 0.6.2",
    "cmlibs.utils >= 0.9.0",
    "cmlibs.zinc >= 4.1",
    "cmlibs.widgets >= 0.7",
    "PySide6"
]


setup(
    name='mapclientplugins.segmentationstitcherstep',
    version=find_version('mapclientplugins', 'segmentationstitcherstep', '__init__.py'),
    description='',
    long_description='\n'.join(readme) + source_license,
    long_description_content_type='text/x-rst',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
    ],
    author='Richard Christie',
    author_email='',
    url='',
    packages=find_packages(exclude=['ez_setup', ]),
    namespace_packages=['mapclientplugins'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)
