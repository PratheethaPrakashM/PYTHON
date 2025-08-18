a=int(input("enter the value:"))
b=lambda a:a*a
print(b(a))
# lambda function is a python function which uses the syntax name lambda it is in the form 
#    variable= lambda arugement:expression
#     print(variable(argument))
a=[1,2,3,5]
p=[]
b=lambda a:a*a
for i in a:
  p.append(b(i))
print(p)

a=[1,2,3,4]
b=[i*i for i in a]
print(b)


a=[1,2,3,4]
b=map(lambda x:x*x,a)
c=list(map(lambda x:x*x,a))
print(c)

a=[2,4,6,7,9]
c=list(filter(lambda a:a%2==0,a))
print(c)
# syntax of map in lambda function
# variable=list(map(lambda argument:expression))

