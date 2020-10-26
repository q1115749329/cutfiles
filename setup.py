#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/26 14:20
# @Author  : 甄超锋
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cutfiles",
    version="1.0.1",
    author="甄超锋",
    author_email="4535@sohu.com",
    description="Cutting file tool.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/q1115749329/cutfiles",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)

