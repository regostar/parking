# coding=utf-8

from envparse import env
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

env.read_envfile()

engine = create_engine(env("DATABASE"))
# engine = create_engine('postgresql://postgres:Infernape@777@localhost:5432/parking')
# move to env later
Session = sessionmaker(bind=engine)

Base = declarative_base()