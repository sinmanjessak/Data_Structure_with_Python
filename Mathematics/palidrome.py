#reverse a number

def palina(n):
    rev= n[::-1]
    return rev

print(palina("radha"))

#find the Palindrome

def palin(n):
    num= n[::-1]
    if n== num:
        print("success__",num)
    else:
        print("try again")


print(palin("78387"))
