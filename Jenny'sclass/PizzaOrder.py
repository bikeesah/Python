"""
pizza price 
small=150
medium=200
large=300

add chesee
extra=50

add peproni
extra=30
"""
size=input("Enter the size of pizza small ,medium, large(S/M/L)")
bill_amt=0
if size=='S' or 's':
    bill_amt +=150
    print("Small size piza price is Rs.150")
elif size=='M' or 'm':
    bill_amt +=200
    print("Medium size piza price is Rs.200")
elif size=='L' or 'l':
    bill_amt +=300
    print("Large size piza price is Rs.300")
else:
    print("Please order something......!")


pepronie=input("Do you want to add Pepronie 'y'or 'Y;")

if pepronie=='y' or pepronie =='Y':
  if size=='S' or 's':
    bill_amt +=30
  else:
     bill_amt +=50

cheese=input("Do you want extra cheese (Y/N)?..")
if cheese=='y' or cheese=='Y':
 
    bill_amt +=30

    print(f"Your Final Bill is {bill_amt}")




