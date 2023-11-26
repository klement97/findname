from dataclasses import dataclass
from typing import Any
from uuid import UUID

from src.domain.entities.enums import PublisherType, VehicleType, TransmissionType, DriveType


@dataclass
class Publisher:
    type: PublisherType
    full_name: str
    phone: str


@dataclass
class BaseVehicleDetails:
    price: int
    make: str
    model: str
    description: str
    location: str


@dataclass
class CarDetails(BaseVehicleDetails):
    vin: str
    year: int
    transmission: TransmissionType
    kms: int
    engine: str
    fuel_type: str
    drive_type: DriveType
    exterior_color: str
    interior_color: str


@dataclass
class MotorcycleDetails(BaseVehicleDetails):
    vin: str
    year: int
    transmission: TransmissionType
    kms: int
    engine: str
    color: str


@dataclass
class BicycleDetails(BaseVehicleDetails):
    pass


@dataclass
class VehiclePublication:
    id: UUID
    publisher: Publisher
    type: VehicleType
    details: {
        VehicleType.CAR: CarDetails | None,
        VehicleType.MOTORCYCLE: MotorcycleDetails | None,
        VehicleType.BICYCLE: BicycleDetails | None,
        VehicleType.VAN: CarDetails | None,
        VehicleType.TRUCK: CarDetails | None,
        VehicleType.BUS: CarDetails | None,
        VehicleType.RECREATIONAL: CarDetails | None,
        VehicleType.BOAT: CarDetails | None,
    }
    created_at: str
    updated_at: str

    photos: list[str] | None = None
    comments: dict[str, Any] | None = None
