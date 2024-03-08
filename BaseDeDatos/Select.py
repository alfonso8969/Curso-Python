#######################################
#       Fichero: Select.py            #
#    Lee de la base de datos los      #
#     registros de las tablas         #
#######################################

# Importa la librería para utilizar SQLite
import sqlite3

# Conecta a la base de datos
database = sqlite3.connect(r"C:\Users\Mañanas\Downloads\libroPython"
                           r"\BaseDeDatos\Coches.db")

# Apertura de un cursor
cursor = database.cursor()

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

# Lectura de todos los coches a partir del fabricantes
cursor.execute("SELECT * FROM Fabricante")
for registro in cursor:
    print("Mostrando todos los coches del fabricante: ", registro[1])
    # Nuevo cursor para ejecutar la consulta para los coches
    cursorCoches = database.cursor()
    # Ejecución de la query
    parametro = (registro[0],)
    cursorCoches.execute(
        "SELECT Modelo, Cilindrada, Color FROM Coche where FabricanteId = ?",
        parametro)
    # Muestra la información de cada coche asociada al fabricante
    for registroCoche in cursorCoches:
        print(registro[1], " ", registroCoche[0], ", ",
              registroCoche[1], "cc, ", registroCoche[2])

# Cierra la conexión a la base de datos
database.close()
