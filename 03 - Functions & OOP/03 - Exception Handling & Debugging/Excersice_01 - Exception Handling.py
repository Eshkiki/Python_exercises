class math():
    def div(val1, val2):
        print( val1/ val2)

# catch error
try:
    math.div(4,0)
except:
    print('error')

# catch a specific error
try:
    math.div(4,0)
except ZeroDivisionError:
    print('divided bt zero')

# catch different error
try:
    math.div(4,'0')
except ZeroDivisionError:
    print('divided bt zero')
except  TypeError:
    print('wrong value type')

# catch any error
try:
    math.div(4,'0')
except  Exception as e:
    print('An error happen')

try:
    math.div(4,'0')
except  Exception as e:
    print('An error happen')
finally:
    print('no matter what , this text will be printed')
    

try:
    math.div(4,1)
except  Exception as e:
    print('An error happen')
else:
    print('print if no error is happening')
finally:
    print('no matter what , this text will be printed')