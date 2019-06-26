#!/usr/bin/env python3
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="homepage",
    version="0.1.0",
    author="Sh3llcod3",
    author_email="no-reply@gmail.co.uk",
    description="A simple flask app to download the audio track from almost any internet video.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sh3llcod3/HomePage",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Multimedia :: Sound/Audio",
    ),
    install_requires=['easyparse'],
    entry_points={
        'console_scripts': [
            'homepage=homepage:main',
        ],
    },
    python_requires='>=3.6+',
)
