from enum import StrEnum


class PublisherType(StrEnum):
    DEALER = "dealer"
    PRIVATE = "private"


class VehicleType(StrEnum):
    CAR = "car"
    MOTORCYCLE = "motorcycle"
    BICYCLE = "bicycle"
    VAN = "van"
    TRUCK = "truck"
    BUS = "bus"
    RECREATIONAL = "recreational"
    BOAT = "boat"


class TransmissionType(StrEnum):
    AUTOMATIC = "automatic"
    MANUAL = "manual"


class DriveType(StrEnum):
    FWD = "fwd"
    RWD = "rwd"
    AWD = "awd"
