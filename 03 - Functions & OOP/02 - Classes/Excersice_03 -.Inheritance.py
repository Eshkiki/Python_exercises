class Employee:
    static_max_id = 0
    __static_max_id = 1

    def __init__(self, name: str = None, grade: int = None): #constructor 
        self._name = name  
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
    
class Teacher_assistant(Employee):
    def __init__(self,name,grade,score):
        super().__init__(name,grade)
        self._score = score 

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    # Overwritting
    def to_string(self):
        print(f" score : {self.score} name: {self.name}")

alice_TA = Teacher_assistant('alice', 20, 15)
alice_TA.to_string()
# Expected output:  score : 15 name: alice

