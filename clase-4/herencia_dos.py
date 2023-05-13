class Persona:
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut

class Maestro(Persona):
    def __init__(self, nombre, rut, titulo_universitario):
        super().__init__(self, nombre, rut)
        self.titulo_universitario = titulo_universitario

class Estudiante(Persona):
    def __init__(self, nombre, rut, pase_estudiantil):
        super().__init__(self, nombre, rut)
        self.pase_estudiantil = pase_estudiantil

class Universitario(Estudiante):
    def __init__(self, nombre, rut, pase_estudiantil, carrera_estudiantil):
        super().__init__(self, nombre, rut, pase_estudiantil)
        self.carrera_estudiantil = carrera_estudiantil


