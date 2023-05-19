## Sintexis try except
## try
##      codigo
##      codigo
##      ......
## except ExceptionName
##      codigo
##      codigo
##      ......
dividendo = 100
while True:
    try:
        edad = int(input('Introduce tu edad: '))
        calculo = dividendo / edad
        print(f'El resultado es: {calculo}')
        # break
    except ValueError:
        print('Debes introducir una edad válida')
    except ZeroDivisionError:
        print('La edad debe ser mayor a cero')
    else:
        print('else se va a ejecutar solo cuando no haya error')
    finally:
        print('finally se va a ejecutar tanto haya un error como no haya un error')
    break

dividendo = 100
while True:
    try:
        edad = int(input('Introduce tu edad: '))
        result = dividendo / edad
        break
    except ValueError as error:
        print('Debe colocar una edad válida')
        print(type(error))
        print(error.args)
        print(error)
    except ZeroDivisionError as error:
        print(type(error))
        print(error.args)
        print(error)