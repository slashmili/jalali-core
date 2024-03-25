from distutils.core import setup

import setuptools

setup(
    name='jalali_core',
    version='1.0.0',
    packages=['jalali_core', ],
    license='LGPL',
    platforms='any',
    author='Milad Rastian',
    author_email='eslashmili@gmail.com',
    description=("a Gregorian to Jalali and inverse date convertor"),
    url="https://github.com/slashmili/jalali-core",
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
