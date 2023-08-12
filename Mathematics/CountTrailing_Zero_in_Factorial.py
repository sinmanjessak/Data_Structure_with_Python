# this is a program for count trailing zero in factorial of a number.
# This a most efficient solution


def CountZero(n):
    res = 0
    i = 5
    while n / i >= 1:
        res = res + (n // i)
        i *= 5
    return res


# time comlexity = O(logn)
# Aux space complexity = O(1)
print(CountZero(12))

# Another way is 1)- find factorial   and then   2)- Count no of Zeros

# Write a Python program to find the number of zeros at the end of a factorial of a given positive number.


def factEndZero(n):
    x = n // 5
    y = x
    while x > 0:
        x = x // 5
        y = y + x
    return y


print(factEndZero(100))
