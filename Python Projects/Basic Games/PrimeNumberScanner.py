#Prime numbers are numbers that can only be cleanly divided by themselves and 1. 
def prime_checker(number):
    flag=True
    for i in range(2,number):
        if(number%i==0):
            flag=False
    if(flag):
        print("It's a prime number.") 
    else:
        print("It's not a prime number.")


 
    
 
n = int(input("Check this number: "))
prime_checker(number=n)
