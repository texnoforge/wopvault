import setuptools


__version__ = '0.0.0'

# get version without importing
exec(open('wopvault/__init__.py').read())


setuptools.setup(
    version=__version__)
