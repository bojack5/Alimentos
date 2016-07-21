#!/usr/bin/env python

from datetime import datetime
from sqlalchemy import create_engine , DateTime , ForeignKey , Boolean
from sqlalchemy.orm import sessionmaker , relationship , backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer , Numeric , String
from models import *

engine = create_engine('sqlite:///alimento_db')
Session = sessionmaker(bind=engine)

session = Session()

Myriam = Usuario(nombre = 'zara',
	                email  = 'chicharra@negro.com',
	                telefono = '1111-555-555',
	                )

session.add(Myriam)


o1 = Orden()
o1.usuario = Myriam
session.add(o1)

al1 = session.query(Alimento).filter(Alimento.nombre == 'panini').one()

linea1 = Linea(alimento = al1 , cantidad = 3 , costo_extendido = 3.00)

al2 = session.query(Alimento).filter(Alimento.nombre == 'Sandwich').one()

linea2 = Linea(alimento = al2 ,cantidad = 12 , costo_extendido = 1.00)

o1.lineas.append(linea1)
o1.lineas.append(linea2)
session.commit()

