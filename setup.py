from __future__ import unicode_literals

import re

from setuptools import find_packages, setup


def get_version(filename):
    with open(filename) as fh:
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", fh.read()))
        return metadata['version']


setup(
    name='mopidy-irjukebox',
    version=get_version('mopidy_mopidy_irjukebox/__init__.py'),
    url='https://github.com/tdemierr/mopidy-irjukebox',
    license='Apache License, Version 2.0',
    author='Tim',
    author_email='timotheed@gmail.com',
    description='Backend to use IR remote control for external CD jukebox',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 1.0',
        'Pykka >= 1.1',
    ],
    entry_points={
        'mopidy.ext': [
            'mopidy_irjukebox = mopidy_mopidy_irjukebox:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
