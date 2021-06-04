class Account:
    
     def __init__(self ,name,phone,transaction) :
         self.name=name
         self.phone=phone
         self.transaction=50
         self.balance=0
     def deposit(self,amount):
            if amount <=0:
                return f"please deposit  a valid amount"
            else:

                self.balance+=amount
                return f"Hello  {self.name} your have deposited {amount}.Your new balance is {self.balance}"
     def  withdraw(self,withdraw ):
            
                 total=withdraw +self.transaction
                    #    return f"Hello ,your{self.a}
                 if withdraw <=0:
                       return f" input a valid amount"
                 elif total >=self.balance :
                      return f"input client balance"
                 else:
                     self.balance=total
                     return f" hello{self.name} you have successfully withdraw {withdraw} account balance{self.balance}"


                    
        
     