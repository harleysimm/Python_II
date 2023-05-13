# Crea una clase llamada cuenta que tendrá los siguientes atributos: titular (que es una persona) 
# y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. 
# Construye los siguientes métodos para la clase.
# •    Un constructor, donde los datos pueden estar vacíos.
# •    Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
#      directamente, solo ingresando o retirando dinero.
# •    Mostrar (): Muestra los datos de la cuenta.
# •    Ingresar (cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# •    Retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar números rojos.
class Cuenta:
    titular = 'Obligatorio'
    cantidad = 'Opcional'

    def __init__(self, titular, cantidad= 0.0):
        self.titular = titular
        self.cantidad = cantidad

    def set_titular(self, titular):
        self.titular = titular

    def get_titular(self):
        return self.titular
    
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_cantidad(self):
        return self.cantidad

    def mostrar(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad

# Ejemplo de uso
titular = {
    'nombre': 'Juan',
    'apellido': 'Perez',
    'numero_cuenta': 123456789
}

cuenta = Cuenta(titular, 100.0)
cuenta.mostrar()

cuenta.ingresar(50.0)
cuenta.mostrar()

cuenta.retirar(20.0)
cuenta.mostrar()