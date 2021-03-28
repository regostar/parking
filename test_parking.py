import pytest

from models import ParkedVehicles
from base import Session, engine, Base
from commands import parse_command

def test_create_parking_lot():
    Base.metadata.create_all(engine)
    ParkedVehicles.create_parking_lot(5)
    assert ParkedVehicles._ParkedVehicles__max_slots == 5
    assert ParkedVehicles._ParkedVehicles__filled == 0

def test_entry():
    ParkedVehicles.create_parking_lot(5)
    reg_no = "PB-01-TG-2341"
    age = "43"
    ParkedVehicles.entry(registration_no=reg_no, driver_age=age)
    s = Session()
    record = s.query(ParkedVehicles).filter(ParkedVehicles.vehicle_registration_no==reg_no, ParkedVehicles.driver_age==age)
    assert record.first()