from pathlib import Path

import sys
sys.path.append('.')

import setuptools


__description__ = "PAY by Square decoding"
__author__      = "SKevo"
__copyright__   = "Copyright (c) 2023, Kevin Svitač"
__credits__     = ["SKevo"]
__license__     = "MIT"
__version__     = "v1.0"
__maintainer__  = "SKevo"
__email__       = "kevin@svit.ac"
__status__      = "5 - Production/Stable"


README_PATH = Path(__file__).parent.absolute() / Path('README.md')

try:
    with open(README_PATH, 'r', encoding="UTF-8") as readme:
        __readme__ = readme.read()

except Exception:
    __readme__ = "Failed to read README.md!"

__doc__ = __readme__



setuptools.setup(
    name = 'pbs_decode',
    packages = setuptools.find_packages(exclude=('tests',)),

    long_description=__readme__,
    long_description_content_type='text/markdown',

    version = __version__,
    license = __license__,
    description = __description__,
    keywords = ["pay by square", "decoding", "decompiler", "qr code", "square", "slovak", "sk"],

    author = __author__,
    author_email = __email__,

    url = 'https://github.com/SKevo18/pbs-decode',

    install_requires=[],

    classifiers=[
        f'Development Status :: {__status__}',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
)
