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



        
from collections import namedtuple
from bank import MobileMoneyAccount
mom= MobileMoneyAccount("verro","07812333","safaricom")
print(mom.deposit(1000))
print(mom.buy_airtime(500))
mom.get_statement()


numbers=[5,5,6,8,0,8]
numbers.append(20)
numbers.insert(0,10)
numbers.remove(5)
numbers.clear()
numbers.pop()
# existences ofz value
print(numbers.index(5))
# check a string if it excestence
print(50 in numbers)
print(numbers.count(5))
numbers.sort()
numbers.reverse()
#numbers2=numbers.copy()


print(numbers)
#removing duplicate
number=[2,3,4,4,2,5,5,]
uniques=[]
for a in number:
    if number not in uniques:
        uniques.append(number)
print(uniques)
#tuples
numbers=(1,2,3,4)
#dictionaries
person={"names":"veron","age":30}
person["birthday"]="jan18 1980"
print(person["name"])

message=input(">")
word=message.split(" ")
emojis ={
    ":)": ""

}
output=""
for words in word:
   output += emojis.get(word,word)
print(output)
#functions
def greet_user(first_name,last_name):
    print(f"Hi{first_name } {last_name}!")  

greet_user("john","veroh")
greet_user(first_name="veroh",last_name="jane")
#functions return
def square(number):
    return number*number


print(square(4))
#handle error
try:

   age=int(input("Age:"))
   income =20000
   risk =income/age
   print(age)
except ValueError:
     print("age  cannot be 0.")  
except ValueError:# catch the error
    print("invalid value")
#
class Point:
    def __init__(self,name,age):
        self.name=name
        self.age=age

          
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1=Point("veroh",20)  
point1. age=21
point1.move()  

#class2
class Human:
    def __init__(self,name,age):
         self.name=name
         self.age=age
    
    def talk(self):
        print(f"Hi,Iam {self.name}")

person=Human("JANE",25)
person.talk()

person1=Human("sarah",39)
person1.talk()

#inheritance
class Dog:
    def walk(self):
        print("talk")

class Cat(Dog) :
    pass

class Mammals(Dog):
      pass

dog1=Dog()
dog1.walk

        




