# iterative Approach
def factorial(n):
       # because the factorial of 0 is always 1.
    res= 1
    for item in range( 2, n+1):
        res= res* item
    return res
   
#Recurssive approach

def Factorial(n):
    if n==0:
        return 1
    return n * Factorial(n-1)


print(factorial(3))
print(Factorial(6))