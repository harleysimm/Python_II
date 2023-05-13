# Desarrollar un programa que conste de una clase padre Cuenta y dos subclases
# plazofijo cajahorro. Definir los atributos titular y cantidad y un metodo 
# para imprimir los datos en la clase Cuenta. La clase CajaAhorro tendra un metodo
# para heredar los datos y uno para mostrar la informacion.
# la clase plazoFijo tendra dos atributos propios, plazo e interes. 
# tendra un metodo para obtener el importe del interes(cantidad * interes / 100)
# y otro metodo para mostrar la informacion, datos del titular, plazo, interes y total
# de interes
# Crear al menos un objeto de cada subclase.

class Cuenta:
    def __init__(self, titular, num_cuenta, saldo):
        self.titular = titular
        self.num_cuenta = num_cuenta
        self.saldo = saldo

class PlazoFijo(Cuenta):
    def __init__(self, titular, num_cuenta, saldo, plazo, interes):
        super().__init__(titular, num_cuenta, saldo)
        self.plazo = plazo
        self.interes = interes

    def calcular_importe(self):
        return ((self.interes / 100) * self.saldo) * self.plazo

class CajaAhorro(Cuenta):
    def __init__(self, titular, num_cuenta, saldo):
        super().__init__(titular, num_cuenta, saldo)

    def mostrar_informacion(self):
        print(f'Titular: {self.titular} \n Numero cuenta: {self.num_cuenta} \n Saldo: {self.saldo} ')

MariaSol = Cuenta('Maria Soledad Infante', 123456, 10000)
Johetsy = CajaAhorro('Johetsy Alvarez', 567890, 8700)
Miguel = PlazoFijo('Miguel Velasco', 345678, 120000, 2, 10)
Johetsy.mostrar_informacion()
Miguel.calcular_importe()
print(Miguel.calcular_importe())

