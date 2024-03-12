# Calculadora con 4 métodos y parámetros con enteros
# Queremos usar type() para ver como Python decide los tipos en base
# a los valores de iniciales que le damos


import sys


def sumar(a: str, b: str):
    """
    This function adds two numbers together.

    Parameters
    ----------
    a : str
        The first number to add.
    b : str
        The second number to add.

    Returns
    -------
    Union[int, float]
        The sum of the two numbers.

    Raises
    ------
    ValueError
        If the input values are not integers or floats.
    """
    print("Type a:", type(a))
    print("Type b:", type(b))

    try:
        if a.__contains__(".") or b.__contains__("."):
            return float(a) + float(b)
        return int(a) + int(b)
    except ValueError:
        print("Error: Los valores no son enteros")
        return main()


def restar(a: str, b: str):
    """
    This function subtracts two numbers.

    Parameters
    ----------
    a : str
        The first number to subtract.
    b : str
        The second number to subtract.

    Returns
    -------
    Union[int, float]
        The difference of the two numbers.

    Raises
    ------
    ValueError
        If the input values are not integers or floats.
    """
    try:
        if a.__contains__(".") or b.__contains__("."):
            return float(a) - float(b)
        return int(a) - int(b)
    except ValueError:
        print("Error: Los valores no son enteros")
        return main()


def multiplicar(a: str, b: str):
    """
    This function multiplies two numbers.

    Parameters
    ----------
    a : str
        The first number to multiply.
    b : str
        The second number to multiply.

    Returns
    -------
    Union[int, float]
        The product of the two numbers.

    Raises
    ------
    ValueError
        If the input values are not integers or floats.
    """
    try:
        if a.__contains__(".") or b.__contains__("."):
            return float(a) * float(b)
        return int(a) * int(b)
    except ValueError:
        print("Error: Los valores no son enteros")
        return main()


def dividir(a: str, b: str):
    """
    This function divides two numbers.

    Parameters
    ----------
    a : str
        The first number to divide.
    b : str
        The second number to divide.

    Returns
    -------
    Union[int, float]
        The result of the division.

    Raises
    ------
    ValueError
        If the input values are not integers or floats.
    ZeroDivisionError
        If the second number is zero.
    """
    print("Type a:", type(a))
    print("Type b:", type(b))

    try:
        if a.__contains__(".") or b.__contains__("."):
            return float(a) / float(b)
        return int(a) / int(b)
    except ValueError:
        print("Error: Los valores no son enteros")
        return main()
    except ZeroDivisionError:
        print("Error: No se puede dividir entre 0")
        return main()


def main():
    """
    This function is the main function of the calculator.
    It prompts the user for input, and calls the appropriate function
    based on the user's input for the operation to perform.
    """
    print("===============================")
    print("Bienvenido")
    print("Calculadora de dos números")
    print("Introduzca exit() para salir de la calculadora")
    print("===============================")
    # Pedir al usuario los valores de a y b
    a = input("Introduce el valor de a: ")
    b = input("Introduce el valor de b: ")
    ope = input("Introduce el operador +, -, * o /: ").lower()
    if a.__contains__("exit()") or b.__contains__("exit()") or ope.__contains__("exit()"):
        sys.exit(0)
    selectOperation(a, b, ope)


def selectOperation(a, b, o):
    """
    This function takes in three inputs: two numbers a and b,
    and an operation o, which is one of the four arithmetic
    operations (+, -, *, /).
    It then calls the appropriate function to perform the operation
    and prints the result.
    If the input operation is not one of the four allowed operations,
    the function prints an error message and returns to the main menu.

    Parameters:
    a (str): the first number
    b (str): the second number
    o (str): the operation to be performed

    Returns:
    None

    """
    match o:
        case "+":
            print("Resultado de la suma: ", sumar(a, b))
        case "-":
            print("Resultado de la resta: ", restar(a, b))
        case "*":
            print("Resultado de la multiplicación: ", multiplicar(a, b))
        case "/":
            print("Resultado de la división: ", dividir(a, b))
        case _:
            print("Operación no válida")
            return main()
    main()


if __name__ == "__main__":
    main()
