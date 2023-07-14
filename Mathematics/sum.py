def sum(n):
    if(n % 2 ==0):
        return (n/2)*(n+1)
    else:
        return n*(n+1)/2
print(sum(5))

#this is the most optimised Solution for this question, because it control the overflow 
# time Complexity = O(1)
#Auxilary space = O(1)


    