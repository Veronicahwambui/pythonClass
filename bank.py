class Bank:
    #  accounttype="Student"
    #  pin=86779
    #  balance=30.0
     def __init__(self ,accounttype,pin,balance) :
         self.accounttype=accounttype
         self.pin=pin
         self.balance=balance
     def withdraw(self):
         return f"my  account type is {self.accounttype} ,pin {self.pin}.My balance is {self.balance}"
        
     def atmcard(self):
          return f"my atmcard balance is {self.balance}"
