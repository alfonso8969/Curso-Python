print("¡Iniciando programa!")
try:
    print(str(17 / 0))
except ZeroDivisionError:
    print("ERROR: Division por cero")
except Exception:
    print("ERROR: General")
else:
    print("¡No se han producido errores!")
finally:
    print("¡Programa acabado!")
