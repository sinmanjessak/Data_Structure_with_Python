def multiple(t):
    temp=0
    for i in range(2,t):       
        if (i%3==0) or (i%5==0):
            temp= temp+i
    return temp
t= int(input("enter the number : "))
print(multiple(t))