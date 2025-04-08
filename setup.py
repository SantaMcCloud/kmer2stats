from setuptools import setup, find_packages

## install main application
desc = "utility script for creating data files for statistic based on kmers"
setup(
    name="kmer2stats",
    version='1.0.0',
    description=desc,
    long_description=desc + "\n See README for more information.",
    author="Santino Faack",
    author_email="santino_faack@gmx.de",
    license="MIT license",
    packages=find_packages(),
    url="https://github.com/SantaMcCloud/kmer2stats",
    scripts=[
        "script/kmer2stats.py"
    ],
)