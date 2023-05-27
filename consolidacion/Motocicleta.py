from consolidacion.Bicicleta import Bicicleta

class Motocicletas(Bicicleta):
    def __init__(self, _marca, _modelo, _numero_ruedas, _tipo_uso, _nro_radios, _cuadro, _motor):
        super().__init__(_marca, _modelo, _numero_ruedas, _tipo_uso)
        self.nro_radios = _nro_radios
        self.cuadro = _cuadro
        self.motor = _motor