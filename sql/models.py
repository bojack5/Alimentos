from datetime import datetime
from sqlalchemy import create_engine , DateTime , ForeignKey , Boolean
from sqlalchemy.orm import sessionmaker , relationship , backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer , Numeric , String

engine = create_engine('sqlite:///alimento_db')
Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer() , primary_key=True)
    nombre = Column(String(15), nullable = False , unique = True)
    direccion = Column(String(255) , nullable = False)
    email  = Column(String(255),nullable = False)
    telefono = Column(String(25),nullable = False)
    fecha_creacion = Column(DateTime(),default=datetime.now())
    fecha_modificacion = Column(DateTime() , default = datetime.now() , onupdate=datetime.now())
    
class Orden(Base):
    __tablename__ = 'ordenes'

    id = Column(Integer() , primary_key = True)
    usuario_id = Column(Integer(),ForeignKey('usuarios.id'))
    enviado    = Column(Boolean() , default = False)
    fecha      = Column(DateTime() , default = datetime.now())
    
    usuario = relationship('Usuario' , backref=backref('ordenes' ))

class Linea(Base):
    """docstring for ObjetoLinea"""
    __tablename__ = 'lineas'    	   
    
    id = Column(Integer() , primary_key = True)
    orden_id = Column(Integer() , ForeignKey('ordenes.id'))
    alimento_id = Column(Integer() , ForeignKey('alimentos.id'))
    cantidad    = Column(Integer())
    costo_extendido = Column(Numeric(12,2))

    orden = relationship('Orden' , backref=backref('lineas'))
    alimento = relationship('Alimento',uselist = False)

class Alimento(Base):
    __tablename__ = 'alimentos'

    id     = Column(Integer , primary_key = True)
    nombre = Column(String(50) , index = True)
    sku    = Column(Integer())
    cantidad = Column(Integer())
    costo    = Column(Numeric(12,2))




Base.metadata.create_all(engine)