from models import ParkedVehicles
from base import Session, engine, Base
from commands import parse_command

# Create table if it was not created
Base.metadata.create_all(engine)

# read input file
with open('input.txt', 'r') as ip:
    # print(ip.readline())
    lines = ip.readlines()
    # read all commands in one go
    # if the number of commands is going to be huge, process each line/command while file is open

# Parse and execute each command
for line in lines:
    parse_command(line)
