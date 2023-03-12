#Based on a user's order, work out their final bill.

#Small Pizza: Rs.15

#Medium Pizza: Rs.20

#Large Pizza: Rs.25

#Pepperoni for Small Pizza: +Rs.2

#Pepperoni for Medium or Large Pizza: +Rs.3

#Extra cheese for any size pizza: + Rs.1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

price=0

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: Rs.{bill}.")
