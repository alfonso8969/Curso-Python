diasSemanaIngles = {
    "Lunes": "Monday",
    "Martes": "Tuesday",
    "Miércoles": "Wednesday",
    "Jueves": "Thursday",
    "Viernes": "Friday",
}

disFinDeSemanaIngles = {
    "Sábado": "Saturday",
    "Domingo": "Sunday",
}

for clave, valor in disFinDeSemanaIngles.items():
    diasSemanaIngles[clave] = valor


print(diasSemanaIngles["Lunes"])
print(diasSemanaIngles["Miércoles"])
print(diasSemanaIngles["Viernes"])

# forma manual
print(diasSemanaIngles["Sábado"])
print(diasSemanaIngles["Domingo"])

# diasTotalIngles = diasSemanaIngles | disFinDeSemanaIngles
# forma automática con un nuevo diccionario
""" print(diasTotalIngles["Sábado"])
print(diasTotalIngles["Domingo"]) """
