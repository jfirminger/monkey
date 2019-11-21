from setuptools import find_packages, setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = "monkey",
    version = "0.0.1dev",
    author = "animl.io",
    author_email = "josh@animl.io",
    description = ("wrapping and deploying python models"),
    license = "Apache License 2.0",
    packages = find_packages(),
    long_description = read('README.md'),
    install_requires = requirements,
    entry_points = {
        "console_scripts": [
            "monkey = monkey.service.server:main"
        ]
    }
)