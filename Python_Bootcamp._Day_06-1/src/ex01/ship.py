from enum import Enum
from pydantic import BaseModel, validator, root_validator


class Alignment(str, Enum):
    ALLY = 'ALLY'
    ENEMY = 'ENEMY'


class ShipClass(str, Enum):
    CORVETTE = 'CORVETTE'
    FRIGATE = 'FRIGATE'
    CRUISER = 'CRUISER'
    DESTROYER = 'DESTROYER'
    CARRIER = 'CARRIER'
    DREADNOUGHT = 'DREADNOUGHT'


class Officer(BaseModel):
    first_name: str
    last_name: str
    rank: str


class Ship(BaseModel):
    name: str
    ship_class: ShipClass
    length: float
    crew_size: int
    armed: bool
    alignment: Alignment
    officers: list[Officer]

    @validator('name')
    def validate_name(cls, name, values):
        if name == 'Unknown' and values.get('alignment') == Alignment.ALLY:
            raise ValueError(f"The Ship with name {name} cannot be ally")
        return name

    @validator('armed')
    def validate_armed(cls, armed, values):
        if values.get('ship_class') == ShipClass.CARRIER and armed:
            raise ValueError(f"{values.get('ship_class')} cannot be armed")
        return armed

    @validator('alignment')
    def validate_alignment(cls, alignment, values):
        if values.get('ship_class') in [ShipClass.FRIGATE, ShipClass.DESTROYER] and alignment == Alignment.ENEMY:
            raise ValueError(f"{values.get('ship_class')} cannot be hostile")
        return alignment

    @root_validator
    def validate_ship_class(cls, values):
        length = values.get('length')
        crew_size = values.get('crew_size')
        ship_class = values.get('ship_class')

        if ship_class == ShipClass.CORVETTE:
            min_length = 80
            max_length = 250
            min_crew_size = 4
            max_crew_size = 10
        elif ship_class == ShipClass.FRIGATE:
            min_length = 300
            max_length = 600
            min_crew_size = 10
            max_crew_size = 15
        elif ship_class == ShipClass.CRUISER:
            min_length = 500
            max_length = 1000
            min_crew_size = 15
            max_crew_size = 30
        elif ship_class == ShipClass.DESTROYER:
            min_length = 800
            max_length = 2000
            min_crew_size = 50
            max_crew_size = 80
        elif ship_class == ShipClass.CARRIER:
            min_length = 1000
            max_length = 4000
            min_crew_size = 120
            max_crew_size = 250
        elif ship_class == ShipClass.DREADNOUGHT:
            min_length = 5000
            max_length = 20000
            min_crew_size = 300
            max_crew_size = 500
        else:
            raise ValueError('Invalid ship class')

        if not (min_length <= length <= max_length):
            raise ValueError(f"Invalid length for {ship_class}")
        if not (min_crew_size <= crew_size <= max_crew_size):
            raise ValueError(f"Invalid crew size for {ship_class}")
        return values
