# Adding new attribute
class Meta(type):
    def __new__(cls, name, bases, dct):  # call befor __init__
        dct['created_at'] = '2025-03-13'
        return super().__new__(cls, name, bases, dct)

class Employee(metaclass=Meta):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name

emp = Employee('alice')
print(f"{str(emp)} is created at {emp.created_at}")  
# Expected outputs: alice is created at 2025-03-13

print('-'*10)

# Singleton pattern
class MySingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MySingletonMeta, cls).__call__(*args, **kwargs)
            cls.created_at = '2025-03-13'
            print('new! instance')
        return cls._instances[cls]

class Employee(metaclass=MySingletonMeta):
     

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# Example usage
emp1 = Employee(name='alice')
print(f"{str(emp1)} is created at {emp1.created_at}") 
# Expected outputs: new! instance
# alice is created at 2025-03-13

emp2 = Employee(name='alice')
print(f"{str(emp2)} is created at {emp2.created_at}") 
# Expected outputs: 

emp3 = Employee(name='bob')
print(f"{str(emp3)} is created at {emp3.created_at}") 
# Expected outputs: 



# Validate a class!
class class_validotor(type):
    def __new__(cls,name,basess,dct):
        if 'pay' not in dct:
            raise TypeError(f"Class {name} must define 'pay'")
        return super().__new__(cls,name,basess,dct)
'''
class Teacher_assistant(metaclass= class_validotor):
    def pay (self):
        print('pay something')

class Tutor(metaclass= class_validotor):
    def teach(self):
        print('teach something')


ta = Teacher_assistant()

tutor = Tutor()
# Expected output: TypeError: Class Tutor must define 'pay'
'''