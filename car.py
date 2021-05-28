class Car:
    # makes="Honda"
    # speed=80
    # color="blue"
    # model ="Civic"  
    def __init__(self,make,color,model,speed) :
          self.make=make
          self.color=color
          self.model=model
          self.speed=speed
    def park(self):
        return f"my car is called  {self.make}, it is {self.color} . {self.model} is its model and it runs at a {self.speed} speed."
    def hoot(self):
        return f" The {self.make} hooted."


