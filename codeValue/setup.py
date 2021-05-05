import sys

from setuptools import find_packages, setup

if "--with-xunit" in sys.argv:
    sys.argv.remove("--with-xunit")

packages = [
    "pytest",
    "pytest-timeout",
    "pytest-runner",
    "chardet==3.0.4",
    "olefile==0.46",
    "pdfminer.six==20191110",
    "Pillow==6.2.1",
    "pycryptodome==3.9.3",
    "pyzbar==0.1.8",
]

setup(
    name="CodeValue-Cipher-Application",
    version="1.0.0",
    author="CodeValue",
    author_email="",
    packages=find_packages(),
    python_requires=">=3.5",
    include_package_data=True,
    zip_safe=False,
    install_requires=packages + ["wheel", "setuptools==41.0.1"],
    setup_requires=packages,
    tests_require=packages,
)
