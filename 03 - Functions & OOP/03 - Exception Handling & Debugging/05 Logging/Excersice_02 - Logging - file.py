import logging

'''
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL
'''
logging.basicConfig(level=logging.INFO, filename='app.log',format='%(asctime)s - %(levelname)s - %(message)s')

class math():
    def div(val1, val2):
        logging.debug(f'div : {val1}, {val2}')
        if val2 >0:
            print( val1/ val2)
        else:
            logging.error(f'div : non positive {val1}, {val2}')
            return 0
    def add(val1, val2):
        logging.info(f'add : {val1}, {val2}')
        print( val1+ val2)
    def diff(val1, val2):
        logging.warning(f'diff : {val1}, {val2}')
        print( val1- val2)
    def dot(val1, val2):
        logging.critical(f'dot : {val1}, {val2}')
        print( val1* val2)

math.div(5, 3)
# Expected output:  1.6666666666666667
'''
debug will be ignored! 
'''                  
math.add(5, 3) 
# Expected output: 8
math.diff(5, 3)
# Expected output: 2
math.dot(5, 3) 
# Expected output: 15

'''
output is in the app.log
'''
