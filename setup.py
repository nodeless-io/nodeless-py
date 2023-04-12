#!/usr/bin/env python

import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="nodelessio",
        version="0.0.1",
        description="python nodeless.io sdk",
        author="BitKarrot",
        author_email="me@bitkarrot.co",
        packages=["nodelessio"],
        install_requires=["aiohttp", "PyYAML"],
    )
