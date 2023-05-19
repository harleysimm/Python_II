class RevertirCadena(Exception):
    def __init__(self, cadena):
        self.cadena = cadena

    def revertir(self):
        palabras = self.cadena.split() #convierte en arreglo
        palabras_reverse = palabras[::-1] #da vuelta el arreglo
        cadena_reverse = ' '.join(palabras_reverse) #une el arreglo
        return cadena_reverse
    
class NoEsFraseException(Exception):
    def __init__(self, message = 'Una palabra no es una frase'):
        self.message = message


while True:
    try:
        cadena = input("Ingrese una frase: ")
        if not cadena:
            raise ValueError("No se ingreso ninguna frase")
        if len(cadena.split()) < 2:
            raise NoEsFraseException()
        reversor = RevertirCadena(cadena)
        print(reversor.revertir())
        break
    except ValueError as error:
        print(f'Error: {error}')
    except NoEsFraseException as error:
        print(f'Error: {error.message}')

