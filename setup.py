from setuptools import setup, find_packages

setup(
    name='flask_rss',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'flask',
        'feedparser',
    ],
)
