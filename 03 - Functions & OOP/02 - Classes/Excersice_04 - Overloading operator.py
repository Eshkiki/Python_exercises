class Employee():
    static_max_id = 0
    __static_max_id = 1
    def __init__(self,name : str = None, grade: int = None): #constructor 
        self.name = name 
        self.grade = grade 
        Employee.static_max_id += 1
        Employee.__static_max_id *= 2
        self.id = Employee.static_max_id

    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def get_grade(self):
        return self.grade
    def set_grade(self,grade):
        if grade is not None and grade > 0:
            self.grade = grade   
        else:
            self.grade = 1

    def get_maxId():
        return Employee.__static_max_id
    
    @classmethod
    def get_maxId_static(cls):
        return cls.__static_max_id
    

    def calc_salary(self):
        salary = (self.grade/10) * 45000
        return salary
    @staticmethod
    def static_calc_salary(grade):
        salary = (grade/10) * 45000
        return salary     
    def __add__(self,other):
        return  other.grade + self.grade
    def __str__ (self):
        return f"name: {self.name} , grade: {self.grade} max_id = {Employee.static_max_id} private max_id = {Employee.__static_max_id}"
    def __eq__(self, other):
        return self.grade == other.grade
    def __len__(self):
        return 0
    def __getitem__(self, key):
        return None

alice = Employee(name='alice', grade=4)
bob = Employee(name='bib', grade=4)

print(alice+bob)
# Expected output: 8
print(alice.__str__())
# Expected output : name: alice , grade: 4 max_id = 2 private max_id = 4