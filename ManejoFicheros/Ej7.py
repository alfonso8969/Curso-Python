fcrear = open("./../ficheronuevox.txt", "x")
fcrear.write("Estoy aprendiendo Python...\n")
fcrear.write("...y me encanta.\n")
fcrear.write("Me parece un lenguaje de programación\n")
fcrear.write("muy fácil de aprender.\n")

fcrear.close()

print("FICHERO CREADO")

flectura = open("./../ficheronuevox.txt", "r")
texto = flectura.read()
flectura.close()
print(texto)
