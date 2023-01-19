#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.md", "rt") as fh:
    long_description = fh.read()

dependencies = [
    "packaging",
    "pytest",
    "pytest-asyncio",
    "pytimeparse",
]

release_dependencies = [
    "chia-blockchain==1.6.2",
]

dev_dependencies = [
    "anyio",
    "chia-blockchain @ git+https://github.com/Chia-Network/chia-blockchain.git@main",
    "flake8",
    "mypy",
    "types-aiofiles",
    "types-click",
    "types-cryptography",
    "types-pkg_resources",
    "types-pyyaml",
    "types-setuptools",
    "black==21.12b0",
    "isort",
    "pre-commit",
    "pylint",
]

setup(
    name="chia_dev_tools",
    version="1.1.5b1",
    packages=find_packages(exclude=("tests",)),
    author="Quexington",
    entry_points={
        "console_scripts": ["cdv = cdv.cmds.cli:main"],
    },
    package_data={
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clsp", "*.clsp.hex"],
    },
    author_email="m.hauff@chia.net",
    setup_requires=["setuptools_scm"],
    install_requires=dependencies,
    url="https://github.com/Chia-Network",
    license="https://opensource.org/licenses/Apache-2.0",
    description="Chia development commands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Security :: Cryptography",
    ],
    extras_require=dict(
        release=release_dependencies,
        dev=dev_dependencies,
    ),
    project_urls={
        "Bug Reports": "https://github.com/Chia-Network/chia-dev-tools",
        "Source": "https://github.com/Chia-Network/chia-dev-tools",
    },
)
