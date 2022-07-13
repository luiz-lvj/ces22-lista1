
class SuperClass1:
    def __init__(self, width = 0):
        self.width = width
    
    def duplicated_method(self, a,b):
        #Sum
        return self.width + a + b

class SuperClass2:
    def __init__(self, height = 0):
        self.height = height
    
    def duplicated_method(self, a,b):
        #Prod
        return self.height*a*b

class ChildClass(SuperClass1, SuperClass2):
    def __init__(self, value):
        super().__init__(value)
    
    def print_values(self):
        value1 = "None"
        value2 = "None"
        
        if self.width:
            value2 = self.width

        print("Height: " +  value1)
        print("Width: " + str(value2))

child_object = ChildClass(2)
child_object.print_values()

