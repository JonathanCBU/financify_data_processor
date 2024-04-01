"""Custom Defined Exceptions"""


class CiError(Exception):
    """Parent Class for CI Exceptions"""


class PlatformException(Exception):
    """Parent Class for Platform Exceptions"""


class InvalidOSException(PlatformException):
    """Raised when operating on an unsupported OS"""


class ParsingException(Exception):
    """Raised when regex parsing fails"""
