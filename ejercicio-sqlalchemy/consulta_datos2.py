from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Presentar todos los jugadores, ordenados por la estatura.
jugadores = session.query(Jugador).order_by(Jugador.Height.desc()).all()

for x in jugadores:
    print("Nombre: %-25s Altura: %d" % (x.FIFADisplayName, x.Height))