

from models import ParkedVehicles
from base import Session, engine, Base

def parse_command(text: str, ParkedVehicles: Base):
    """[summary]

    Args:
        text (str): [description]
    """
    command_list = {
        'create_parking_lot': ParkedVehicles.create_parking_lot,
        'park': ParkedVehicles.entry,
        'slot_numbers_for_driver_of_age': ParkedVehicles.get_all_slots_of_driver_age,
        'slot_number_for_car_with_number': ParkedVehicles.get_slot_no,
        'leave': ParkedVehicles.leave,
        'vehicle_registration_number_for_driver_of_age': ParkedVehicles.get_all_vehicle_nos_of_diver_age
    }
    try:
        text_list = text.split(' ')
        # assuming there is atleast a space separation between the commands and the args
        command = text_list[0]

        arg = None
        for param in text_list[1:]:
            if param:
                arg = param
                break
        if command.lower() not in command_list or not arg:
            raise Exception("Invalid command - ", command, " and Argument - ", arg)

        result = command_list[command.lower()](arg)
        return result


    except Exception as e:
        print("Error while parsing command :- ", str(e))
