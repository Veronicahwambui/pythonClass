class Person:
    def __init__(self, name ,employee) :
        self.name=name
        self.employee=employee

    def getName(self):
        return f"my name is{self.name}"
    def isEmployee(self):
        return f"my name is {self.name} and i work as {self.employee}" 
class Employee(Person):
    def getName(self):
        return f"my name is{self.name}"

human=Person("veroh" ,"software developer")
print(human.getName())
print(human.isEmployee())


employee=Employee("veroh" ,"software developer")
print(employee.getName())
print(employee.isEmployee())




        