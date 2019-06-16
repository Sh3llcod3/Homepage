#!/usr/bin/env python3
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="memecrypt",
    version="1.3",
    author="Sh3llcod3",
    author_email="no-reply@gmail.co.uk",
    description="An encryption tool, designed for recreational purposes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sh3llcod3/Memecrypt",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Topic :: Security :: Cryptography",
    ),
    install_requires=['easyparse'],
    entry_points={
        'console_scripts': [
            'memecrypt=memecrypt:main',
        ],
    },
    python_requires='>=3',
)
