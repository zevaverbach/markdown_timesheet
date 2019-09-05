#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

test_requirements = ["pytest"]

setup(
    author="Zev Averbach",
    author_email="zev@averba.ch",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="A quick way to add up time entries in a markdown document.",
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="markdown timesheet",
    name="markdown_timesheet",
    packages=find_packages(include=["app"]),
    test_suite="tests",
    tests_require=test_requirements,
    entry_points="""
        [console_scripts]
        add=app.cli:cli
    """,
    url="https://github.com/zevaverbach/markdown_timesheet",
    version="0.02",
    zip_safe=False,
)
