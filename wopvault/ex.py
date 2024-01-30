"""
wopvault exceptions

when wopvault CLI run results in exception being raised
its returncode is returned as process return code
"""


class WoPVaultException(Exception):
    returncode = 1


class InvalidUsage(WoPVaultException):
    returncode = 10
