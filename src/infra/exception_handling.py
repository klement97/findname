from functools import partial
from http import HTTPStatus

from fastapi import HTTPException as Hexc

from src.domain.exceptions import PublicationError, PublicationExistsError

unauthorized = partial(Hexc, status_code=HTTPStatus.UNAUTHORIZED)
forbidden = partial(Hexc, status_code=HTTPStatus.FORBIDDEN)
not_found = partial(Hexc, status_code=HTTPStatus.NOT_FOUND)
bad_request = partial(Hexc, status_code=HTTPStatus.BAD_REQUEST)

EXCEPTION_MAP = {
    PublicationError: lambda e: bad_request(detail=str(e)),
    PublicationExistsError: lambda e: bad_request(detail=str(e)),
}
