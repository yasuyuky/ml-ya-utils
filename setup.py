from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ml_ya_utils',
    version='0.1.0',
    description='Yet Another Utilities for Machine Learning',
    long_description=long_description,
    url='https://github.com/yasuyuky/ml-ya-utils',
    author='Yasuyuki YAMADA',
    author_email='yasuyuki.ymd@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='Machine Learning',
    packages=['ml.ya.utils'],
    install_requires=['requests'],
)
