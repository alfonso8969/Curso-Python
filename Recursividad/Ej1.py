def Factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * Factorial(numero - 1)


factorial = int(input("Introduzca el número del que quiere calcular el factorial: "))
print(f"El factorial de {str(factorial)} es: {str(Factorial(factorial))}")
