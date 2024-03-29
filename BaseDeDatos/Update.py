#######################################
#       Fichero: Update.py            #
#    Actualiza registros de las       #
#     tablas de base de datos         #
#######################################

# Importa la librería para utilizar SQLite
import sqlite3

# Conecta a la base de datos
database = sqlite3.connect("coches.db")

# Apertura de un cursor
cursor = database.cursor()

# Lectura de todos los fabricantes
cursor.execute("SELECT * FROM Fabricante")
print("Mostrando todos los fabricantes:")
for registro in cursor:
    print(registro)

# Actualización de un fabricante
query = "UPDATE Fabricante SET Email = \
        'nuevoemailotravez@honda.es' WHERE id = 1"
cursor.execute(query)
database.commit()

# Lectura de todos los fabricantes
cursor.execute("SELECT * FROM Fabricante")
print("Mostrando todos los fabricantes:")
for registro in cursor:
    print(registro)

# Lectura de todos los coches
cursor.execute("SELECT * FROM Coche")
print("Mostrando todos los coches:")
for registro in cursor:
    print(registro)

# Actualización de un coche
query = "UPDATE Coche SET Color = 'Amarillo', Cilindrada = 3500 WHERE id = 1"
cursor.execute(query)
query = "UPDATE Coche SET Cilindrada = 1600 WHERE id = 3"
cursor.execute(query)
database.commit()

# Lectura de todos los coches
cursor.execute("SELECT * FROM Coche")
print("Mostrando todos los coches:")
for registro in cursor:
    print(registro)

# Cierra la conexión a la base de datos
database.close()
