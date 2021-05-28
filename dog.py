class Dog:
    #  name="fufi"
    #  age=4
    #  color="blown"
      def __init__(self, name,age,color):
           self.name=name
           self.age=age
           self.color=color
      def run(self):
          return f"my dog is called {self.name} It's {self.age} years old and It's color is{self.color}"
      def bark(self):
          return f"my {self.name} barks everyday"