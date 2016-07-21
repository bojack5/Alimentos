#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer , Numeric , String
from models import *

engine = create_engine('sqlite:///alimento_db')
Session = sessionmaker(bind=engine)

session = Session()

panini = Alimento()

panini.nombre = 'panini'
panini.sku    = 'SW001'
panini.cantidad = 1
panini.costo    = 15.5

session.add(panini)
session.commit()

print panini.id

a1 = Alimento(nombre = 'Sandwich',
              sku = 'SW002',
              cantidad = 3,
              costo = 60)

a2 = Alimento(nombre = 'Hamburguesa',
              sku = 'SW003',
              cantidad = 2,
              costo = 40)

session.bulk_save_objects([a1,a2])
session.commit()

comidas = session.query(Alimento).all()

for alimento in comidas:
    print alimento.nombre
