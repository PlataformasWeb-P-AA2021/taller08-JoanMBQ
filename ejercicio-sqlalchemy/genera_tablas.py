from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

# Creacion de atributos de la Entidad Jugador
class Jugador(Base):
    __tablename__ = "jugadores"
    id = Column(Integer, primary_key=True)
    Numero = Column(Integer)
    FIFADisplayName = Column(String(100))
    Country = Column(String(100))
    LastName = Column(String(100))
    FirstName = Column(String(100))
    ShirtName = Column(String(100))
    POS = Column(String(2))
    Height = Column(Integer)
    Caps = Column(Integer)
    Goals = Column(Integer)
    
    def __repr__(self):
        return "Número: %-3s || Nombre FIFA: %-25s || Pais: %-15s || Apellido: %-15s || Nombre: %-15s \
         || Nombre camiseta: %-20s || Posicion: %-3s || Altura: %-5s || Caps: %-4s || Goles: %-3s ||\n"% (
                          self.Numero, 
                          self.FIFADisplayName, 
                          self.Country,
                          self.LastName,
                          self.FirstName,
                          self.ShirtName,
                          self.POS,
                          self.Height,
                          self.Caps,
                          self.Goals)


Base.metadata.create_all(engine)