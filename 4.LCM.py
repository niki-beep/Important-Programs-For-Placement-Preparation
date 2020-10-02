def hcf(a,b):
    hcf = 0
    for i in range(1, a+1):
        if a%i==0 and b%i==0:
            hcf = i

    return hcf


a = int(input('Enter a number :'))
b = int(input('Enter second number : '))
lcm = (a*b)/hcf(a,b)
print("Lcm of {} and {} is {}".format(a,b,lcm))