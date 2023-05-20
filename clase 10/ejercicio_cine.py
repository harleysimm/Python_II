class Cinema:
    def __init__(self):
        self.salas = []
        self.carteleras =[]
        self.cine = []
        
    def registrar_cine(self, nombre, rut, direccion):
        self.cine.append(Cinema(nombre, rut, direccion))
        nombre = str(input('Ingrese el nombre del cine a crear: '))
        rut = str(input('Ingrese el rut del cine a crear: '))
        direccion = str(input('Ingrese el rut del cine a crear: '))


    def agregar_sala(self, sala):
        self.salas.append(sala)

    def agregar_cartelera(self, cartelera):
        self.carteleras.append(cartelera)

    def obtener_cartelera(self, fecha):
        for cartelera in self.carteleras:
            if cartelera.fecha == fecha:
                return cartelera
        return None
    
    def reporte_entradas_dia (self, fecha):
        total_entradas = 0
        for cartelera in self.carteleras:
            if cartelera.fecha == fecha:
                total_entradas += cartelera.total_entradas_vendidas()
            return total_entradas

class Salas:
    def __init__(self, num_sala, asientos):
        self.num_sala = num_sala
        self.asientos = asientos

class Cartelera:
    def __init__(self, peliculas, fecha, hora):
        self.peliculas = peliculas
        self.fecha = fecha
        self.hora = hora

    def agregar_pelicula(self, pelicula, sala, horario):
        self.peliculas.append((pelicula, sala, horario))

    def reporte_entradas_funcion(self):
        total_entradas = 0
        for pelicula, _, _ in self.peliculas:
            total_entradas += pelicula.reporte_entradas_funcion()
            return total_entradas

class Ticket:
    def __init__(self, num_ticket, fecha, hora):
        self.num_ticket = num_ticket
        self.fecha = fecha
        self.hora = hora
        self.asiento = None
        self.types = {
            'type': 'normal',
             'price': 3500,
             'correlation_number':0
            },
    {
            'type': 'VIP',
            'price': 7000,
             'correlation_number':0
            }
    
    def asignar_asiento(self, asiento):
        self.asiento = asiento

class Boleteria:
    def __init__(self, num_ticket, pelicula, asiento, fecha, hora):
        self.num_ticket = num_ticket
        self.pelicula = pelicula
        self.asiento = asiento
        self.fecha = fecha
        self.hora = hora

Cine_Oriente = Cinema('Oriente', '77.777.777-1', 'Av.Kennedy 5001, Vitacura', 4)
Cine_Poniente = Cinema('Poniente', '77.777.777-2', 'Av. Pajaritos 750, Maipu', 2)
Cine_Centro = Cinema('Centro', '77.777.777-3', 'Huerfanos 234, Santiago', 5)