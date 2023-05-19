class KeyErrorExample(Exception):
    def __init__(self, message="Clave no encontrada"):
        self.message = message
        super().__init__(self.message)

def get_value_from_dict(key):
    my_dict = {"a": 1, "b": 2}
    try:
        return my_dict[key]
    except KeyError:
        raise KeyErrorExample("La clave no existe en el diccionario")

try:
    print(get_value_from_dict("c"))
except KeyErrorExample as e:
    print(f"Error: {e.message}")
