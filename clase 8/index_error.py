# Generar en diferentes class, al menos una clase por error, las siguientes Exceptions:
#IndexError
#TypeError
#KeyError

class IndexErrorExample(Exception):
    def __init__(self, message="Índice fuera de rango"):
        self.message = message
        super().__init__(self.message)

# Ejemplo de uso
def get_element_from_list(index):
    my_list = [1, 2, 3]
    try:
        return my_list[index]
    except IndexError:
        raise IndexErrorExample("El índice está fuera de rango")

# Pruebas
try:
    print(get_element_from_list(5))
except IndexErrorExample as e:
    print(f"Error: {e.message}")