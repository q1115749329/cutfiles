#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/26 14:20
# @Author  : 甄超锋
import setuptools

filepath = "README.md"
setuptools.setup(
    name="cutfiles",
    version="1.0.5",
    author="甄超锋",
    author_email="4535@sohu.com",
    description="Cutting file tool.",
    long_description=open(filepath, encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/q1115749329/cutfiles",
    packages=setuptools.find_packages(),
    data_files=[filepath],
    include_package_data=True,
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)

