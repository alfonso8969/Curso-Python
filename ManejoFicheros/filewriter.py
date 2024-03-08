fcrear = open("./ficheronuevo.txt", "w")
fcrear.write("Fichero creado desde cero\n")
fcrear.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit,")
fcrear.write("sed eiusmod tempor incidunt ut labore et dolore magna aliqua.")
fcrear.write(
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi "
    "ut aliquid ex ea commodi consequat."
)
fcrear.write(
    "Exercitation id magna sint velit aute labore nisi laborum magna labore "
    "consequat exercitation irure do. In mollit in ex officia incididunt do "
    "cillum ipsum aute dolore elit. Dolore consequat excepteur excepteur sunt."
    "Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu "
    "fugiat nulla pariatur."
)
fcrear.write(
    "Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui "
    "officia deserunt mollit anim id est laborum.\n"
)
fcrear.close()

print("### Fichero creado ###")

flectura = open("./ficheronuevo.txt", "r")
texto = flectura.read()
flectura.close()
print(texto)
