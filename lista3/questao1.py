from abc import abstractclassmethod
from unicodedata import name

#Métodos abstratos
class SuperClass:
    def __init__(self, name):
        self.name = name

    @abstractclassmethod
    def abstract_method(self):
        pass
    
    @classmethod
    def class_method_name_modified(cls, student_name):
        return cls("Student "+student_name)

    @staticmethod
    def static_method_sum(a,b):
        return a+b
    
    def instance_method_rename(self, new_name):
        self.name = new_name
    
    def print_name(self):
        print(self.name)
    
    
class ChildClass1(SuperClass):
    def __init__(self, name):
        self.name = name
    
    def abstract_method(self):
        print(" This is child class 1")
    
class ChildClass2(SuperClass):
    def __init__(self, name):
        self.name = name
    
    def abstract_method(self):
        print("This is child class 2")

father1 = SuperClass("Teste")
father2 = SuperClass.class_method_name_modified("Teste")
father1.print_name()
father2.print_name()

father1.instance_method_rename("teste 2")

child1 = ChildClass1("child 1")
child2 = ChildClass2("child 2")
child1.abstract_method()
child2.abstract_method()

