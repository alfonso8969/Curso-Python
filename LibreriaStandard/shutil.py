import os
import shutil
print("¡Cambiando directorio de trabajo!")
os.chdir("/Users/alfre/Desktop/Ejercicio/")
print("Nuevo directorio de trabajo: ",os.getcwd())
print("Contenido del directorio: ", os.listdir())
print("¡Copiando el fichero prueba.txt!")
shutil.copy("prueba.txt","NuevaPrueba.txt")
print("Contenido del directorio: ", os.listdir())
print("¡Renombrando el fichero NuevaPrueba.txt!")
os.rename("NuevaPrueba.txt","Ejercicio.txt")
print("Contenido del directorio: ", os.listdir())
print("¡Creando el nuevo directorio!")
os.mkdir("NuevoDirectorio")
print("Contenido del directorio: ", os.listdir())
print("¡Moviendo el fichero al nuevo directorio!")
shutil.move("Ejercicio.txt","NuevoDirectorio")
print("Contenido del directorio: ", os.listdir())
print("¡Cambiando directorio de trabajo!")
os.chdir("/Users/alfre/Desktop/Ejercicio/NuevoDirectorio")
print("Nuevo directorio de trabajo: ",os.getcwd())
print("Contenido del directorio: ", os.listdir())