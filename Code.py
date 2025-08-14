# def prime(num,):
#     a="prime"
#     for i in range(2,num//2):
#          if(num%i==0):
#             a="not prime"
#     print(a) 
# prime(11)

# a=str(input("enter the input:"))
# b=int(a)
# print(b)


# a=[1,2,3,4,1,8,2,5,7]
# b=[]
# for i in range(0,len(a)):
#     if a[i] not in b:
#         b.append(a[i])
# print(b)


# a=[1,2,1,3,4,5]

# b=set(a)
# print(b)

# num=int(input("enter the range"))
# b=[]
# def is_prime(num):
#  flag=0
#  for i in range(2,num+1):
#     for j in range(2,i):
#         if i%j==0:
#               flag=1
#               break
#         else:
#              flag=0
#     if flag==0:
#         b.append(i)
# is_prime(num)        
# print(b)


nums=[2,7,11,15]
target=9
index=[]
for i in range(len(nums)+1):
    for j in range(i+1,len(nums)):
        if target==nums[i]+nums[j]:
            index.append(i)
            index.append(j)
print(index)