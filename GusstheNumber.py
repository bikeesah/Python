import random

randNum=random.randint(1,5)
print(randNum)

while True:
    userChoice =int(input("Please guss the number :"))
    if userChoice == randNum:
        print("Sucess : you choose the correct number")
        break
    elif userChoice <randNum:
        print("Your number is too small Please guess the big number")
    else:
        print("Sorry your number was too big please choose between 1 to 100")

print("___-Game Over____")