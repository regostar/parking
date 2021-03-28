from models import ParkedVehicles
from base import Session, engine, Base

# Create table if it was not created
Base.metadata.create_all(engine)

# read input file
