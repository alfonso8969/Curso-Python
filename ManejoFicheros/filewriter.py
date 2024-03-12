fCrear = open("./fichero-nuevo.txt", "w")
fCrear.write("Fichero creado desde cero\n")
fCrear.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit,")
fCrear.write("sed eiusmod tempor incidunt ut labore et dolore magna aliqua.")
fCrear.write(
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi "
    "ut aliquid ex ea commodi consequat."
)
fCrear.write(
    "Exercitation id magna sint velit aute labore nisi laborum magna labore "
    "consequat exercitation irure do. In mollit in ex officia incididunt do "
    "cillum ipsum aute dolore elit. Dolore consequat excepteur excepteur sunt."
    "Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu "
    "fugiat nulla pariatur."
)
fCrear.write(
    "Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui "
    "officia deserunt mollit anim id est laborum.\n"
)
fCrear.close()

print("### Fichero creado ###")

fLectura = open("./fichero-nuevo.txt", "r")
texto = fLectura.read()
fLectura.close()
print(texto)
