'''
def find_divisors(n):
    divisors = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    divisors.sort()
    return divisors

num = int(input("Enter a number: "))
divisors = find_divisors(num)
print("Divisors of", num, "in sorted order:", divisors)

#time complexity : O(sqrt(n)
#space complexity : O(sqrt(n)

'''

def find_divisor(n):
    i=1
    while(i*i<n):
        if n % i==0:
            print(i)
        i+=1
    while(i>=1):
        if n % i==0:
            print(n//i)
        i-=1
        
print(find_divisor(44))

#time complexity : O(sqrt(n)
#space complexity :O(1)