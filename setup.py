from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements safely
def read_requirements():
    req_file = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if os.path.exists(req_file):
        with open(req_file) as f:
            return [line.strip() for line in f if line.strip()]
    return []

setup(
    name="kmer2stats",
    version="1.0.2",
    author="Santino Faack",
    author_email="santino_faack@gmx.de",
    description="Utility for computing k-mer-based statistics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SantaMcCloud/kmer2stats",
    packages=find_packages(),
    install_requires=read_requirements(),
    license="GPL-3.0",
    entry_points={
        "console_scripts": [
            "kmer2stats=kmer2stats.core:main"
        ]
    },

    python_requires=">=3.8",
    include_package_data=True,
)