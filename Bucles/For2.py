listaAbecedario = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "ñ",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
listaIteraciones = [1, 2, 3, 4, 5]
for item in listaIteraciones:
    print("Iteración número: " + str(item))
    for letra in listaAbecedario:
        print(letra, end=" ")
    print("\n")
