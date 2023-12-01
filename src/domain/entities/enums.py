from enum import auto, StrEnum


class PublisherType(StrEnum):
    DEALER = auto()
    PRIVATE = auto()


class VehicleType(StrEnum):
    CAR = auto()
    MOTORCYCLE = auto()
    BICYCLE = auto()
    VAN = auto()
    TRUCK = auto()
    BUS = auto()
    RECREATIONAL = auto()
    BOAT = auto()


class TransmissionType(StrEnum):
    AUTOMATIC = auto()
    MANUAL = auto()


class DriveType(StrEnum):
    FWD = auto()
    RWD = auto()
    AWD = auto()
