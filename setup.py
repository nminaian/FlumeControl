"""Package description."""

from pathlib import Path

from setuptools import find_packages, setup

long_description = (Path() / "README.md").read_text(encoding="utf-8")

setup(
    name="flumecontrol",
    version="0.1.0",
    description=("Package description."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nminaian/FlumeControl",
    author="Nazanin Minaian",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "fire~=0.4",
        "LabJackPython~=2.0",
        "PyQt5~=5.15",
        "pyqtgraph~=0.12",
        "python_vfd @ git+https://github.com/blakeNaccarato/python-vfd.git",
        "simple-pid~=1.0",
        "uModbus~=1.0",
    ],
    entry_points={
        "console_scripts": ["flumecontrol=flumecontrol.flumecontrol:main"],
    },
)
