# Live Demo
 

https://user-images.githubusercontent.com/67270567/226451638-85522054-b02e-4672-8322-7dafec1b1f05.mp4

Press Play to see the Output

# Line by Line Explanation of the code

```python
    import turtle as turtle_module
```
1. This line imports the turtle module, which provides turtle graphics primitives, in both object-oriented and procedure-oriented ways. It's imported as turtle_module to make it easier to use throughout the code.

```python
    turtle_module.colormode(255)
```
2. This line sets the color mode for the turtle to RGB color values. The colormode() function specifies the maximum value that can be used for each RGB color value, and here it's set to 255, which is the maximum value for an 8-bit color depth.

```python
  tim = turtle_module.Turtle()
```
3. This line creates a new turtle object called tim. The Turtle() function creates a new turtle object, which is used to draw on the screen.

```python
   tim.speed("fastest")
```
4. This line sets the speed of the turtle to the fastest possible speed. The speed() function sets the speed of the turtle to a predefined value, or to a number between 0 and 10, where 0 is the fastest possible speed.

```python
   tim.penup()
```
5. This line lifts the pen up so that the turtle does not leave any trails while moving. The penup() function lifts the pen up, so that subsequent movements of the turtle will not be drawn on the screen.

```python
  tim.hideturtle()
```
6. This line hides the turtle so that it is not visible while moving. The hideturtle() function hides the turtle from view, so that it doesn't interfere with the drawing on the screen.

```python
    color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
```
7. This line creates a list of RGB color values that will be used to color the dots. Each tuple in the list represents an RGB color value.

```python
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
```
8. These lines set up the initial position of the turtle. The setheading() function sets the direction that the turtle is facing, where 0 is towards the right side of the screen. The forward() function moves the turtle forward by the specified number of pixels.

```python
number_of_dots = 100
```
9. This line sets the number of dots to be painted.
```python
 for dot_count in range(1, number_of_dots + 1):
```
10. This line sets up a for loop that will iterate from 1 to the total number of dots. The range() function creates a sequence of numbers
