
# closure
def func_outer(message):
    def func_inner():
        print(message)
    return func_inner

func_outer(2)


# closure with cache!
def sqaure(a):
    print(a)
    return a * a 

def func_outer(func):
    results = {}
    def func_inner(*args):
        if args in results:
            res = results[args]
            print(f"{args} is already calculated {res}")
            return res 
        else:
            res = func(*args)
            results[args]  = res
            print(f"just calculated {args} => {res}")
            return res
    return func_inner 
     
 
memoized_func =   func_outer(sqaure)
memoized_func(2)
memoized_func(2)


def counter():
    count = 0
    def inner_counter():
        nonlocal count
        count += 1
        return count
    return inner_counter
cnt  = counter()
print(cnt())
print(cnt())




