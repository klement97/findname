import uuid

from pydantic import BaseModel


class CurrentUser(BaseModel):
    id: uuid.UUID
    email: str
    full_name: str | None = None
    phone: str | None = None
