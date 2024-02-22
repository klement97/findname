class _BaseException(Exception):
    def __init__(self, message):
        self.message = message


class PublicationExistsException(_BaseException):
    def __init__(self, publication_id, message="Publication already exists"):
        super().__init__(message)
        self.publication_id = publication_id


class PublicationException(_BaseException):
    def __init__(self, publication_id, message="Publication already exists"):
        super().__init__(message)
        self.publication_id = publication_id


class UserDoesNotExist(_BaseException):
    def __init__(self, message="User does not exist!"):
        super().__init__(message)


class UserAlreadyExistsException(_BaseException):
    def __init__(self, message="User already exists!"):
        super().__init__(message)


class PasswordIncorrectException(_BaseException):
    def __init__(self, message="Email or Password is incorrect!"):
        super().__init__(message)
