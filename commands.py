
from typing import List

from models import ParkedVehicles
from base import Session, engine, Base


def parse_command(text: str) -> None:
    """[This function is used to Parse the string, 
        extract the command and the arguments
        and call the corresponding command function.]

    Args:
        text (str): [The line we received from the input file which has to be parsed and run]
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



def get_non_empty_arg(split_command_list: List, starting_index: int = 1) -> (str, int):
    """[Return first non empty argument. Why we need this function is 
        if the input command has more than 1 space separation]

    Args:
        starting_index ([int]): [starting_index to look from the list provided]
        split_command_list (List, starting_index, optional): [command parsed by splitting based on a single space]

    Returns:
        [tuple]: [Argument, last index seen ]
    """

    arg = None
    index = starting_index
    for param in split_command_list[starting_index:]:
        if param:
            arg = param
            break
    return arg, index


    

