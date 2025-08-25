num1=[1,3]
num2=[4,5]
c=num1+num2
c.sort()
if len(c)%2!=0:
    m=int(len(c)/2)
    print("median is",m)
else:
    m=int((len(c)-1//2+len(c)//2)/2)
    print("median is",m)


