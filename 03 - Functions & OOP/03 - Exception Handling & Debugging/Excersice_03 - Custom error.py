class MyException(Exception):
    def __init__(self, message="Error !!"):
        self.message = message
        super().__init__(self.message)

class math():
    def div(val1, val2):
        if val2 < 1:
            raise MyException('value should be positive')
        print( val1/ val2)

try:
    math.div(4,0)
except MyException:
    print('ValueError')


math.div(4,0)
