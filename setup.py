# -*- coding: utf-8 -*-

from setuptools import setup, find_namespace_packages

setup(
    name="Playground",
    version="1.0.0",
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    extras_require={
        'dev': [],
        },
    install_requires=[]
    )
