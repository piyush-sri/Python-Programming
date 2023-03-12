#You are painting a wall. The instructions on the paint can says that 
#1 can of paint can cover 5 square meters of wall. 
#Given a random height and width of wall, it will calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can.
import math
def paint_calc(height,width,cover):
    NoOfCans=math.ceil((height*width)/cover)
    print(f"You'll need {NoOfCans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
