from datetime import datetime

from pydantic import BaseModel


class CarModel(BaseModel):
    id: int | None
    title: str
    brand: str
    model: str
    year: int
    color: str | None
    price: float
    description: str
    created_at: datetime
    updated_at: datetime
