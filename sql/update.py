#!/usr/bin/env python

from sqlalchemy import create_engine,desc,func,cast , and_ , or_ , not_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer , Numeric , String
from models import *


engine = create_engine('sqlite:///alimento_db')
Session = sessionmaker(bind=engine)

session = Session()
query = session.query(Alimento)

paninis = query.filter(Alimento.nombre.contains('in')).first()

paninis.cantidad += 1

session.commit()

print paninis.cantidad

print 'Borrar registros\n'

query = session.query(Alimento)
query = query.filter(Alimento.nombre == 'Hamburguesa')
borrar = query.one()
session.delete(borrar)
session.commit()

borrar = query.first()
print borrar