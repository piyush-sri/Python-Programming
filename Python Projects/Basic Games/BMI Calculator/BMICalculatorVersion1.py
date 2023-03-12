#The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weight
#the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
 
bmi=int(float(weight)/(float(height)*float(height)))
print(bmi)
