# Turtle Shapes
 This repository contains a Python project that uses the Turtle graphics module to draw shapes on the screen. The project is suitable for intermediate-level 
 programmers who are interested in exploring the capabilities of the Turtle module and learning how to create simple games in Python.
 
## Requirements
   - To run the project, you will need to have Python 3 installed on your computer, as well as the Turtle module.
   - The project was developed and tested on Python 3.9.5, but it should work on other versions of Python 3 as well.
   
## Usage
 - Clone or Download the repository to your local machine.
 - Open the terminal/command prompt and navigate to the directory where file is located.
 - To run the project, run the main.py file using Python:
```cmd
   python main.py
```
 - This will launch the game, which will draw a series of shapes on the screen using randomly selected colors.
 
# Demo Video

https://user-images.githubusercontent.com/67270567/226439699-38ad1816-0113-43e0-bb75-43655b69e6b1.mp4

 Press Play to Exit!!!

# Line By Line Explanation of Code
```python
import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
```
1.  **import turtle as t:** This line imports the turtle module and renames it as "t" to make it easier to reference in the code.
    - **import random:** This line imports the random module, which will be used later to randomly choose colors from a list.
    - **tim = t.Turtle():** This line creates a new turtle object named "tim", which will be used to draw shapes on the screen.
    - **colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]:** This line creates a list of color names       that   will be used to randomly color the shapes.
  
  ```python
  def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)
  ```
  2. **def draw_shape(num_sides):** This line defines a function called "draw_shape" that takes one parameter called "num_sides", which represents the number of sides of the shape to be drawn.
     - **angle = 360 / num_sides:** This line calculates the angle that the turtle will need to turn in order to draw each side of the shape.
     - **for i in range(num_sides):** This line starts a loop that will repeat "num_sides" times, each time drawing one side of the shape.
     - **tim.forward(100):** This line moves the turtle forward 100 pixels to draw the next side of the shape.
     - **tim.right(angle):** This line turns the turtle to the right by the angle calculated earlier, so that it will be facing in the correct direction to draw the next side of the shape.
     
 ```python
 for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)
 ```   
 3. **for shape_side_n in range(3, 10):** This line starts a loop that will repeat 7 times, each time drawing a shape with a different number of sides,
          ranging from 3 to 9.
     - **tim.color(random.choice(colours)):** This line randomly selects a color from the "colours" list and sets it as the turtle's drawing color for the next shape.
     - **draw_shape(shape_side_n):** This line calls the "draw_shape" function, passing in the current number of sides as the argument, so that the turtle will draw a               shape with that number of sides.
     
4. In summary, this code creates a turtle named "tim" and a list of colors, defines a function to draw shapes with a given number of sides, and then uses a loop to draw    a series of shapes with different numbers of sides, randomly selecting colors for each shape from the list of colors.
     
     
## Customization
   - The project can be customized in various ways, such as changing the number of shapes drawn, the colors used, and the size of the shapes. 
   - These customizations can be    made by modifying the main.py file.
   
## License
   This project is licensed under the `MIT License`. Feel free to use, modify, and distribute the code as you see fit. See the LICENSE file for more details.     
