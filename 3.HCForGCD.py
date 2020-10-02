# Python program to find the HCF of two numbers
# if i is in range 1 to number1+1 then if statement then gcd=i because highest factor will be hcf

a = int(input("Enter first number"))
b = int(input("Enter second number"))
gcd = 0
for i in range(1, a+1):
    if ((a%i==0) and (b%i==0)):
        gcd = i
    
print("The GCD of {} and {} is {}".format(a,b,gcd))
