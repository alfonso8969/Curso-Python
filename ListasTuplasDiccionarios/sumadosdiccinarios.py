diassemanaingles = {
    "Lunes": "Monday",
    "Martes": "Tuesday",
    "Miércoles": "Wednesday",
    "Jueves": "Thursday",
    "Viernes": "Friday",
}

diasdefindesemanaingles = {
    "Sábado": "Saturday",
    "Domingo": "Sunday",
}

for clave, valor in diasdefindesemanaingles.items():
    diassemanaingles[clave] = valor


print(diassemanaingles["Lunes"])
print(diassemanaingles["Miércoles"])
print(diassemanaingles["Viernes"])

# forma manual
print(diassemanaingles["Sábado"])
print(diassemanaingles["Domingo"])

# diastotalesingles = diassemanaingles | diasdefindesemanaingles
# forma automatica con un nuevo diccionario
""" print(diastotalesingles["Sábado"])
print(diastotalesingles["Domingo"]) """
