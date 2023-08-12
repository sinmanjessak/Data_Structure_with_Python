def exactly3Divisors(N):
    # check prime no
    def Isprime(x):
        factor = 2
        while factor * factor <= x:
            if x % factor == 0:
                return False
            factor += 1
        return True

    # finding the the number which  has exactly 3 divisor.
    i = 2
    ans = 0
    while i * i <= N:
        if Isprime(i):
            ans += 1
        i += 1
    return ans


print(exactly3Divisors(50))
