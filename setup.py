from setuptools import find_packages
from distutils.core import setup

setup(
    name='docker_hub_listener',
    version='0.1',
    packages=find_packages(),
    license='ASL 2.0',
    long_description=open('README.txt').read(),
)
