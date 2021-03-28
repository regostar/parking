# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:Infernape@777@localhost:5432/parking')
# move to env later
Session = sessionmaker(bind=engine)

Base = declarative_base()