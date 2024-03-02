from setuptools import setup, find_packages

setup(
    name="libraryX",
    version="0.0.1",
    author="Sorin",
    author_email="samanatis761@gmail.com",
    url="",
    description="universal library for everyone",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    entry_points={"console_scripts": ["libraryX = libraryX.main:download"]},
)