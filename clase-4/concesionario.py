## Autos, motos y biciletas
## Autos [color, tipo_motor, ruedas, cantidad_puertas, tipo_encendido, tipo_freno]
## Motos [color, tipo_motor, ruedas, tipo_encendido, tipo_freno, tipo_cadena]
## Bicicletas [color, ruedas, tipo_freno, marca, modelo, tipo_manubrio] 

class Vehiculo:
    def __init__(self, color, ruedas, tipo_freno):
        self.color = color
        self.ruedas = ruedas
        self.tipo_freno = tipo_freno

    def frenar(self):
        print('Este vehículo está frenando')

class VehiculoMotorizado:
    def __init__(self, tipo_motor, tipo_encendido):
        self.tipo_motor = tipo_motor
        self.tipo_encendido = tipo_encendido

    
class Auto(Vehiculo):
    def __init__(self, color, ruedas, tipo_freno, tipo_motor, tipo_encendido):
        Vehiculo.__init__(self, color, ruedas, tipo_freno)
        VehiculoMotorizado.__init__(self, tipo_motor, tipo_encendido)

    def abrir_puerta(self, puerta):
        print (f'Abriendo puerta {puerta}')

class Moto(Vehiculo):
    def __init__(self, color, ruedas, tipo_freno, tipo_motor, tipo_encendido, tipo_cadena):
        Vehiculo.__init__(self, color, ruedas, tipo_freno)
        VehiculoMotorizado.__init__(self, tipo_motor, tipo_encendido)
        self.tipo_cadena = tipo_cadena

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo_freno, tipo_manubrio):
        super().__init__(color, ruedas, tipo_freno)
        self.tipo_manubrio = tipo_manubrio

    def pedalear(self, sentido):
        print(F'La bicicleta está pedaleando hacia {sentido}')

Bycicle = Bicicleta('roja', 2, 'torpedo', 'tipo T')
Bycicle.pedalear('adelante')
Bycicle.frenar()
