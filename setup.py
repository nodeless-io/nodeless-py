#!/usr/bin/env python

import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="nodelesspy",
        version="0.0.1",
        description="python nodeless.io sdk",
        author="BitKarrot",
        author_email="me@bitkarrot.co",
        packages=["nodelesspy"],
        install_requires=["aiohttp", "PyYAML"],
    )
