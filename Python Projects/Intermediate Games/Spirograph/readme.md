# Spirograph Turtle Project
This program allows you to create a spirograph using Python's turtle module. A spirograph is a geometric drawing tool that creates intricate and beautiful patterns. The program uses random module to generate different patterns of the spirograph every time you run the program.

##  Requirements
- Python 3.x
- Turtle module (pre-installed with Python)
- Random module (pre-installed with Python)

##  Usage
1. Clone or download the repository to your local machine

2. Open the terminal/command prompt and navigate to the directory where the files are located

3. Run the following command to start the program:
```cmd
  python spirograph_turtle.py
```
4. The spirograph will be drawn on the turtle window. You can close the window once the drawing is complete.

# Live Demo
https://user-images.githubusercontent.com/67270567/226445938-1d5e2b6e-8ed3-4e7d-8064-139ca8ef9b02.mp4

Play the Video to see the Output

##  Line By Line Explanation of the Sourcecode

```python
  import turtle as t
  import random
```
1. In this line, we import the turtle moduleThe code imports the turtle module and renames it as t for ease of use. It also imports the random module for generating random colors.

```python
  tim = t.Turtle()
  t.colormode(255)
```
2. Here, we create a turtle object called "tim". We also set the color mode to 255. This means that the colors we choose will be in the range of 0 to 255, instead of 0 to 1.

```python
  def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
```
3. The code defines a function random_color() that generates a random RGB color by generating random values for red, green, and blue components of the color, and returning the tuple of the three values.

```python
  def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        tim.speed(20)
```
4.  The code above defines a function called draw_spirograph that takes a single argument, size_of_gap, which represents the size of the gap between the circles drawn by the turtle object named tim. Here's what the code does in detail:

  - The for loop iterates over a range of values that represent angles in degrees. The number of iterations is determined by dividing 360 degrees (a full circle) by the size_of_gap argument, and converting the result to an integer using the int() function. This determines how many circles will be drawn in the spirograph.

  - Inside the loop, the color of the turtle is set to a randomly generated color using the random_color() function (not shown in the code provided).

  - The circle() method of the turtle object is called with an argument of 100, which specifies the radius of the circle to be drawn. This draws a circle of radius 100.

  - The setheading() method is called on the turtle object, with an argument of tim.heading() + size_of_gap. This updates the direction that the turtle is facing by adding the size_of_gap value to the current heading of the turtle.

  - Finally, the speed() method is called on the turtle object with an argument of 20. This sets the speed of the turtle to 20, which is a moderate speed for drawing the spirograph.

Overall, this code generates a spirograph by drawing a series of circles with random colors and slightly offsetting each subsequent circle by the size_of_gap angle. The size_of_gap argument controls the complexity and density of the spirograph.

## Customization
You can customize the appearance of the spirograph by changing the following values in the code:

- pen size: turtle.pensize()
- pen color: turtle.pencolor()
- background color: turtle.bgcolor()
- animation speed: turtle.speed()

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code as long as you include the original license in your distribution.
