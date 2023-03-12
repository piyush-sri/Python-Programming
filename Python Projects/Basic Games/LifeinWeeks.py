age = input("What is your current age? ")

a=int(age)
ageleft=90-a
days=365*ageleft
weeks=ageleft*52
months=12*ageleft
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
