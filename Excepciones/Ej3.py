print("¡Iniciando programa!")
print("\n¡Comenzando primera parte del programa!")
try:
    print(str(17 / 0))
except ZeroDivisionError as zex:
    print("ERROR:", zex)
finally:
    print("¡Primera parte de programa acabada!")

print("\n¡Comenzando segunda parte del programa!")
try:
    print(str(17 / 1))
except ZeroDivisionError as zex:
    print("ERROR:", zex)
finally:
    print("¡Segunda parte de programa acabada!")
