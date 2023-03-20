class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    
    # Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def get_dni(self):
        return self.__dni
    
    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print('Error: La edad no puede ser menor a cero')
    
    def set_dni(self, dni):
        if len(dni) == 8:
            self.__dni = dni
        else:
            print('Error: El dni  debe tener 8 caracteres')
    
    def mostrar(self):
        print('Nombre:', self.__nombre)
        print('Edad:', self.__edad)
        print('DNI:', self.__dni)
    
    def es_mayor_de_edad(self):
        if self.__edad >= 18:
            return True
        else:
            return False
