from setuptools import find_packages, setup

import importer


def read_file(path: str):
    with open(path, "r") as file:
        return file.read()


setup_requires = [
    "wheel",
]

setup(
    name="geonode-importer",
    version=importer.__version__,
    url=importer.__url__,
    description=importer.__doc__,
    long_description="A GeoNode 4.1 app that implements a brand new upload/import flow",
    long_description_content_type="text/markdown",
    author=importer.__author__,
    author_email=importer.__email__,
    platforms="any",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django :: 4.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
    ],
    packages=find_packages("src"),
    package_data={"importer": ["templates/*.html", "templates/layers/*.html"]},
    include_package_data=True,
    install_requires=[
        "setuptools>=59",
        "gdal>=3.2.2",
        "pdok-geopackage-validator==0.8.0",
        "geonode-django-dynamic-model==0.4.0",
    ],
)
