# In leap year program, the number has to be divided by 3 numbers i.e if 

year = int(input('Enter a year : '))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a Leap year".format(year))

    else:
        print("{0} is a leap year".format(year))

else:
    print("{0} is not a Leap year".format(year))

