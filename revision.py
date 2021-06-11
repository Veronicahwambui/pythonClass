class Person:

     def __init__(self, name, age,location, phonenumber):
             self.name=name
             self.age=age
             self.location=location
             self.phonenumber=phonenumber
     def Study(self):
         return f"My name is{self.name} ,I am {self.age} years old and I live in {self.locatoion}"
      

    #  def run(self,eat):
    #      if



        
from bank import MobileMoneyAccount
mom= MobileMoneyAccount("verro","07812333","safaricom")
print(mom.deposit(1000))
print(mom.buy_airtime(500))
mom.get_statement()
