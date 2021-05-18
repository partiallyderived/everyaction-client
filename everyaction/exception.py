"""
This module contains the exceptions used for the EveryAction client
"""

from requests import HTTPError, Response

__all__ = ['EAException', 'EAFindFailedException', 'EAHTTPException']


class EAException(Exception):
    """Class of exceptions raised for EveryAction-related errors which are raised prior to sending HTTP requests.
    HTTP errors are raised as instances of the subclass :class:`.EAHTTPException`.
    """


class EAFindFailedException(EAException):
    """Class of exceptions raised when a function cannot proceed because it expected to find data but failed."""


class EAHTTPException(EAException):
    """Class of exceptions raised if an error response was received for an EveryAction request.

    :ivar Response response: The response with status code >= 400.
    :ivar Sequence[Error] errors: List of EveryAction
        `Error <https://docs.everyaction.com/reference/overview#errors>`__ objects given in the response.
    :ivar HTTPError http_error: The :class:`.HTTPError` associated with the error response.
    """

    def __init__(self, response: Response) -> None:
        from everyaction.core import EAProperty

        try:
            response.raise_for_status()
        except HTTPError as e:
            self.http_error = e
        else:
            raise ValueError(f'{response} is not an error response.')

        self.response = response
        self.errors = EAProperty.shared('errors').value('errors', response.json()['errors'])

        if len(self.errors) == 1:
            error_msg = f'EveryAction error={self.errors[0]}'
        else:
            error_msg = f'EveryAction errors={self.errors}'

        super().__init__(f'{error_msg}, HTTPError={self.http_error}')
