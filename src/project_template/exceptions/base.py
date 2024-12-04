from abc import ABC

from fastapi import HTTPException, status


class Unauthorized(ABC, HTTPException):
    def __init__(self, detail) -> None:
        status_code = status.HTTP_401_UNAUTHORIZED
        super().__init__(status_code, detail)


class NotFound(ABC, HTTPException):
    def __init__(self, detail) -> None:
        status_code = status.HTTP_404_NOT_FOUND
        super().__init__(status_code, detail)


class Conflict(ABC, HTTPException):
    def __init__(self, detail) -> None:
        status_code = status.HTTP_409_CONFLICT
        super().__init__(status_code, detail)