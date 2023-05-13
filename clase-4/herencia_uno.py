class Padre:
    def __init__(self, name_padre, rut_padre):
        self.name = name_padre
        self.rut = rut_padre
        self.sueldo = 0
    
    def pintar(self):
        print(f'{self.name} estoy pintando')

class Hijo(Padre):
    def __init__(self, name_hijo, rut_hijo, color_ojos):
        Padre.__init__(self, name_hijo, rut_hijo)
        self.color_ojos = color_ojos

    def lijar(self):
        print(f'{self.name} está lijando')
        
richar = Padre('Richar Lujano', "1-9")

richard = Hijo('Richard Lujano', '1-7', 'Marron')

print(richar.name, richar.sueldo)
print(richard.name, richard.sueldo)

richar.pintar()
richard.pintar()
richard.lijar()