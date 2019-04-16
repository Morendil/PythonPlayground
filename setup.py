# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="Playground",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    extras_require={
        'dev': [],
        },
    install_requires=[],
    setup_requires=['setuptools_scm'],
    use_scm_version=True
    )
