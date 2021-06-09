from datetime import datetime
class Account:
    
     def __init__(self ,name,phone,) :
         self.name=name
         self.phone=phone
      
         self.balance=0
         self.loan_amount=0
         self.loan_limit=40000
         self.loan_fees=5
         self.transaction=[]

     def deposit(self,amount):
            if amount <=0:
                return f"please deposit  a valid amount"
            else:

                self.balance+=amount
                transaction={"amount":amount,"balance":self.balance,"narration":"You deposited","time":datetime.now()}
                self.transaction.append(transaction)
                return f"Hello  {self.name} your have deposited {amount}.Your new balance is {self.balance}"
     def  withdraw(self,withdraw ):
            
                 total=withdraw +self.transaction
                   
                 if withdraw <=0:
                       return f" input a valid amount"
                 elif total >=self.balance :
                      return f"input client balance"
                 else:
                     self.balance=total
                     transaction={"amount":withdraw,"balance":self.balance,"narration":"You deposited","time":datetime.now()}
                     self.transaction.append(transaction)

                     return f" hello{self.name} you have successfully withdraw {withdraw} account balance{self.balance}"
     def  borrow(self, amount):
        interest=self.loan_fees/100*+amount
        
        if amount<=0:
             return f"you  cannot borrow less money"
        elif self.loan_amount>0:
              return f"clear your loan"
        elif amount > self.loan_limit:
              return f"you have exceed loan limit"
        else:
             self. loan_amount=amount+interest
             transaction={"amount":amount,"balance":self.balance,"narration":"You deposited","time":datetime.now()}
             self.transaction.append(transaction)

             return  f" succefully acquired  your loan {amount} and your loan due payment is {self.loan_amount},you new  account balance is {self.balance+amount}"
     def repay(self,amount):
         if amount<=0:
             return f"Amount must be greater than 0"
         elif amount>=self.loan_amount:
             payment=amount-self.loan_amount
             self.balance+=payment
             transaction={"amount":amount,"balance":self.balance,"narration":"You deposited","time":datetime.now()}
             self.transaction.append(transaction)

             return f'You have repaid your loan new balance is {self.balance}'

         else:
             rem=self.loan_amount-amount
             transaction={"amount":amount,"balance":self.balance,"narration":"You deposited","time":datetime.now()}
             self.transaction.append(transaction)

             return f"{amount} has been deducted to repay your loan outstanding debt is {rem}"

           

     def get_statement(self):    
          for transaction in self.transaction:
              amount=transaction["amount"]
              narration=transaction["narration"]
              balance=transaction["balance"]
              time=transaction["time"]
              date=time.strftime("%D")
              print(f"{date}....{narration}....{amount}...{balance}")

                

    


                    
        
     