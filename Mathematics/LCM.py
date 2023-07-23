# Efficient Solution ..
'''  An efficient solution is based on the below formula for LCM of two numbers ‘a’ and ‘b’. 
   a x b = LCM(a, b) * GCD (a, b)
LCM(a, b) = (a x b) / GCD(a, b)   '''

def Gcd(a,b):
    if b==0:
        return a
    return Gcd(b,a%b)

def lcm(a,b):
    return a*b //Gcd(a,b)

print(lcm(4,8))

'''
Time Complexity: O(log(min(a,b))

Auxiliary Space: O(log(min(a,b))'''