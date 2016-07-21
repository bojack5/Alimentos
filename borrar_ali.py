#!/usr/bin/env python3

from tkinter.ttk import Frame, Button
from tkinter import Tk, BOTH ,Listbox, StringVar, END , Menu , Label , Entry , DISABLED
from tkinter import messagebox as mbox
from datetime import datetime
from sqlalchemy import create_engine , DateTime , ForeignKey , Boolean , func
from sqlalchemy.orm import sessionmaker , relationship , backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer , Numeric , String
import time
from sql.models import *

from tkinter import messagebox as mbox

engine = create_engine('sqlite:///alimento_db')
Session = sessionmaker(bind=engine)

session = Session()

for alimento in session.query(Alimento):
    session.delete(alimento)
    session.commit()

print(session.query(func.count(Alimento)).scalar())    