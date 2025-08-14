# def isevenorodd(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"

# a=5
# b=10
# a=a^b
# b=a^b
# a=b^a
# print(a,b)


nums=[2,7,11,15,11,15]
unique_list=[]
[unique_list.append(i) for i in nums if i not in unique_list]
print(unique_list)