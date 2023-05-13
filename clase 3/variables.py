class Alumno:
    #variable de clase
    semestre = 1
    materias = ['Phyton', 'Javascript', 'Base de datos']

    def __init__(self, name):
        #variable de instancia
        self.name = name
        self.asignatura = ''
        self.notas = []
        
    def inscribir_asignatura(self,asignatura):
        self.asignatura = asignatura

    def registrar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0
        else:
            promedio = sum(self.notas) / len(self.notas)
            return promedio

alumno1 = Alumno('Marysabel')
alumno2 = Alumno('María Soledad')
alumno3 = Alumno('María Fernanda')

print(f'alumno1: {alumno1.name} --- alumno2: {alumno2.name} --- alumno3: {alumno3.name}')
print(f'semestre alumno1: {alumno1.semestre} --- semestre alumno2: {alumno2.semestre} --- semestre alumno3: {alumno3.semestre}')

alumno2.semestre = 2 
print(f'semestre alumno1: {alumno1.semestre} --- semestre alumno2: {alumno2.semestre} --- semestre alumno3: {alumno3.semestre}')

Alumno.semestre = 3
print(f'semestre alumno1: {alumno1.semestre} --- semestre alumno2: {alumno2.semestre} --- semestre alumno3: {alumno3.semestre}')


alumno1.inscribir_asignatura('Phyton')
print(f'La asignatura inscrita del alumno {alumno1.name} es {alumno1.asignatura}')

alumno1.registrar_nota(5)
alumno1.registrar_nota(7)
alumno1.registrar_nota(4)

promedio_alumno1 = alumno1.calcular_promedio()
print(f'El promedio de notas de {alumno1.name} es: {round(promedio_alumno1,2)}')

# objeto-->sustantivo, atributo-->adjetivo, método-->verbo
#los m+etodos aportan funcionamiento al objeto
