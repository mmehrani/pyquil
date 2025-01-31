# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ""
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, "README.rst")
if os.path.exists(readme_path):
    with open(readme_path, "rb") as stream:
        readme = stream.read().decode("utf8")

setup(
    long_description=readme,
    name="pyquil",
    version="3.0.1",
    description="A Python library for creating Quantum Instruction Language (Quil) programs.",
    python_requires="==3.*,>=3.7.0",
    project_urls={
        "documentation": "https://pyquil-docs.rigetti.com",
        "repository": "https://github.com/rigetti/pyquil.git",
    },
    author="Rigetti Computing",
    author_email="softapps@rigetti.com",
    license="Apache-2.0",
    keywords="quantum quil programming hybrid",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    packages=[
        "pyquil",
        "pyquil._parser",
        "pyquil.api",
        "pyquil.compatibility",
        "pyquil.compatibility.v2",
        "pyquil.compatibility.v2.api",
        "pyquil.experiment",
        "pyquil.external",
        "pyquil.latex",
        "pyquil.quantum_processor",
        "pyquil.quantum_processor.transformers",
        "pyquil.simulation",
    ],
    package_dir={"": "."},
    package_data={"pyquil": ["*.typed"], "pyquil._parser": ["*.lark", "*.md"], "pyquil.external": ["*.md"]},
    install_requires=[
        'importlib-metadata==3.*,>=3.7.3; python_version < "3.8"',
        "lark==0.*,>=0.11.1",
        "networkx==2.*,>=2.5.0",
        "numpy==1.*,>=1.20.0",
        "qcs-api-client==0.*,>=0.8.0",
        "retry==0.*,>=0.9.2",
        "rpcq==3.*,>=3.6.0",
        "scipy==1.*,>=1.6.1",
    ],
    extras_require={
        "dev": [
            "black==20.*,>=20.8.0.b1",
            "flake8==3.*,>=3.8.1",
            "mypy==0.740",
            "pytest==6.*,>=6.2.2",
            "pytest-cov==2.*,>=2.11.1",
            "pytest-freezegun==0.*,>=0.4.2",
            "pytest-mock==3.*,>=3.6.1",
            "pytest-rerunfailures==9.*,>=9.1.1",
            "pytest-timeout==1.*,>=1.4.2",
            "pytest-xdist==2.*,>=2.2.1",
            "respx==0.*,>=0.15.0",
        ],
        "docs": [
            "nbsphinx==0.*,>=0.8.6",
            "recommonmark==0.*,>=0.7.1",
            "sphinx==4.*,>=4.0.2",
            "sphinx-rtd-theme==0.*,>=0.5.2",
        ],
        "latex": ["ipython==7.*,>=7.21.0"],
    },
)
