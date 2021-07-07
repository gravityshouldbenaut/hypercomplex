from os import path
from setuptools import setup

version = "0.1.0"

directory = path.abspath(path.dirname(__file__))
with open(path.join(directory, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='hypercomplex',
    version=version,
    author='discretegames',
    author_email='discretizedgames@gmail.com',
    description="TODO",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/discretegames/hypercomplex',
    packages=['hypercomplex'],
    install_requires=['mathdunders'],  # TODO > 0.4.0
    license="MIT",
    keywords=['TODO']
)
