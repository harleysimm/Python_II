class Ticket:
    types = {
            'type': 'general',
             'price': 5000,
             'correlation_number':0
            },
    {
            'type': 'VIP',
            'price': 1000,
             'correlation_number':0
            }

def __init__(self, self_date, ):
    self.tipo_ticket = self.types[0]
    
class Token:
    type_papers = {
        'normal': 1,
        'sellado': 2
    }
    type_pays ={
        'Transbank': 1,
        'PayPal': 2,
        'Mercado Pago': 3,
        'Cash': 4
    }

    def __init__(self):
        self.type_papers = ''
        self.type_pays = ''      

class Atraction:
    type_people