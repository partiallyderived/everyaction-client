"""
This module contains the exceptions used for the EveryAction client
"""

from __future__ import annotations

from json.decoder import JSONDecodeError
from typing import List, TYPE_CHECKING

from requests import HTTPError, Response

if TYPE_CHECKING:
    from everyaction.objects import ChangedEntityExportJob, Error

__all__ = ['EAException', 'EAFindFailedException', 'EAHTTPException']


class EAException(Exception):
    """Class of exceptions raised for EveryAction-related errors which are raised prior to sending HTTP requests.
    HTTP errors are raised as instances of the subclass :class:`.EAHTTPException`.
    """


class EAChangedEntityJobFailedException(EAException):
    """Class of exceptions raised when an EveryAction changed entity export job has failed."""

    def __init__(self, job: ChangedEntityExportJob) -> None:
        super().__init__()
        self.job = job


class EAFindFailedException(EAException):
    """Class of exceptions raised when a function cannot proceed because it expected to find data but failed."""


class EAHTTPException(EAException):
    """Class of exceptions raised if an error response was received for an EveryAction request."""

    #: The response with status code >= 400.
    response: Response

    #: List of EveryAction `Error <https://docs.everyaction.com/reference/errors>`__ objects given in the response.
    errors: List[Error]

    #: The `HTTPError https://2.python-requests.org/en/master/api/#requests.HTTPError>` associated with the error
    #: response.
    http_error: HTTPError

    def __init__(self, response: Response) -> None:
        from everyaction.core import EAProperty

        try:
            response.raise_for_status()
        except HTTPError as e:
            self.http_error = e
        else:
            raise ValueError(f'{response} is not an error response.')

        self.response = response
        try:
            self.errors = EAProperty.shared('errors').value('errors', response.json()['errors'])
        except JSONDecodeError:
            self.errors = []

        # str(self.http_error) is usually a nice simple message like:
        # HTTPError=400 Client Error: Bad Request for url: https://api.securevan.com/v4/changedEntityExportJobs
        # These message components will be joined by new lines.
        msg_components = [str(self.http_error)]

        if len(self.errors) == 1:
            msg_components.append(f'Reason: {self.errors[0].text}')
        elif len(self.errors) != 0:
            msg_components.append('Reasons:')
            [msg_components.append(f'* {e.text}') for e in self.errors]

        super().__init__('\n'.join(msg_components))
