import Persona


class Profesor(Persona.Persona):
    def __init__(self):
        self.__Antigüedad = ""
        self.__Tutorials = ""
        self.__Phone = ""

    def GetAntigüedad(self):
        return self.__Antigüedad

    def SetAntigüedad(self, antigüedad):
        self.__Antigüedad = antigüedad

    def GetTutorials(self):
        return self.__Tutorials

    def SetTutorials(self, tutorials):
        self.__Tutorials = tutorials

    def GePhone(self):
        return self.__Phone

    def SetPhone(self, phone):
        self.__Phone = phone

    def MostrarProfesor(self):
        print("Profesor:")
        print("\tNombre:", self.GetNombre())
        print("\tApellidos:", self.GetApellidos())
        print("\tEdad:", self.GetEdad())
        print("\tAntigüedad:", self.__Antigüedad)
        print("\tTutorías:", self.__Tutorials)
        print("\tphone:", self.__Phone)
