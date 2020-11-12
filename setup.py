#!/usr/bin/python3

import os
import shutil
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

with open('README.md', 'r') as f:
	readme = f.read()

setup(name='xbinfo',
	version='0.1',
	packages=['xbinfo'],
	scripts=['scripts/xbinfo'],
	install_requires=[
		'xbstrap',
		'pydot',
		'pyyaml'
	],

	# Package metadata.
	author='Daniel Chapiesky',
	author_email='dchapiesky2@gmail.com',
	license='MIT',
	url='https://github.com/dchapiesky/xbinfo',
	long_description=readme,
	long_description_content_type='text/markdown'
)

