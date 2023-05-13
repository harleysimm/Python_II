requisitos = {
    "titulo": "requerido",
    "notas": "requerido",
    "foto": "opcional"
}

print(requisitos)

#acceder a una propiedad
print(f'Las notas son de tipo {requisitos["notas"]}')
print(f'Las fotos son de tipo {requisitos["foto"]}')

#modificar una propiedad
requisitos["foto"] = "requerido"
print(f'Las fotos son de tipo {requisitos["foto"]}')
requisitos["titulo"] ="obligatorio"
print(f'Los títulos son de tipo {requisitos["titulo"]}')



## Practica --> Construir un diccionario de datos para guardar 
##              la información de un avión, coloque al menos 6 propiedades
##              imprima tres de ellas y cambie el valor de dos
##              al menos debe existir una propiedad booleana, una entera, un flotante
##              un arreglo, un diccionario y un string

boeing_737 = {
    "piloto": {
        "nombre": "Jonh",
        "apellido": "Smith"
        },
    "activo": True,
    "longitud": 39.52,
    "num_max_asientos": 210,
    "tipo_motor": "LEAP-1B de CFM Internacional",
    "seats": ["economic", "turist", "executive", "first class" ]

 }

print('\n-------------------------------------------------------\n')

# construya un programa q solicite el peso en kilogramos a una persona
# y si el peso está entre 60 y 70 recomiende una dieta de 5 comidas alta en carbohidratos
# si el peso está entre 70 y 80 recomiende una dieta de 4 comidas alta en proteinas.
# si el peso es mayor a  80 recomiende una dieta de 3 comidas alta en fibras.
# utilice solo diccionarios para agrupar los respectivos menues

menu1 = {
    "desayuno": "pan con huevo revuelto y café",
    "merienda": "una barrita de cereal",
    "almuerzo": "spaguetti con albóngidas",
    "once":"tostadas con palta y té",
    "cena":"pollo arvejado con arroz"
    }
menu2 = {
    "desayuno": "huevos revueltos y café con leche",
    "almuerzo": "filete con ensalada",
    "once":"yogurt y trozo de quesillo",
    "cena":"pechuga de pollo con quinoa"
    }
menu3= {
    "desayuno": "avena con chia, leche y fruta",
    "almuerzo": "ensalada verde con atun",
    "cena":"ensalada verde con pechuga de pollo"
    }


peso = float(input("Por favor introduzca su peso en kg: "))

if peso >= 60 and peso <=70:
    print(f"Ud necesita una dieta de 5 comidas alta en carbohidratos por ejemplo desayuno {menu1['desayuno']}")
elif peso > 70 and peso <= 80:
    print(f"Ud necesita una dieta de 4 comidas alta en proteínas por ejemplo almuerzo {menu2['almuerzo']}")
elif peso > 80:
    print(f"Ud necesita una dieta de 3 comidas alta en fibras por ejemplo cena {menu3['cena']}")
