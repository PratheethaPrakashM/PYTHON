# withraw ,deposit and checkbalance
class account:
    def __init__(self,name ,balance=0):
         self.__name=name
         self.__balance=balance
    def withraw(self,amount):
         if self.__balance > amount:
          self.__balance=self.__balance-amount
    def deposit(self,amount):
         if amount > 0:
          self.__balance=self.__balance+amount
    def checkbalance(self):
          print(f"Name={self.__name} \nBalance= {self.__balance}")

user=account("Janaki")    
user.deposit(5000)
user.withraw(6000)
user.checkbalance()     
# for multiple user create new user
# student details and institution  details
    

