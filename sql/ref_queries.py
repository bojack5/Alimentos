#!/usr/bin/env python

from datetime import datetime
from sqlalchemy import create_engine , DateTime , ForeignKey , Boolean , func
from sqlalchemy.orm import sessionmaker , relationship , backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer , Numeric , String
from models import *

query = session.query(Orden.id , Usuario.nombre , Usuario.telefono , Alimento.nombre , Linea.cantidad , Linea.costo_extendido)

query = query.join(Usuario).join(Linea).join(Alimento)

results = query.filter(Usuario.nombre.contains('y')).all()

print results

for resultado in session.query(Usuario):
    print resultado.nombre, resultado.id


query = session.query(Usuario.nombre , func.count(Orden.id))

query = query.outerjoin(Orden).group_by(Usuario.nombre)    

for row in query:
    print row