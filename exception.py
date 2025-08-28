class InvaliidName(Exception):
    pass 
def username(name):
        if len(name)<3:
         raise InvaliidName("length of name should be greater than 3")

class InvalidAge(Exception):
    pass
def userage(age):
        if age<10 or age>25:
             raise InvalidAge("Age limit should be between 10 and 25")

class InvalidScore(Exception):
    pass
def userscore(score):
        if score<0 or score>100:
             raise InvalidScore("Invalid score")
try:        
   name=input("enter the name :") 
   username(name) 
   age=int(input("enter the age :"))
   userage(age) 
   score=int(input("enter the score :"))
   userscore(score)
except InvaliidName as error:     
     print("error:",error)
except InvalidAge as error:
     print("error:",error)   
except InvalidScore as error:
     print("error:",error)
except(InvaliidName,InvalidAge,InvalidScore):
     print

               



