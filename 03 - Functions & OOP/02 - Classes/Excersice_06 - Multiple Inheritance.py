class Employee():
    def __init__(self,name):
        self._name = name 
    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self,value):
        self._name = value 

class Reasercher(Employee):
    def __init__(self, name, research_intrest, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        self.research_intrest = research_intrest
class Teaching(Employee):
    def __init__(self, name, modules_list, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        self.modules_list = modules_list

class Lectrurer(Reasercher,Teaching):
    def __init__(self, name,research_intrest, modules_list):
        super().__init__(name,research_intrest,modules_list)

lectrurer = Lectrurer('fabio', 'Optimasation', 'Concurency')
print(lectrurer.modules_list)
print(lectrurer.research_intrest)
print(lectrurer.name)
# Expected output: Concurency
#                  Optimasation
#                  fabio