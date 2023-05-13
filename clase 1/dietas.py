# Dieta recomendada en función del rango de peso
dietas = {
    'flaco': {
        'numero_comidas': 5,
        'tipo_dieta': 'alta en carbohidratos',
        'menu': [
            'Desayuno: Pan con mermelada y juguito de naranja',
            'colación: Barra de proteina',
            'Almuerzo: Pasta con salsa de tomate',
            'once: avena y granola',
            'Cena: Arroz con vegetales'
        ]
    },
    'medio': {
        'numero_comidas': 4,
        'tipo_dieta': 'alta en proteínas',
        'menu': [
            'desayuo: Huevos revueltos con tostadas',
            'almuerzo: Pechuga de pollo con ensalada',
            'once:  jugo con proteinas',
            'Cena: pollo a la parrilla con brócoli'
        ]
    },
    'obeso': {
        'numero_comidas': 3,
        'tipo_dieta': 'alta en fibra',
        'menu': [
            'Desayuno: Avena con frutas y nueces',
            'Almuerzo: Quinoa con vegetales',
            'once: Ensalada de  porotos negros '
        ]
    }
}

# Solicitar el peso de la persona
peso = float(input("Ingrese su peso en kg: "))

# condicional para decidir

#dieta_recomendada pasa a ser una propiedad del diccionario 

if peso >= 60 and peso <= 70:
    dieta_recomendada = 'flaco'
elif peso >= 71 and peso <= 80:
    dieta_recomendada = 'medio'
elif peso > 80:
    dieta_recomendada = 'obeso'
else:
    dieta_recomendada = None

# Imprimir la dieta recomendada
if dieta_recomendada:
    print("Su nutricionista le recomienda una dieta de", dietas[dieta_recomendada]['numero_comidas'], "comidas",dietas[dieta_recomendada]['tipo_dieta'])
    print("El menú es:")
    for comida in dietas[dieta_recomendada]['menu']:
        print(comida)
else:
    print("coloque un peso real ")
