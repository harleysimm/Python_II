class NoPuedeEscribirDosException(Exception):
    def __init__(self, _value):
            self.value = _value

try:
    number = input('Introduce un número: ')
    if (number == '2'):
        raise NoPuedeEscribirDosException('Introdujo un número 2 y este no es válido')
    else:
        print('El número introducido es válido')
except Exception as error:
    print(type(error))
    print(error.args)
