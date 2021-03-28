from typing import List
class Parking:
    
    def __init__(self, max_slots: int):
        self.max_slots = n
        self.filled = 0
        # connect to db and initialize

    def entry(self, registration_no: str, driver_age: int) -> int:
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
        if self.filled == self.max_slots:
            # cannot accomodate more cars
            return -1
        self.filled += 1
        # get closest vacant slot

        # mark slot as filled

        # return slot 
        return 4
    
    def exit(self, slot_no: int) -> str:
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

    
    def get_slot_no(self, vehicle_reg_no: str) -> int:
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

    def get_all_vehicle_nos_of_diver_age(self, age) -> List:
        """[Get list of vehicle numbers which are currently parked,
          and have driver of age = <age>
          Return None if there isn't any]

        Args:
            age ([type]): [description]
        """
        pass

    
    def get_all_slots_of_driver_age(self, age) -> List:
        """[Return list of slot numbers occupied by cars of drivers of given age, 
           empty list is returned if none are present]

        Args:
            age ([type]): [description]

        Returns:
            List: [description]
        """
        pass

    