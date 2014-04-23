"""
:summary: Exceptions

:license: Creative Commons Attribution-ShareAlike 3.0 Unported
:author: Mark LaPerriere
:contact: rundeckrun@mindmind.com
:copyright: Mark LaPerriere 2013
"""
__docformat__ = "restructuredtext en"

import requests


class InvalidAuthentication(Exception):
    """The method of authentication is not valid"""


class JobNotFound(Exception):
    """The Job could not be found in the Project"""


class MissingProjectArgument(Exception):
    """The requested action requires a Project name to be supplied"""


class InvalidJobArgument(Exception):
    """The Job name or ID is not valid"""


class InvalidResponseFormat(Exception):
    """The requested response format is not supported"""


class InvalidJobDefinitionFormat(Exception):
    """The specified job definition format is not supported"""


class RundeckServerError(Exception):
    """Base exceptions generated by the Rundeck server"""
    def __init__(self, *args, **kwargs):
        self.rundeck_response = kwargs.pop('rundeck_response', None)
        super(RundeckServerError, self).__init__(*args)


class InvalidDupeOption(Exception):
    """The dupeOption specified is invalid"""


class InvalidUuidOption(Exception):
    """The uuidOption specified is invalid"""

class InvalidResourceSpecification(Exception):
    """The resource specified does not meet requirements"""
