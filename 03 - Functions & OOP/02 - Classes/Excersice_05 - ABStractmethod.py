from abc import ABC, abstractmethod

class Employee(ABC):  # Abstract class
    @abstractmethod
    def signin(self):
        pass  # Must be implemented by child class

class Teacher_Assistant(Employee):
    def signin(self):
        return "you are ok now!"

ta = Teacher_Assistant()
print(ta.signin())  # Output: Woof!
