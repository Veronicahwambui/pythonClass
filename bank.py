from datetime import datetime
class Account:
    
     def __init__(self ,name,phone) :
         self.name=name
         self.phone=phone
      
         self.balance=0
         self.loan_amount=0
         self.loan_limit=40000
         self.loan_fees=5
         self.transaction=[]

     def deposit(self,amount):
            try:
               amount+10
            except TypeError:
                return f"please enter amount in figures"
            if amount <=0:
                return f"please deposit  a valid amount"
            else:

                self.balance+=amount
                transaction={"amount":amount,"balance":self.balance,"narration":"You deposited","time":datetime.now()}
                self.transaction.append(transaction)
                return f"Hello  {self.name} your have deposited {amount}.Your new balance is {self.balance}"
     def  withdraw(self,withdraw ):
            try:
                withdraw +10
            except TypeError:
              return f"please enter  withdraw in figures"

            
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
            try:
             amount +10
            except TypeError:
                return f"please enter  amount in figures"

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
            try:
               amount +10
            except TypeError:
                return f"please enter  withdraw in figures"

            if amount<=0:
                return f"Amount must be greater than 0"
            elif amount>=self.loan_amount:
                payment=amount-self.loan_amount
                self.balance+=payment
                self.loan=0
                return f'You have repaid your loan new balance is {self.balance}'

            else:
                rem=self.loan_amount-amount
                transaction={"amount":amount,"balance":self.balance,"narration":"You deposited","time":datetime.now()}
                self.transaction.append(transaction)
                return f"{amount} has been deducted to repay your loan outstanding debt is {rem}"
     def transfer(self, amount,account):
            try:
                amount +10
            except TypeError:
                return f"please enter  withdraw in figures"
            if amount<0:
                return f"please enter  invalid amount"
                fee= amount* 0.05
                total=amount+fee
            if total > self. balance.account:
                return f"Your balance is {self.balance} you need{total}"
            else:
                self.balance-=total
                account.deposit=(amount)
                transaction={"amount":amount,"balance":self.balance,"narration":"You have transfered","time":datetime.now()}
                self.transaction.append(transaction)
                return f"your have transfered{amount} to {account} ,your account balance is{self.balance}"

           

     def get_statement(self):    
          for transaction in self.transaction:
              amount=transaction["amount"]
              narration=transaction["narration"]
              balance=transaction["balance"]
              time=transaction["time"]
              date=time.strftime("%D")
              print(f"{date}....{narration}....{amount}...{balance}")
class MobileMoneyAccount(Account):
      def __init__(self,name,phone,service_provider):
        Account.__init__(self,name,phone)
        self.service_provider=service_provider
      def buy_airtime(self,amount):
            try:
              amount+0
            except TypeError:
                return f"please enter  amount in figures"

            if amount<0:
                return f"your have  insuffient balance,"
            else:
                
                self.balance-=amount
                transaction={"amount":amount,"balance":self.balance,"narration":"You have bought airtime","time":datetime.now()}
                self.transaction.append(transaction)
                return f"you have  purchase your airtime of {amount}. Your new balance is {self.balance}"

            

                

    


                    
        
     