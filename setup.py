from setuptools import setup, find_packages

## install main application
desc = "utility script for creating data files for statistic based on kmers"

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

import os
lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = f"{lib_folder}/requirements.txt"
install_requires = []
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

setup(
    name="kmer2stats",
    version='1.0.1',
    install_requires=install_requires,
    description=desc,
    long_description=long_description,
    long_description_content_type = "text/markdown",
    author="Santino Faack",
    author_email="santino_faack@gmx.de",
    license="GPL-3.0",
    packages=find_packages(),
    url="https://github.com/SantaMcCloud/kmer2stats",
    scripts=[
        "script/kmer2stats.py"
    ],
)