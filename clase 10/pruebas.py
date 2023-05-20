from datetime import datetime
fecha = datetime.today().strftime('%Y-%m-%d')

class Cinema:
    def __init__(self):
        self.salas = []
        self.carteleras =[]
        self.cine = []
        
    def registrar_cine(self):
        nombre = str(input('Ingrese el nombre del cine a crear: '))
        rut = str(input('Ingrese el rut del cine a crear: '))
        direccion = str(input('Ingrese la direccion del cine a crear: '))
        self.cine.append({
            'nombre' : nombre,
            'rut': rut,
            'direccion': direccion})
        print(f'Usted ha creado con éxito el cine: {nombre}, {rut}, {direccion}.')

    def agregar_sala(self):
        inicio = int(input('Ingrese la sala inicial a crear: '))
        fin = int(input('Ingrese la sala final a crear: '))
        cantidad_asientos = int(input('Ingrese la cantidad de asientos por sala: '))
        
        for numero_sala in range(inicio, fin + 1):
            sala ={'numero': numero_sala, 'asientos': [] }
            for numero_asiento in range(cantidad_asientos):
                asiento = {'numero': numero_asiento + 1, 'vendido': False}
                sala['asientos'].append(asiento)
            self.salas.append(sala)

        print(f'Usted ha creado con éxito las salas de {inicio} a {fin} con {cantidad_asientos} de asientos cada una.')

    def agregar_cartelera(self):
        nombre_pelicula = str(input('Ingrese el nombre de la película a registrar: '))
        hora = input('Ingrese el horario de la película (HH:MM): ')

        cine_seleccionado = None
        while cine_seleccionado is None:
            print('Cines Disponibles: ')
            for cine in self.cine:
                print(cine['nombre'])
            nombre_cine = str(input('Ingrese el nombre del cine seleccionado: '))

            for cine in self.cine:
                if cine['nombre'] == nombre_cine:
                    cine_seleccionado = cine
                    break
        if cine_seleccionado == None:
            print('No se encontró el cine seleccionado.')

        sala_seleccionada = None
        while sala_seleccionada is None:
            print('Salas disponibles: ')
            for sala in self.salas:
                print(sala['numero'])
            numero_sala = int(input('Ingrese el número de la sala seleccionada: '))

            for sala in self.salas:
                if sala['numero'] == numero_sala:
                    sala_seleccionada = sala
                    break
        if sala_seleccionada == None:
            print('La sala seleccionada no existe.')
        
        cartelera = {
                    'pelicula': nombre_pelicula,
                    'cine': nombre_cine,
                    'sala': numero_sala,
                    'hora': hora,
                    'fecha': datetime.today().strftime('%Y-%m-%d')
                     }
        
        self.carteleras.append(cartelera)
        
        print(f'Usted ha creado con éxito la cartelera: {nombre_pelicula}, en el cine {nombre_cine} en la sala {numero_sala} el día {fecha} a las {hora} hrs.')
        
        return cartelera
    
class Boleteria(Cinema):
    def __init__(self):
        super().__init__()
        self.carteleras = []
        self.num_ticket = 0
        self.types = {
            'type': 'normal',
             'price': 5000,
             'correlation_number':0
            },
        {
            'type': 'Socio',
            'price': 3500,
             'correlation_number':0
            }
        
    def vender_ticket(self):
        print('\n-----------------------------------------\n')
        print('----****** Bienvenido a Cinema ******--------')
        print('\n-----------------------------------------\n')
        print('Cartelera:')
        for cartelera in self.carteleras:
            print('{:<15}'.format(cartelera['pelicula']), '{:<15}'.format(cartelera['cine']),'{:<15}'.format(cartelera['sala']),'{:<15}'.format(cartelera['hora']),'{:<15}'.format(cartelera['fecha']))


crear_cine = Cinema()
crear_cine.registrar_cine()
crear_cine.agregar_sala()
crear_cine.agregar_cartelera()

boleto = Boleteria()
boleto.salas = crear_cine.salas
boleto.carteleras = crear_cine.carteleras

boleto.vender_ticket()

