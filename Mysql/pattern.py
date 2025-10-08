def pyramid(m):
    for i in range(m):
        for j in range(m-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        print()    
pyramid(5)   




def reverse_pyramid(p):
    for i in range(p):
        for j in range(i):
            print(" ",end="")
        for j in range(2*(p-i)-1):
            print("*",end="")
        print()
reverse_pyramid(5)            