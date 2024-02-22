from functools import partial
from http import HTTPStatus

from fastapi import HTTPException as Hexc

from src.domain import exceptions as exc

unauthorized = partial(Hexc, status_code=HTTPStatus.UNAUTHORIZED)
forbidden = partial(Hexc, status_code=HTTPStatus.FORBIDDEN)
not_found = partial(Hexc, status_code=HTTPStatus.NOT_FOUND)
bad_request = partial(Hexc, status_code=HTTPStatus.BAD_REQUEST)

EXCEPTION_MAP = {
    exc.PublicationException: lambda e: bad_request(detail=str(e)),
    exc.PublicationExistsException: lambda e: bad_request(detail=str(e)),
    exc.UserDoesNotExist: lambda e: not_found(detail=str(e)),
    exc.UserAlreadyExistsException: lambda e: bad_request(detail=str(e)),
    exc.PasswordIncorrectException: lambda e: bad_request(detail=str(e))
}
