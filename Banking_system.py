# withraw ,deposit and checkbalance
class account:
    def __init__(self,name ,balance):
         self.__name=name
         self.__balance=balance
    def withraw(self,amount):
         if self.__balance > amount:
          self.__balance=self.__balance-amount
    def deposit(self,amount):
         if amount > 0:
          self.__balance=self.__balance+amount
    def checkbalance(self):
          print(f"{self.__name} - {self.__balance}")

user=account("Janaki",1000)    
user.checkbalance()     
# for multiple user create new user

    

