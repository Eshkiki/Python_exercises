class math():
    def div(val1, val2):
        if val2 < 1:
            raise ValueError('value should be positive')
        print( val1/ val2)

'''
math.div(4,0)
# Expected output: raise ValueError('value should be positive')'
'''

try:
    math.div(4,0)
except ValueError:
    print('ValueError')
