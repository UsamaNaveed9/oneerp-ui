from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in oneerp/__init__.py
from oneerp import __version__ as version

setup(
	name="oneerp",
	version=version,
	description="one erp theme setup",
	author="Hammad",
	author_email="hammadazmrauf@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
