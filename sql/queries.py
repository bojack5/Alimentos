#!/usr/bin/env python

from sqlalchemy import create_engine,desc,func,cast , and_ , or_ , not_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer , Numeric , String
from models import *


engine = create_engine('sqlite:///alimento_db')
Session = sessionmaker(bind=engine)

session = Session()

print session.query(Alimento.nombre , Alimento.cantidad).first()

print "ORDER BY\n"

for comida in session.query(Alimento).order_by(Alimento.cantidad):
    print '{:3} - {}'.format(comida.cantidad , comida.nombre)

print 

for comida in session.query(Alimento).order_by(desc(Alimento.cantidad)):
    print '{:3} - {}'.format(comida.cantidad , comida.nombre)

print 

for comida in session.query(Alimento).order_by(Alimento.cantidad.desc()):
    print '{:3} - {}'.format(comida.cantidad , comida.nombre)    

print "\nLIMITING\n"

query = session.query(Alimento.nombre , Alimento.cantidad).limit(2)

print [resultado.nombre for resultado in query]

print "\nDATABASE FUNCTIONS\n"

#Func es la funcion dentro del gestor de base de datos , llamar la funcion suma seria sumarlo dentro de postgress envez de python

inventario = session.query(func.sum(Alimento.cantidad)).scalar()
print 'Inventario = %s'%inventario 

print 'sin scalar()\n'
alimentos_totales = session.query(func.count(Alimento.nombre)).first()
print alimentos_totales
print 'con scalar()\n'
alimentos_totales = session.query(func.count(Alimento.nombre)).scalar()
print alimentos_totales

print '\nKEYS\n'

alimentos_totales = session.query(func.count(Alimento.nombre).label('inventario')).first()

print alimentos_totales.keys()

print alimentos_totales.inventario

print alimentos_totales

print '\nFILTER BY\n'

record = session.query(Alimento).filter_by(nombre = 'panini').first()
print record.nombre

record = session.query(Alimento).\
filter(Alimento.nombre == 'panini').first()

print record.nombre

print 'CLAUSULAS...!!!!\n'

query = session.query(Alimento).filter(
	                                   Alimento.nombre.like('%ni%'))

for record in query : print record.nombre

print 'OPERADORES'

query = session.query(Alimento.nombre,
	                  cast((Alimento.cantidad * Alimento.costo),
	                  Numeric(12,2)).label('costo_de_inventario'))

for result in query:
    print '{} - {}'.format(result.nombre,result.costo_de_inventario)

print 'CONJUNCTIONS'

query = session.query(Alimento).filter(
	or_(
        Alimento.cantidad.between(10,50),
        Alimento.nombre.contains('in')
		)
	)

for result in query: print result.nombre


print 'UPDATE'



