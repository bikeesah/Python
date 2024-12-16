"""
divisible by 4 it may be leap year if not not a leap year
 if divisible by 4 then check the num divisible by 100 if no the it is also not leap a year
   if divisible by 100 check divisible by 400 if divisible then leap years else not a leap year

"""
Year=int(input("Enter the year"))

if Year % 4== 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print("It is a leap year")
        else:
            print("Not a leap year")

    else:
        print("Not leap year")

else:
    print("Not leap year")