from dataclasses import dataclass
from typing import Literal, Any
from uuid import UUID


@dataclass
class Info:
    type: Literal["dealer", "private"]
    full_name: str
    phone: str


@dataclass
class VehicleDetails:
    vin: str
    year: int
    make: str
    model: str
    transmission: Literal["automatic", "manual"]
    kms: int
    description: str
    is_modified: bool
    location: str
    engine: str
    body_style: str
    fuel_type: str
    drive_type: Literal["fwd", "rwd", "awd"]
    exterior_color: str
    interior_color: str
    days_on_action: int = 7


@dataclass
class VehiclePublication:
    id: UUID
    info: Info
    vehicle_details: VehicleDetails
    created_at: str
    updated_at: str

    reserve_price: float | None = None
    photos: list[str] | None = None
    comments: dict[str, Any] | None = None
