s=[int(i) for i in input("Enter the numbers\n").split(",")]
sum=0
for i in s:
    sum+=i
print("Total sales=",sum)
avg=sum//len(s) 
print(avg)   
maximum=s[0]
minimum=s[0]
for i in s:
    if i>maximum:
        maximum=i
    elif i<minimum:
        minimum=i    
print(maximum)
print(minimum)
if avg>200:
    print("Good Performance")
else:
    print("Needs Improvement")
s.reverse()
print(s)
