from setuptools import setup, find_packages

## install main application
desc = "utility script for creating data files for statistic based on kmers"

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()
setup(
    name="kmer2stats",
    version='1.0.0',
    description=desc,
    long_description=long_description,
    long_description_content_type = "text/markdown",
    author="Santino Faack",
    author_email="santino_faack@gmx.de",
    license="MIT",
    packages=find_packages(),
    url="https://github.com/SantaMcCloud/kmer2stats",
    scripts=[
        "script/kmer2stats.py"
    ],
)