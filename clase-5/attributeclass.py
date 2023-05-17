class Student:
## @class.method --> devolver o modificar una variable de clase
    escuela_nombre = 'USACH'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def cambiar_escuela(cls, new_name):
        cls.escuela_nombre = new_name

    def ver_nombre_escuela(self):
        print(Student.escuela_nombre)

student1 = Student('Rodrigo', 24)
student1.ver_nombre_escuela()
student1.cambiar_escuela('Andrés Bello')
student1.ver_nombre_escuela()
