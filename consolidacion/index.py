import csv

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
                self.lista_vehiculos = []
                contar = 1
            
                while contar <= ingresar_vehiculos:
                    print(f'*****Datos del automovil {contar}******')
                    marca = input("Inserte la marca del automovil: ")
                    modelo = input("Inserte el modelo: ")
                    num_ruedas = int(input("Inserte el número de ruedas: "))
                    velocidad = int(input("Inserte la velocidad en km/h: "))
                    cilindraje = int(input("Inserte el cilindraje en cc: "))
                    automovil = Automovil(marca, modelo, num_ruedas, velocidad, cilindraje)
                    self.lista_vehiculos.append(automovil)
                    contar += 1
                    print("Vehiculo agregado correctamente")
  
                print("Imprimiendo por pantalla los Vehículos")
                for i, automovil in enumerate(self.lista_vehiculos):
                    print(
                f'Datos del automóvil {i+1}: Marca {automovil.marca}, Modelo {automovil.modelo}, {automovil.numero_ruedas} ruedas {automovil.velocidad} Km/h, {automovil.cilindrada} cc')
            
            except ValueError:
                print("Error: La cantidad de vehículos debe ser un número entero.")
            except Exception as e:
                print(f"Error inesperado al agregar vehículos: {e}")

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

class Motocicleta(Bicicleta):
    def __init__(self, _marca, _modelo, _numero_ruedas, _tipo_uso, _nro_radios, _cuadro, _motor):
        super().__init__(_marca, _modelo, _numero_ruedas, _tipo_uso)
        self.nro_radios = _nro_radios
        self.cuadro = _cuadro
        self.motor = _motor

class SistemaControlVehiculos(Automovil):
    def __init__(self):
        self.lista_vehiculos = []

    def agregar_vehiculos(self, vehiculo):
        self.lista_vehiculos.append(vehiculo)

    def guardar_csv(self, nombre_archivo):
        try:
            with open(nombre_archivo, "w", newline="") as archivo:
                archivo_csv = csv.writer(archivo)
                for vehiculo in self.lista_vehiculos:
                    if isinstance(vehiculo, Automovil):
                        datos = [
                            vehiculo.marca,
                            vehiculo.modelo,
                            vehiculo.numero_ruedas,
                            vehiculo.velocidad,
                            vehiculo.cilindrada
                        ]
                        archivo_csv.writerow(datos)
        except IOError as e:
            print(f"Error al guardar el archivo CSV: {e}")
        except Exception as e:
            print(f"Error inesperado al guardar el archivo CSV: {e}")

    def recuperar_csv(self, nombre_archivo):
        try:
            self.lista_vehiculos = []
            with open(nombre_archivo, "r") as archivo:
                archivo_csv = csv.reader(archivo)
                for fila in archivo_csv:
                    marca, modelo, num_ruedas, velocidad, cilindrada = fila
                    automovil = Automovil(marca, modelo, int(num_ruedas), int(velocidad), float(cilindrada))
                    self.lista_vehiculos.append(automovil)
        except IOError as e:
            print(f"Error al recuperar el archivo CSV: {e}")
        except Exception as e:
            print(f"Error inesperado al recuperar el archivo CSV: {e}")
        return self.lista_vehiculos
        
    
sistema = SistemaControlVehiculos()
sistema.agregar_vehiculos()
auto1 = Automovil('', '', '', '', '')

particular = Particular("Skoda", "Yeti", 4, "177", "1968", 5)
print('\n*****Verificación de Objetos*****')
print(f'Marca {particular.marca}, Modelo {particular.modelo}, {particular.numero_ruedas} ruedas {particular.velocidad} Km/h, {particular.cilindrada} cc, Puestos:{particular.numero_puestos}')
carga = Carga("Renault", "Oroch", 4, 187, "1300", "683")
print(f'Marca {carga.marca}, Modelo {carga.modelo}, {carga.numero_ruedas} ruedas, {carga.velocidad} Km/h, {carga.cilindrada} cc, Carga:{carga.peso_carga} lt')
bicicleta = Bicicleta("Kross", "Evado 4.0", 2, "Montaña")
print(f'Marca {bicicleta.marca}, Modelo {bicicleta.modelo}, {bicicleta.numero_ruedas} ruedas, Tipo: {bicicleta.tipo_uso}')
motocicleta = Motocicleta("HONDA", "CB125 TWISTER",2,"Ciudad","4T","Tubo de acero", 6)
print(f'Marca {motocicleta.marca}, Modelo {motocicleta.modelo}, {motocicleta.numero_ruedas} ruedas, Tipo: {motocicleta.tipo_uso}, Motor: {motocicleta.motor}, Cuadro: {motocicleta.cuadro}, Número de Radios: {motocicleta.nro_radios}')
print('\n*****Verificación de Relaciones*****')
print("Motocicleta es instancia con relación a Vehículo:", isinstance(motocicleta, Vehiculo))
print("Motocicleta es instancia con relación a Automóvil:", isinstance(motocicleta, Automovil))
print("Motocicleta es instancia con relación a Vehículo particular:", isinstance(motocicleta, Particular))
print("Motocicleta es instancia con relación a Vehículo de Carga:", isinstance(motocicleta, Carga))
print("Motocicleta es instancia con relación a Bicicleta:", isinstance(motocicleta, Bicicleta))
print("Motocicleta es instancia con relación a Motocicleta:", isinstance(motocicleta, Motocicleta))

sistema.guardar_csv("listado.csv")
automoviles = sistema.recuperar_csv("listado.csv")
for automovil in automoviles:
    print(automovil.marca, automovil.modelo, automovil.numero_ruedas, automovil.velocidad, automovil.cilindrada)


