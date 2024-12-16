import random
import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
pass_length=int(input("Enter the length of password "))

generator=string.ascii_letters+string.digits+string.punctuation

password= ""

for i in range (pass_length):
    password += random.choice(generator)

print("Your generated random password is :", password)
# password=random.choice(1.5)
# print(password)