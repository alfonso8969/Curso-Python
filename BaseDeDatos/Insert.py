#######################################
#       Fichero: Insert.py            #
#   Inserta en base de datos los      #
#     registros de las tablas         #
#######################################

# Importa la librería para utilizar SQLite
import sqlite3

# Conecta a la base de datos
database = sqlite3.connect("coches.db")

# # Crea los registros de fabricantes
# register1 = (3, "Renault", "911234567", "Calle Japón 51", "hello@renault.es")
# register2 = (4, "Tesla", "919876543", "Calle España 121", "info@tesla.es")

# # Apertura de un cursor e inserción de los fabricantes
cursor = database.cursor()
# cursor.execute("INSERT INTO Fabricante VALUES(?,?,?,?,?)", register1)
# cursor.execute("INSERT INTO Fabricante VALUES(?,?,?,?,?)", register2)

# # Commit de las operaciones
# database.commit()

# Crea los registros de los coches
register1 = (5, 3, "Megan", 1600, "Azul")
register2 = (6, 3, "Space", 2400, "Negro")
register3 = (7, 4, "x", 1200, "Rojo")
register4 = (8, 4, "x-2", 1800, "Blanco")

# Inserción de los modelos de coches
cursor.execute("INSERT INTO Coche VALUES(?,?,?,?,?)", register1)
cursor.execute("INSERT INTO Coche VALUES(?,?,?,?,?)", register2)
cursor.execute("INSERT INTO Coche VALUES(?,?,?,?,?)", register3)
cursor.execute("INSERT INTO Coche VALUES(?,?,?,?,?)", register4)

# Commit de las operaciones
database.commit()

# Cierra la conexión a la base de datos
database.close()
