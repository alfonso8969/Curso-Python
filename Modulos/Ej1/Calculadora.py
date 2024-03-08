import Operaciones


def Sumar():
    sum1: str = input("Sumando uno:")
    sum2: str = input("Sumando dos:")

    try:
        if sum1.__contains__(".") or sum2.__contains__("."):
            return print("La Suma es:", Operaciones.Sumar(float(sum1) +
                                                          float(sum2)))
        return print("La Suma es:", Operaciones.Sumar(int(sum1) + int(sum2)))
    except ValueError as ve:
        print("Error: Los valores no son enteros", ve)
        return Calculadora()


def Restar():
    minuendo: str = input("Minuendo:")
    sustraendo: str = input("Sustraendo:")
    try:
        if minuendo.__contains__(".") or sustraendo.__contains__("."):
            return print("La Resta es:", Operaciones.Restar(float(minuendo) +
                                                            float(sustraendo)))
        return print("La Resta es:", Operaciones.Restar(int(minuendo) +
                                                        int(sustraendo)))
    except ValueError:
        print("Error: Los valores no son enteros")
        return Calculadora()


def Multiplicar():
    multiplicando = input("Multiplicando:")
    multiplicador = input("Multiplicador:")
    try:
        if multiplicando.__contains__(".") or multiplicador.__contains__("."):
            return print("La Multiplicación es:",
                         Operaciones.Multiplicar(float(multiplicando) +
                                                 float(multiplicador)))
        return print("La Multiplicación es:",
                     Operaciones.Multiplicar(int(multiplicando) +
                                             int(multiplicador)))
    except ValueError:
        print("Error: Los valores no son enteros")
        return Calculadora()


def Dividir():
    dividendo = input("Dividendo:")
    divisor = input("Divisor:")
    try:
        if dividendo.__contains__(".") or divisor.__contains__("."):
            return print("La Division es:",
                         Operaciones.Dividir(float(dividendo),
                                             float(divisor)))
        return print("La Division es:", Operaciones.Dividir(int(dividendo),
                                                            int(divisor)))
    except ValueError:
        print("Error: Los valores no son enteros")
        return Calculadora()
    except ZeroDivisionError:
        print("Error: No se puede dividir entre 0")
        return Calculadora()


def Factorial():
    try:
        factorial = int(input("Introduzca el número del que"
                              + " quiere calcular el factorial: "))
    except ValueError:
        print("Error: Los valores no son enteros")
        return Calculadora()

    print(
        "El factorial de "
        + str(factorial)
        + " es: "
        + str(Operaciones.Factorial(factorial))
    )


def Potencia():
    try:
        base = int(input("Introduzca la base de la potencia: "))
        exponente = int(input("Introduzca el exponente de la potencia: "))
    except ValueError:
        print("Error: Los valores no son enteros")
        return Calculadora()
    print(
        "El valor de "
        + str(base)
        + " elevado a "
        + str(exponente)
        + " es: "
        + str(Operaciones.Potencia(base, exponente))
    )


def Calculadora():
    fin = False
    while not (fin):
        opc = int(input("Opción:"))
        if opc == 1:
            Sumar()
        elif opc == 2:
            Restar()
        elif opc == 3:
            Multiplicar()
        elif opc == 4:
            Dividir()
        elif opc == 5:
            Factorial()
        elif opc == 6:
            Potencia()
        elif opc == 7:
            fin = True


print(
    """************
Calculadora
************
Menu
1) Suma
2) Resta
3) Multiplicación
4) Division
5) Factorial
6) Potencia
7) Salir"""
)
Calculadora()
