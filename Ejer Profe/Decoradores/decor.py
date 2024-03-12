autenticado = True


def requiere_autenticación(f):
    def function_decorada(*args, **kwargs):
        if not autenticado:
            print("Error. El usuario no se ha autenticado")
        else:
            return f(*args, **kwargs)

    return function_decorada


@requiere_autenticación
def di_hola():
    print("Hola")


di_hola()


def log(fichero_log):
    def decorador_log(func):
        def decorador_function(*args, **kwargs):
            with open(fichero_log, "a") as opened_file:
                output = func(*args, **kwargs)
                opened_file.write(f"{output}\n")

        return decorador_function

    return decorador_log


@log("fichero_salida.log")
def suma(a, b):
    return a + b


@log("fichero_salida.log")
def resta(a, b):
    return a - b


@log("fichero_salida.log")
def multiplicaDivide(a, b, c):
    return a * b / c


suma(10, 30)
resta(7, 23)


multiplicaDivide(5, 10, 2)
