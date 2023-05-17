## Accedemos a los atributos
## Públicos --> Por defecto en phyton todos los atributos son públicos
## privados -->
## @property --> devolver el valor de un atributo privado
## al colocar __ como prefijo a una variable la coloca como privada
## @variable.setter --> modificar el atributo privado
## @class.method --> devolver o modificar una variable de clase

class Empleado:
    sueldo = 0 ## variable de clase

    def __init__(self, name):
        self.name = name

persona = Empleado('Juan Perez')
print(persona.name)

## Redifiniendo la clase para hacer el atributo publico name privado

class EmpleadoProtected:
    sueldo = 0

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
        

persona2 = EmpleadoProtected('Maria Perez')
print(persona2.name)

persona2.name = 'Juan' ##está protegido y no se modifica, con el setter podemos modificar
print(persona2.name)