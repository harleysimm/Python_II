from datetime import datetime
fecha = datetime.today().strftime('%Y-%m-%d')
salas = []
carteleras =[]

class Cinema:
    def __init__(self):
        self.cine = []
        self.correlativo = 0
        
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
            salas.append(sala)

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
                print('No se encontró el cine seleccionado')

        sala_seleccionada = None
        while sala_seleccionada is None:
            print('Salas disponibles: ')
            for sala in salas:
                print(sala['numero'])
            numero_sala = int(input('Ingrese el número de la sala seleccionada: '))

            for sala in salas:
                if sala['numero'] == numero_sala:
                    sala_seleccionada = sala
                    break
            if sala_seleccionada == None:
                print('La sala seleccionada no existe')

        cartelera_existente = False
        for cartelera in carteleras:
            if(cartelera['sala'] == numero_sala and cartelera['hora'] == hora):
                cartelera_existente = True
                break
        if cartelera_existente:
            print('Ya existe una película para esa sala y hora')
        else:
            cartelera = {
                    'correlativo': self.correlativo + 1,
                    'pelicula': nombre_pelicula,
                    'cine': nombre_cine,
                    'sala': numero_sala,
                    'hora': hora,
                    'fecha': datetime.today().strftime('%Y-%m-%d')
            }
            self.correlativo +=1
            carteleras.append(cartelera)
        
            print(f'Usted ha creado con éxito la cartelera: {nombre_pelicula}, en el cine {nombre_cine} en la sala {numero_sala} el día {fecha} a las {hora} hrs.')
        
        return cartelera
    
class Boleteria(Cinema):
    def __init__(self):
        super().__init__()
        self.num_ticket = 1
        self.types =[{
            'type': 'normal',
             'price': 5000,
             'correlation_number':0
            },
        {
            'type': 'socio',
            'price': 3500,
             'correlation_number':0
            }]
        self.tickets_vendidos = []
        
    def vender_ticket(self):
        print('\n-------------------------------------------------\n')
        print('------****** Bienvenido a Cineland ******--------')
        print('\n-------------------------------------------------\n')
        print('Cartelera:')
        print('{:<5}'.format('N°'),'{:<30}'.format('Película'), '{:<15}'.format('Cine'),'{:<5}'.format('Sala'),'{:<10}'.format('Hora'),'{:<10}'.format('Fecha'))
        for cartelera in carteleras:
            print('{:<5}'.format(cartelera['correlativo']),'{:<30}'.format(cartelera['pelicula']), '{:<15}'.format(cartelera['cine']),'{:<5}'.format(cartelera['sala']),'{:<10}'.format(cartelera['hora']),'{:<10}'.format(cartelera['fecha']))
        print('\n-------------------------------------------------------------------------\n')        
        elige_pelicula = int(input('Elija el número de la película que quiere ver: '))
        if elige_pelicula <= len(carteleras):
            cartelera_elegida = carteleras[elige_pelicula - 1]
            print('Tipos de ticket:')
            for ticket in self.types:
                print('{:<15}'.format(ticket['type']),'{:<15}'.format(ticket['price']))
            ticket_elegido = input('Elija tipo ticket: ')
            ticket_encontrado = None
            for ticket in self.types:
                    if ticket['type'] == ticket_elegido:
                        ticket_encontrado = ticket
                        break
            if ticket_encontrado is not None:
                print(f'Usted ha elegido {ticket_elegido}')

                sala = None
                for sala in salas:
                    if sala['numero'] == cartelera_elegida['sala']:
                        break
                
                asientos_disponibles = [asiento for asiento in sala['asientos'] if not asiento['vendido']]
                print(f'Asientos disponibles para la película {cartelera_elegida["pelicula"]} en la sala {cartelera_elegida["sala"]}: {[asiento["numero"] for asiento in asientos_disponibles]}')

                asiento_encontrado = None
                while asiento_encontrado is None:
                    asiento_elegido = int(input('Por favor escriba un número de asiento: '))

                    for asiento in sala['asientos']:
                        if asiento['numero'] == asiento_elegido and not asiento['vendido']:
                            asiento_encontrado = asiento
                            break

                    if asiento_encontrado is not None:
                        asiento_encontrado['vendido'] = True

                        ticket_vendido = {
                            'correlativo': self.num_ticket,
                            'pelicula': cartelera_elegida['pelicula'],
                            'cine': cartelera_elegida['cine'],
                            'sala': cartelera_elegida['sala'], 
                            'hora': cartelera_elegida['hora'],
                            'fecha': cartelera_elegida['fecha'],
                            'tipo': ticket_elegido
                        }
                        self.tickets_vendidos.append(ticket_vendido)
                                                
                        print(f'Usted ha seleccionado el asiento {asiento_elegido}')
                        print(f'Usted ha elegido la película {cartelera_elegida["pelicula"]} en la sala {cartelera_elegida["sala"]} en el cine {cartelera_elegida["cine"]}, asiento {asiento_elegido} y el tipo de ticket {ticket_elegido}')
                        print(f'Su ticket es: {ticket_elegido} y su correlativo es: {self.num_ticket} y su monto a pagar es: {ticket_encontrado["price"]}')
                        
                        self.num_ticket += 1

                    else:
                        print('El asiento elegido está vendido, por favor escoja otro')
                                        
            else: 
                print('El tipo de ticket elegido no es válido')
        else:
            print('El número de película elegido no es válido')

    def total_entradas_dia(self):
        entradas_dia = {}
        for ticket in self.tickets_vendidos:
            fecha = ticket['fecha']
            if fecha in entradas_dia:
                entradas_dia[fecha] += 1
            else:
                entradas_dia[fecha] = 1
        print('\n---------------------------------------------------\n')
        print("Reporte de entradas vendidas por día:")
        print('\n---------------------------------------------------\n')
        print('{:<12}'.format('Fecha'),'{:<5}'.format('Entradas vendidas'))
        for fecha, cantidad_entradas in entradas_dia.items():
            print('{:<12}'.format(fecha),'{:<5}'.format(cantidad_entradas))

    def total_entradas_por_funcion(self):
        entradas_por_funcion = {}
        for ticket  in self.tickets_vendidos:
            funcion = f"{ticket['pelicula']} - {ticket['cine']} - Sala {ticket['sala']} - {ticket['hora']}"
            if funcion in entradas_por_funcion:
                entradas_por_funcion[funcion] += 1
            else:
                entradas_por_funcion[funcion] = 1

        print('\n---------------------------------------------------\n')
        print("Reporte de entradas vendidas por función:")
        print('\n---------------------------------------------------\n')
        print('{:<30}'.format('Función'),'{:<5}'.format('Entradas vendidas'))
        for funcion, cantidad_entradas in entradas_por_funcion.items():
            print('{:<30}'.format(funcion),'{:<5}'.format(cantidad_entradas))

    def total_entradas_por_pelicula(self):
        entradas_por_pelicula = {}
        for ticket in self.tickets_vendidos:
            pelicula = ticket['pelicula']
            if pelicula in entradas_por_pelicula:
                entradas_por_pelicula[pelicula] += 1
            else:
                entradas_por_pelicula[pelicula] = 1

        print('\n---------------------------------------------------\n')
        print("Reporte de entradas vendidas por película:")
        print('\n---------------------------------------------------\n')
        print('{:<30}'.format('Película'),'{:<5}'.format('Entradas vendidas'))
        for pelicula, cantidad_entradas in entradas_por_pelicula.items():
            print('{:<30}'.format(pelicula),'{:<5}'.format(cantidad_entradas))

    def reporte_entradas_completo(self):
        entradas_completas = {}
        for ticket in self.tickets_vendidos:
            fecha = ticket['fecha']
            pelicula = ticket['pelicula']
            funcion = f"{ticket['cine']} - Sala {ticket['sala']} - {ticket['hora']}"
            tipo_ticket = ticket['tipo']
            precio_ticket = None

            for ticket_type in self.types:
                if ticket_type['type'] == tipo_ticket:
                    precio_ticket = ticket_type['price']
                    break
            if precio_ticket is not None:
                key = (fecha, pelicula, funcion, tipo_ticket)
                if key in entradas_completas:
                    entradas_completas[key] += 1
                else:
                    entradas_completas[key] = 1
    
        print('\n-------------------------------------------------------\n')
        print("Reporte de entradas vendidas por día, película y función:")
        print('\n-------------------------------------------------------\n')
        print('{:<10}'.format('Fecha'),'{:<20}'.format('Película'), '{:<30}'.format('Función'),'{:<12}'.format('Entradas vendidas'),'{:<15}'.format('Tipo ticket'))
        for key, cantidad_entradas in entradas_completas.items():
            fecha, pelicula, funcion, tipo_ticket = key
            print('{:<10}'.format(fecha),'{:<20}'.format(pelicula), '{:<30}'.format(funcion),'{:<12}'.format(cantidad_entradas),'{:<15}'.format(tipo_ticket))


crear_cine = Cinema()
crear_cine.registrar_cine()
crear_cine.agregar_sala()
crear_cine.registrar_cine()
crear_cine.agregar_sala()
crear_cine.agregar_cartelera()
crear_cine.agregar_cartelera()
crear_cine.agregar_cartelera()

boleto = Boleteria()

boleto.vender_ticket()
boleto.vender_ticket()
boleto.vender_ticket()

boleto.total_entradas_dia()
boleto.total_entradas_por_funcion()
boleto.total_entradas_por_pelicula()
boleto.reporte_entradas_completo()
