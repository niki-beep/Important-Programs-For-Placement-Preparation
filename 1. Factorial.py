# Python program to find factorial of a number

def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i

    return fact

print(fact(5))