from typing import List

from sqlalchemy import Column, Integer, String, Boolean
from base import Session, engine, Base



class ParkedVehicles(Base):
    __tablename__ = 'ParkedVehicles'
    
    slot = Column(Integer, primary_key=True)
    vehicle_registration_no = Column(String)
    vacant = Column(Boolean, unique=False, default=True)
    driver_age = Column(Integer,  unique=False, default=None)
    
    # Class variables :- 
    __max_slots = 0
    __filled = 0

    # Database session
    __s = Session()

    
    def __init__(self, slot, vehicle_registration_no, vacant=True):
        self.slot = slot
        # should not be repeated since it's pk
        self.vehicle_registration_no = vehicle_registration_no
        self.vacant = vacant


    @staticmethod
    def create_parking_lot(max_slots: str) -> None:
        """[Create records with slot numbers from 1 to max_slots,
            mark all of them as vacant]

        Args:
            max_slots (str): [Max slots alloted for parking space, we later convert to int]
        """
        max_slots = int(max_slots)
        ParkedVehicles.__max_slots = max_slots
        ParkedVehicles.__filled = 0
        
        # Empty DB on a create_parking_lot
        ParkedVehicles.__s.query(ParkedVehicles).delete()

        objects = [ParkedVehicles(slot=ctr, vehicle_registration_no='', vacant=True) for ctr in range(1, max_slots+1)]
        ParkedVehicles.__s.bulk_save_objects(objects)
        ParkedVehicles.__s.commit()
        
        # Create empty records with slot numbers from 1 to max_slots
        print("Created parking of", max_slots, "slots")


    @staticmethod
    def entry(registration_no: str, driver_age: str) -> int:
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
            driver_age (str): [Age of the driver of the car in str]

        Returns:
            int: [Slot number (-1) if slot is not assigned]
        """
        try:
            if ParkedVehicles.__filled == ParkedVehicles.__max_slots:
                # cannot accomodate more cars
                print("Cannot accomodate more vehicles")
                return
            ParkedVehicles.__filled += 1
            
            # get closest vacant slot
            closest_slot_no = ParkedVehicles.__s.query(ParkedVehicles).filter(ParkedVehicles.vacant==True).order_by('slot').first().slot

            # mark slot as filled and update vehicle number
            ParkedVehicles.__s.query(ParkedVehicles).filter(ParkedVehicles.slot==closest_slot_no).update(
                {
                    ParkedVehicles.vacant: False, 
                    ParkedVehicles.vehicle_registration_no: registration_no,
                    ParkedVehicles.driver_age: int(driver_age)
                })
            ParkedVehicles.__s.commit()

            # print slot
            print('Car with vehicle registration number "'+ registration_no +'" has been parked at slot number', closest_slot_no) 
        except Exception as e:
            print("Error while marking entry of car with reg no :- ", registration_no, " driver age:- ", driver_age, " error :- ", str(e))


    @staticmethod
    def leave(slot_no: str) -> str:
        """[When car exits the parking, the input is only the slot number.
        ]

        Args:
            slot_no (str): [slot number while exit, convert it to int later]

        Returns:
            str: [description]
        """
        try:
            # check slot number if not vacant
            parking = ParkedVehicles.__s.query(ParkedVehicles).filter(ParkedVehicles.slot==slot_no).first()
            
            if parking is None:
                print(" Invalid slot number "+ slot_no)
            else:
                # get the vehicle reg. no
                reg_no = parking.vehicle_registration_no
                age = parking.driver_age

                if reg_no is None or age is None:
                    print("No car parked in the slot number "+slot_no)
                else:
                    # mark slot as vacant
                    parking.vacant = True
                    parking.vehicle_registration_no = ''
                    ParkedVehicles.__s.commit()
                    ParkedVehicles.__filled -= 1

                    # print the reg. no if it existed

                    print('Slot number', int(slot_no), 'vacated, the car with vehicle registration number "'+reg_no+'" left the space,')
                    print('the driver of the car was of age', age)
        except Exception as e:
            print("Leave command failed due to :- ", str(e) , " slot no :-", int(slot_no))


    @staticmethod
    def get_slot_no(vehicle_reg_no: str) -> int:
        """[Get slot number of cars which is currently parked ]

        Args:
            vehicle_reg_no (str): [description]

        Returns:
            int: [description]
        """
        try:
            # query the vehicle number if it exists in the system -> currently parked
            parked_vehicle = ParkedVehicles.__s.query(ParkedVehicles).filter(ParkedVehicles.vehicle_registration_no==vehicle_reg_no.strip()).first()
            if parked_vehicle is None:
                print("Vehicle with registration - ", vehicle_reg_no, " is not parked anywhere")
            else:
                slot_no = parked_vehicle.slot
                print(slot_no)

        except Exception as e:
            print("Error while getting slot number of vehicle with registration no - ", vehicle_reg_no, " error - ", str(e))



    @staticmethod
    def get_all_vehicle_nos_of_diver_age(age) -> List:
        """[Get list of vehicle numbers which are currently parked,
          and have driver of age = <age>
          Return None if there isn't any]

        Args:
            age ([type]): [description]
        """
        try:
            all_vehicles = ParkedVehicles.__s.query(ParkedVehicles).filter(ParkedVehicles.driver_age==int(age)).order_by('slot')
            slot_list = [str(each.vehicle_registration_no) for each in all_vehicles]
            str_list = ", ". join(slot_list)
            if str_list == '':
                print("null")
            else:
                print(str_list)
        except Exception as e:
            print("Error in getting all slots of driver error - ", str(e))


    @staticmethod
    def get_all_slots_of_driver_age(age: str) -> None:
        """[Prints list of slot numbers occupied by cars of drivers of given age, 
           null is printed if none are present]

        Args:
            age ([str]): [Driver Age]

        Returns:
            None
        """
        try:
            all_slots = ParkedVehicles.__s.query(ParkedVehicles).filter(ParkedVehicles.driver_age==int(age)).order_by('slot')
            slot_list = [str(each.slot) for each in all_slots]
            str_list = ", ". join(slot_list)
            if str_list == '':
                print("null")
            else:
                print(str_list)
        except Exception as e:
            print("Error in getting all slots of driver error - ", str(e))


