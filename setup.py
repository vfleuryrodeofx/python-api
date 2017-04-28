# -*- coding: utf-8 -*-
import sys
from setuptools import setup, find_packages

f = open('README.md')
readme = f.read().strip()

f = open('LICENSE')
license = f.read().strip()

# For python 2.4 support
script_args = sys.argv[1:]
if (sys.version_info[0] <= 2) or (sys.version_info[0] == 2 and sys.version_info[1] <= 5):
    if 'install' in script_args and '--no-compile' not in script_args:
        script_args.append('--no-compile')

# version of the library was into when the fork was done
shotgun_software_version='3.0.32'
# versionning of the rodeo internal updates
rodeo_version='1.1.0'

setup(
    name='shotgun_api3',
    version='-rdo-'.join([shotgun_software_version, rodeo_version]),
    description='Shotgun Python API: RodeoFX specifications',
    long_description=readme,
    author='Shotgun Software, RodeoFX',
    author_email='shotgundev@rodeofx.com',
    url='https://github.com/rodeofx/python-api',
    license=license,
    packages=find_packages(exclude=('tests',)),
    script_args=script_args,
    include_package_data=True,
    package_data={'': [ 'cacerts.txt']},
    zip_safe=False,
)
