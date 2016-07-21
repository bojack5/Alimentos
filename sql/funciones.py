#!/usr/bin/env python
from datetime import datetime
from sqlalchemy import create_engine , DateTime , ForeignKey , Boolean
from sqlalchemy.orm import sessionmaker , relationship , backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer , Numeric , String

engine = create_engine('sqlite:///alimento_db')
Session = sessionmaker(bind=engine)

session = Session()

