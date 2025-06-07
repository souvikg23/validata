
from setuptools import setup, find_packages

setup(
    name='validata',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'schedule',
    ],
    author='Souvik Ghosh',
    description='Validata: A unified data cleaning and validation library with parallelism, scheduling, and AI-assisted type inference.',
    url='https://github.com/YOUR_GITHUB_USERNAME/validata',
)
