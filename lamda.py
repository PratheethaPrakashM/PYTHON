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
# syntax of map in lambda function
# variable=list(map(lambda argument:expression))


a=[2,4,6,7,9]
c=list(filter(lambda a:a%2==0,a))
print(c)
# syntax of filter in lambda function
# variable=list(filter(lambda argument:condition))

from functools import reduce
x=[1,2,3,4,5,6,7,8,9,10]
y= reduce(lambda a,b:a+b,x)
print(y)
# syntax of reduce in lambda function
# from functools import reduce
# variable=reduce(lambda storing,iteration:experssion)

a=['janaki','pratheetha','vishnupriya','praveena']
a.sort(key=len)
a.sort(key=lambda a :len(a))
b=sorted(a)
print(a)
print(b)
a.sort(key=len, reverse=True)
b=sorted(a,reverse=True)
print(a)
print(b)

