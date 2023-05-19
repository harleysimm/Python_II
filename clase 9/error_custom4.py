class NewError(Exception):
    def __init__(self, *args):
        self.value = args

try:
    raise NewError(1, 3, 'Casa', [0, 922])
except Exception as error:
    print(error.args)