from setuptools import find_packages, setup

setup(
    name="fuzzy-broccoli-2",
    version="0.1",
    packages=find_packages(include=["scripts", "scripts.*"]),
    include_package_data=True,
    install_requires=[
        "flake8>=7.1.0",
        "mypy>=1.10.0",
        "pygame>=2.5.2",
        "pytest>=8.2.2",
        "tox>=4.15.1",
        "black",
        "isort",
        "pip-tools",
    ],
    entry_points={
        "console_scripts": [
            "main=scripts.main:main",  # Adjust this based on your main module
        ],
    },
)
