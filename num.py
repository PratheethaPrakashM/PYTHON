num=1248
n=num
count=0
while n>0:
    value=n%10
    if num % value==0:
     count=count+1
    n=n//10
print(count)     