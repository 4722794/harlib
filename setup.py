#! python

# examplesetup.py - create a file for the package harlib, in the root

# directory of the project

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="harlib",
    version="0.0.1",
    author="Hargun Singh Oberoi",
    author_email="hargun3045@gmail.com",
    description="A personal collection of python functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/4722794/harlib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
