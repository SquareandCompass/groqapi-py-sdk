from setuptools import setup, find_packages

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "groqapi-client"
VERSION = "0.0.1"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "grpcio" >= 1.42.0
]

setup(
    name=NAME,
    version=VERSION,
    description="Groq API Python",
    author="Groq",
    author_email="",
    url="",
    keywords=["Groq API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    The Groq Python API. Please see https://platform.groq.com/docs/api-reference for more details.
    """,  # noqa: E501
)