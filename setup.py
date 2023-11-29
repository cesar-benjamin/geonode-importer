from setuptools import find_packages, setup


def read_file(path: str):
    with open(path, "r") as file:
        return file.read()


NAME = 'dynamic-rest'
DESCRIPTION = 'A GeoNode 4.1 app that implements a brand new upload/import flow'
URL = "https://github.com/cesar-benjamin/geonode-importer"
AUTHOR = "César Benjamin"
VERSION = '1.0.6-alpha0'


setup(
    name="geonode-importer",
    version=VERSION,
    url=URL,
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email='mathereall@gmail.com',
    platforms="any",
    package_dir={"": "src"},
    packages=find_packages("src"),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django :: 4.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
    ],
    package_data={"importer": ["templates/*.html", "templates/layers/*.html"]},
    include_package_data=True,
    install_requires=open('install_requires.txt').readlines(),
)
