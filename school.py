class School:
    number_student=0
    def __init__(self,name,id):
       self.name=id
       self.id=id
       self.fees=50000
       self.excess=0
       
    def calaculateFee(self,amount):
        try:
            amount+0 
        except TypeError:
            return f"please enter  amount in figures"
        if amount<=500 and amount < 0:
            return f"you have paid less amount"
        elif amount< self.fees and amount > 500:
              balance =self.fees-amount
              return f"you  amount is {balance} "   
        else:
            excess=amount-self.fees
            self.excess+=excess
            return f" you have paid excess and your balance is {self.excess}"


        



