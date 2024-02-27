class _BaseException(Exception):
    def __init__(self, message):
        self.message = message


class PublicationExistsException(_BaseException):
    def __init__(self, publication_id, message="Publication already exists"):
        super().__init__(message)
        self.publication_id = publication_id


class PublicationException(_BaseException):
    def __init__(self, publication_id):
        self.publication_id = publication_id

    def __str__(self):
        return f"Publication with ID: {self.publication_id} already exists."


class UserAlreadyExistsException(_BaseException):
    def __init__(self, message="User already exists!"):
        super().__init__(message)


class IncorrectCredentialsException(_BaseException):
    def __init__(self, message="Email or Password is incorrect!"):
        super().__init__(message)
