class Persona:
    message_base = 'Te estoy llamando'
    def __init__(self, name):
        self.name = name
    
    def llamar(self):
        print(self.message_base)

    def llamar(self, medio=''):
        message = self.message_base
        if (medio != ''):
            message = f'{self.message_base} por {medio}'
        print(message)

    def llamar(self, medio='', time=''):
        message = self.message_base
        if (medio != '' and time == ''):
            message = f'{self.message_base} por {medio}'
        if (medio != '' and time != ''):
            message = f'{self.message_base} por {medio} a las {time}'
        print(message)

Juan = Persona('Juan')
Maria= Persona('Maria')
Fernando = Persona('Fernando')

Maria.llamar()
Fernando.llamar('Whatsapp')
Juan.llamar('Teams', '16:00 hrs')
