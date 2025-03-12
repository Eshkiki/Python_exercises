class Employee:
    static_max_id = 0
    __static_max_id = 1 # Private

    def __init__(self, name: str = None, grade: int = None): #constructor 
        self._name = name  # Protected
        self.grade = grade # Use the property setter here
        Employee.static_max_id = 1
        Employee.__static_max_id *= 2
        self.id = Employee.static_max_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value: int):
        if value is not None and value > 0:
            self._grade = value
        else:
            self._grade = 1

    @property
    def max_id(self):
        return self.__static_max_id

    @classmethod
    def get_maxId_static(cls):
        return cls.__static_max_id
    
    def to_string(self):
        print(f"name: {self.name}, grade: {self.grade}, max_id = {Employee.static_max_id}, private max_id = {Employee.__static_max_id}")

    def calc_salary(self):
        salary = (self.grade / 10) * 45000
        return salary

    @staticmethod
    def static_calc_salary(grade):
        salary = (grade / 10) * 45000
        return salary

alice = Employee('alice',20)
alice.to_string()
# Expected output: name: alice , grade: 20 max_id = 1 private max_id = 2

new_employee = Employee()
new_employee.to_string()
# Expected output: name: None , grade: None max_id = 2 private max_id = 4

'''
new_employee.set_name('bob')
print(new_employee.get_name())
# Expected output: AttributeError: 'Employee' object has no attribute 'set_name'
'''

print(Employee.static_max_id)
# Expected output: 2

'''
print(Employee.__max_id)
# Expected output: AttributeError: type object 'Employee' has no attribute '__max_id'. Did you mean: 'max_id'?'
'''
print(Employee.get_maxId_static())
# Expected output: 4


print(alice.calc_salary())
# Expected output: 90000.0

print(Employee.static_calc_salary(20))
# Expected output: 90000.0

jon = Employee('jon', 0)
jon.to_string()
# Expected output:name: name: jon, grade: 1, max_id = 1, private max_id = 8