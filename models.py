from typing import List

from sqlalchemy import Column, Integer, String, Boolean
from base import Session, engine, Base



class ParkedVehicles(Base):
    __tablename__ = 'ParkedVehicles'
    
    slot = Column(Integer, primary_key=True)
    vehicle_registration_no = Column(String)
    vacant = Column(Boolean, unique=False, default=True)
    
    # Class variables :- 
    __max_slots = 0
    __filled = 0

    # Database session
    session = Session()

    
    def __init__(self, slot, vehicle_reg_no, vacant=True):
        self.slot = slot
        # should not be repeated since it's pk
        self.vehicle_registration_no = vehicle_reg_no
        self.vacant = vacant


    @staticmethod
    def create_parking_lot(max_slots: int):
        __max_slots = max_slots
        __filled = 0
        
        # Create empty records with slot numbers from 1 to max_slots
        pass


    @staticmethod
    def entry(registration_no: str, driver_age: int) -> int:
        """[When car enters the Parking, 
            we check if a slot is available.
            If available, 
                -> we return the closest vacant slot number
                -> store in db about the 
            If not available, 
                -> we return -1
            ]

        Args:
            registration_no (str): [Vehicle Registration Number]
            driver_age (int): [Age of the driver of the car]

        Returns:
            int: [Slot number (-1) if slot is not assigned]
        """
        # if self.filled == self.max_slots:
        #     # cannot accomodate more cars
        #     return -1
        # self.filled += 1
        # get closest vacant slot

        # mark slot as filled

        # return slot 
        return 4
    
    @staticmethod
    def leave(slot_no: int) -> str:
        """[When car exits the parking, the input is only the slot number.
        ]

        Args:
            slot_no (int): [description]

        Returns:
            str: [description]
        """
        # check slot number if not vacant
        
        # get the vehicle reg. no

        # mark slot as vacant

        # return the reg. no if it existed

        pass

    @staticmethod
    def get_slot_no(vehicle_reg_no: str) -> int:
        """[Get slot number of cars which is currently parked ]

        Args:
            vehicle_reg_no (str): [description]

        Returns:
            int: [description]
        """
        # query the vehicle number if it exists in the system -> currently parked

        # if not return -1

        # if found, return the slot number
        pass

    @staticmethod
    def get_all_vehicle_nos_of_diver_age(age) -> List:
        """[Get list of vehicle numbers which are currently parked,
          and have driver of age = <age>
          Return None if there isn't any]

        Args:
            age ([type]): [description]
        """
        pass

    @staticmethod
    def get_all_slots_of_driver_age(age) -> List:
        """[Return list of slot numbers occupied by cars of drivers of given age, 
           empty list is returned if none are present]

        Args:
            age ([type]): [description]

        Returns:
            List: [description]
        """
        pass

