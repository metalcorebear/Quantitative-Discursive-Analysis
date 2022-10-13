#!/usr/bin/env python
"""
@author: metalcorebear
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="QDA",
    version="0.0.2",
    author="metalcorebear",
    author_email="mark.mbailey@gmail.com",
    description="A tool for quantitatively measuring the discursive similarity between bodies of text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/metalcorebear/Quantitative-Discursive-Analysis",
    packages=setuptools.find_packages(),
    install_requires=['networkx', 'textblob', 'numpy'],
    py_modules=["QDA"],
    package_data={},
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)