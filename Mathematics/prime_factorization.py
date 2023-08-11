
    
    
    
n= int(input(" enter the number : ")) 
prime_fac(n) '''

def prime_factorization(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

num = int(input("Enter a number: "))
prime_factors = prime_factorization(num)
print("Prime factorization of", num, ":", prime_factors)

time complexity :O(sqrt(n)).
aux complexity :O(log(n)).
  
