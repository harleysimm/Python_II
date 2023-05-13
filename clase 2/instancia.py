class Taza: #los objetos de la clase deben tener atributos y valores
    sizes = {
        'small': 'pequeno',
        'medium': 'mediano',
        'large': 'grande'
    }
    
    def __init__(self):
        self.size = self.sizes['small']

class Maquina:
    def __init__(self, tipo_cafe, cantidad_agua, cantidad_cafe):
        self.tipo_cafe = tipo_cafe
        self.cantidad_de_agua = cantidad_agua
        self.cantidad_cafe = cantidad_cafe

class Cafe: #tipo_grano {}
    def __init__(self):
        self.tipo_cafe = {
            'tipo_cafe_1': 'arabica',
            'tipo_cafe_2': 'robusta',
            'tipo_cafe_3': 'descafeinado'
    }

cafe_1 = Cafe() #instancia
#objeto  #clase
print(cafe_1)
class Leche: #tipo leche {}
    def __init__(self):
        self.tipo_leche = {
            'tipo_leche_1': 'entera',
            'tipo_leche_2': 'descremada',
            'tipo_leche_3': 'sin_lactosa',
            'tipo_leche_4': 'almendra',
            'tipo_leche_5': 'soya'
            
    }
