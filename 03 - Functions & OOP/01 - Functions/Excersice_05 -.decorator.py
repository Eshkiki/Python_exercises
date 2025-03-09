# input validation
def decorator_func(f):
    def wrapper(*args):
        args = (min(args[0], 10),)
        return f(*args)
    return wrapper

@decorator_func
def sqaure(a):
    return a * a 


print(sqaure(12))
# expected output : 109



# use decorator for repeating a function
def repeat_func(n):
    def docorate(f):
        def wrapper(*arg):
            for _ in range(n):
                f(*arg)
        return wrapper
    return docorate

@repeat_func(3)
def sqaure(a):
    print( a * a )

sqaure(4)
        
# use decorator for repeating a function, return all values in a list
def repeat_func(n):
    def docorate(f):
        def wrapper(*arg):
            list = []
            for _ in range(n):
                list.append(f(*arg))
            return list
        return wrapper
    return docorate

@repeat_func(3)
def sqaure(a):
    return( a * a )

print(sqaure(4))


# use decorator for timing
import time
def timing(n):
    def docorate(f):
        def wrapper(*arg):
            start =  time.time()
            for _ in range(n):
                f(*arg)
            duration = time.time()- start
            print(f"Execution time : {duration:.6f} seconds")
            return duration
        return wrapper
    return docorate

@timing(30000)
def sqaure(a):
    return( a * a )

print(sqaure(4))


# log

# Access Control




# limit time between calling function
def decorator(func):
    last_time = [0] # needs to be mutable like a list  
    def wrapper(*args):
        gap = time.time() - last_time[0]
        if gap<1:
            print('calling me too fast')
            return
        else:
            last_time[0] = time.time()
            return func(*args)
    return wrapper

@decorator
def login(password, uname):
    print(password, uname)

login("2", "alice")
login("2", "alice")
time.sleep(1.1)
login("2", "alice")
