from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import csv

from genera_tablas import Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

datos = open('data/mundial2018.csv', 'r', encoding='utf-8')
read = csv.reader(datos, delimiter='|')

next(read)

for row in read:
    jugador = Jugador(Numero=int(row[0]), FIFADisplayName=row[1], Country=row[2], LastName=row[3], FirstName=row[4], ShirtName=row[5],
             POS=row[6], Height=int(row[7]), Caps=int(row[8]), Goals=int(row[9]))
    session.add(jugador)
session.commit()