from consolidacion.Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, _marca, _modelo, _numero_ruedas, _tipo_uso):
        super().__init__(_marca, _modelo, _numero_ruedas)
        self.tipo_uso = _tipo_uso