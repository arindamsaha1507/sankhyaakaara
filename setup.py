"""Setup file for sankhyaakaara package."""

import pathlib
from setuptools import setup, find_packages

# Read the contents of the README file
current_dir = pathlib.Path(__file__).parent
long_description = (current_dir / "README.md").read_text()
with open(current_dir / "requirements.txt", encoding="utf-8") as f:
    install_requires = f.read().splitlines()


setup(
    name="sankhyaakaara",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    package_data={
        "sankhyaakaara": ["data/*"],  # Include all files in the data directory
    },
    description="A package for Sanskrit numeral processing and sandhi.",
    long_description=long_description,  # Add long description
    long_description_content_type="text/markdown",  # Specify content type
    author="Arindam Saha",
    author_email="arindamsaha1507@gmail.com",
    license="GPL-3.0",
)
