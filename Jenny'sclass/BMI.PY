weight=float(input("Enter your weight in kg"))
heigth=float(input("Enter your height in meters"))


BMI=round(weight/heigth**2)

print(BMI)

if BMI<18.5:
    print(f"Your BMI IS{BMI}.You are underweight")
elif BMI<25:
    print(f"Your BMI is {BMI}.You are normal")
elif BMI<30:
    print(f"Your BMI is {BMI}.You are overweight")
elif BMI<35:
    print(f"Your BMI is {BMI}.You are obeses")

else:
    print(F"Your BMI is {BMI}.You are critically obess.")