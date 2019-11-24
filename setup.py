from setuptools import find_packages, setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

tests_require = [
    'pytest<=5.3.0',
    'scikit-learn<=0.21.3',
]


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
    tests_requires=tests_require,
    entry_points = {
        "console_scripts": [
            "monkey = monkey.service.server:main"
        ]
    }
)