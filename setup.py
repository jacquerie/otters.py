# -*- coding: utf-8 -*-

"""Otters are smaller pandas with less features."""

from __future__ import absolute_import, division, print_function

import os

from setuptools import find_packages, setup


g = {}
with open(os.path.join('otters', 'version.py'), 'rt') as f:
    exec(f.read(), g)
    version = g['__version__']

readme = open('README.md').read()
history = open('CHANGES.md').read()

packages = find_packages()

install_requires = []

setup_requires = []

docs_require = []

tests_require = []

extras_require = {
    'docs': docs_require,
    'tests': tests_require,
}

extras_require['all'] = []
for reqs in extras_require.values():
    extras_require['all'].extend(reqs)

setup(
    name='otters',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='',
    license='MIT',
    author='Jacopo Notarstefano',
    author_email='jacopo.notarstefano@gmail.com',
    url='https://github.com/jacquerie/otters.py',
    packages=packages,
    zip_false=False,
    include_package_data=True,
    platforms='any',
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
