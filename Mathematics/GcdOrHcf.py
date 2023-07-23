# Using Most efficient Euclidean Algoridhm

def Gcd(a,b):
    if b==0:
        return a
    return Gcd(b,a%b)

print(Gcd(16,32))