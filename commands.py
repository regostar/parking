
from typing import List

from models import ParkedVehicles
from base import Session, engine, Base

def parse_command(text: str):
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

        if command.lower() not in command_list:
            raise Exception("Invalid command - ", command)

        # only park command has 2 arguments
        if command.lower() == 'park':
            # Park PB-01-TG-2341 driver_age 40
            # get next non empty element in list
            arg_reg_no, last_index = get_non_empty_arg(split_command_list=text_list, starting_index=1)
            driver_age, last_index = get_non_empty_arg(split_command_list=text_list, starting_index=last_index+1)
            arg_age, last_index = get_non_empty_arg(split_command_list=text_list, starting_index=last_index+1)
            command_list[command.lower()](registration_no=arg_reg_no, driver_age=arg_age)
        else:
            arg, _ = get_non_empty_arg(split_command_list=text_list, starting_index=1)
            command_list[command.lower()](arg)

    except Exception as e:
        print("Error while parsing command :-  ", text, " error:- ", str(e))



def get_non_empty_arg(split_command_list: List, starting_index: int = 1) -> (int, int):
    """[Return first non empty argument]

    Args:
        int ([type]): [description]
        split_command_list (List, starting_index, optional): [description]. Defaults to 1)->(int.

    Returns:
        [tuple]: [description]
    """

    arg = None
    index = starting_index
    for param in split_command_list[starting_index:]:
        if param:
            arg = param
            break
    return arg, index


    

