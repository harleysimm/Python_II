from consolidacion.Automovil import Automovil
from consolidacion.Automovil import Particular
from consolidacion.Automovil import Carga
from consolidacion.Motocicleta import Motocicleta
from consolidacion.Bicicleta import Bicicleta

class Vehiculo:
    def __init__(self, _marca, _modelo, _numero_ruedas):
        self.marca = _marca
        self.modelo = _modelo
        self.numero_ruedas = _numero_ruedas