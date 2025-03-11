# nested function
def func_outer():
    a = 2
    def func_inner():
        return a
    return func_inner() 
     
print(func_outer())


