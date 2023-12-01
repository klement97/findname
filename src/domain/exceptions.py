class BaseError(Exception):
    def __init__(self, message):
        self.message = message


class PublicationExistsError(BaseError):
    def __init__(self, publication_id, message="Publication already exists"):
        super().__init__(message)
        self.publication_id = publication_id


class PublicationError(BaseError):
    def __init__(self, publication_id, message="Publication already exists"):
        super().__init__(message)
        self.publication_id = publication_id
