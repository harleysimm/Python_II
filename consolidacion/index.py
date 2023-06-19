
class Vehiculo:
    def __init__(self, _marca, _modelo, _numero_ruedas):
        self.marca = _marca
        self.modelo = _modelo
        self.numero_ruedas = _numero_ruedas

class Automovil(Vehiculo):
    def __init__(self, _marca, _modelo, _numero_ruedas, _velocidad, _cilindrada):
        super().__init__(_marca, _modelo, _numero_ruedas)
        self.velocidad = _velocidad
        self.cilindrada = _cilindrada
        
    def agregar_vehiculos(self):
            try:             
                ingresar_vehiculos = int(input("Cuántos vehiculos desea insertar: "))
                contar = 1
            
                while contar <= ingresar_vehiculos:

                    print(f'*****Datos del automovil {contar}******')
                    marca = input("Inserte la marca del automovil: ")
                    modelo = input("Inserte el modelo: ")
                    num_ruedas = int(input("Inserte el número de ruedas: "))
                    velocidad = int(input("Inserte la velocidad en km/h: "))
                    cilindraje = int(input("Inserte el cilindraje en cc: "))
                    self.lista_vehiculos.append({
                        "marca": marca,
                        "modelo": modelo,
                        "numero ruedas": num_ruedas,
                        "velocidad": velocidad,
                        "cilindraje": cilindraje
                    })
                    contar += 1
                    print("Vehiculo agregado correctamente")
        
            except:
                pass

        def mostrar_vehiculos():
            pass

        def guardar_datos_csv():
            pass

        def leer_datos_csv():
            pass

class Particular(Automovil):
    def __init__(self, _marca, _modelo, _numero_ruedas, _velocidad, _cilindrada, _numero_puestos):
        super().__init__(_marca, _modelo, _numero_ruedas, _velocidad, _cilindrada)
        self.numero_puestos = _numero_puestos

class Carga(Automovil):
    def __init__(self, _marca, _modelo, _numero_ruedas, _velocidad, _cilindrada, _peso_carga):
        super().__init__(_marca, _modelo, _numero_ruedas, _velocidad, _cilindrada)
        self.peso_carga = _peso_carga

class Bicicleta(Vehiculo):
    def __init__(self, _marca, _modelo, _numero_ruedas, _tipo_uso):
        super().__init__(_marca, _modelo, _numero_ruedas)
        self.tipo_uso = _tipo_uso

class Motocicletas(Bicicleta):
    def __init__(self, _marca, _modelo, _numero_ruedas, _tipo_uso, _nro_radios, _cuadro, _motor):
        super().__init__(_marca, _modelo, _numero_ruedas, _tipo_uso)
        self.nro_radios = _nro_radios
        self.cuadro = _cuadro
        self.motor = _motor

class SistemaControlVehiculos:
    def __init__(self):
        self.lista_vehiculos = []

    


AutoMaria = SistemaControlVehiculos()
AutoMaria.agregar_vehiculos()
    