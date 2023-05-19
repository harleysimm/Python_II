class TypeErrorExample(Exception):
    def __init__(self, message="Tipo de dato incorrecto"):
        self.message = message
        super().__init__(self.message)

def add_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeErrorExample("Ambos valores deben ser enteros")
    return a + b

try:
    print(add_numbers(10, "20"))
except TypeErrorExample as e:
    print(f"Error: {e.message}")
