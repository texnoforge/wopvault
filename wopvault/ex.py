"""
wopvault exceptions

when wopvault CLI run results in exception being raised
its returncode is returned as process return code
"""


class WoPVaultException(Exception):
    returncode = 1
    statuscode = 400


class NotFound(WoPVaultException):
    returncode = 4
    statuscode = 404


class AlphabetNotFound(NotFound):
    pass


class SymbolNotFound(NotFound):
    pass


class TagNotFound(NotFound):
    pass


class InvalidUsage(WoPVaultException):
    returncode = 10


class PayloadTooSmall(WoPVaultException):
    returncode = 12
    statuscode = 418

class PayloadTooLarge(WoPVaultException):
    returncode = 13
    statuscode = 413
