# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup


version = "1.0.0a1.dev0"


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="mauritsbobtemplates",
    version=version,
    description="Templates for Maurits for mostly Plone projects.",
    long_description=long_description,
    classifiers=[
        "Environment :: Console",
        "Framework :: Plone",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="web plone zope skeleton project",
    author="Maurits van Rees",
    author_email="maurits@vanrees.org",
    url="https://github.com/maurits/mauritsbobtemplates/",
    license="GPL version 2",
    packages=find_packages(),
    zip_safe=False,
    python_requires=">=3.11",
    install_requires=[
        "setuptools",
        "mr.bob",
        "plonecli",
        "lxml",
        "case-conversion",
        "colorama",
        "tox",
        "isort",
        "black",
    ],
    setup_requires=[],
    tests_require=[],
    extras_require={},
    entry_points={
        "mrbob_templates": [
            "maurits_plone_addon = mauritsbobtemplates.bobregistry:maurits_plone_addon",
            "maurits_plone_buildout = mauritsbobtemplates.bobregistry:maurits_plone_buildout",
        ]
    },
)
