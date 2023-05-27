from consolidacion.Vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, _marca, _modelo, _numero_ruedas, _velocidad, _cilindrada):
        super().__init__(_marca, _modelo, _numero_ruedas)
        self.velocidad = _velocidad
        self.cilindrada = _cilindrada
        self.guardar_vehiculo = []

    def ingresar_automovil(self):
        try:
             
            ingresar_vehiculos = int(input("Cuántos vehiculos desea insertar: "))
            contar = 1
        
            while contar >= ingresar_vehiculos:

                print(f'*****Datos del automovil******')
                marca = input("Inserte la marca del automovil: ")
                modelo = input("Inserte el modelo: ")
                num_ruedas = int(input("Inserte el número de ruedas: "))
                velocidad = int(input("Inserte la velocidad en km/h: "))
                cilindraje = int(input("Inserte el cilindraje en cc: "))
                automovil = Automovil(marca, modelo, num_ruedas, velocidad, cilindraje)
                self.guardar_vehiculo.append({
                    "marca": marca,
                    "modelo": modelo,
                    "numero ruedas": num_ruedas,
                    "velocidad": velocidad,
                    "cilindraje": cilindraje
                })
                contar += 1
                break
        except:
            pass

class Carga(Automovil):
    def __init__(self, _marca, _modelo, _numero_ruedas, _velocidad, _cilindrada, _peso_carga):
        super().__init__(_marca, _modelo, _numero_ruedas, _velocidad, _cilindrada)
        self.peso_carga = _peso_carga

class Particular(Automovil):
    def __init__(self, _marca, _modelo, _numero_ruedas, _velocidad, _cilindrada, _numero_puestos):
        super().__init__(_marca, _modelo, _numero_ruedas, _velocidad, _cilindrada)
        self.numero_puestos = _numero_puestos