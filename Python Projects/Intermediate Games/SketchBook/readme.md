# Live Demo

https://user-images.githubusercontent.com/67270567/226549542-cd786152-fcb2-43f9-ba1d-6d6994775f33.mp4

Press the Play button to See the Output

# Line by Line Explanation of the Code
```python
   from turtle import Turtle, Screen
```
1. **Importing Libraries**

The code starts by importing the necessary libraries `Turtle` and `Screen` from the turtle module. The `Turtle` class is used to create a turtle object that can move around the screen, while the `Screen` class is used to create the window that the turtle will be drawn on.

```python
  orbit = Turtle()
  window = Screen()
```
2. **Creating Objects**

Two objects are created, `orbit` and `window`, using the `Turtle()` and `Screen()` functions respectively. The orbit object is assigned to the `turtle`, and the window object is assigned to the `window`.

```python
  orbit.pensize(10)
  orbit.pencolor("red")
  orbit.shape("turtle")
```
3. **Setting Up the Turtle**

Several properties of the turtle object are set using the following lines of code:

  - `orbit.pensize(10)` sets the width of the turtle's pen to 10 pixels.
  - `orbit.pencolor("red")` sets the color of the turtle's pen to red.
  - `orbit.shape("turtle")` sets the shape of the turtle to the default turtle shape.
  
 ```python
 def move_forward():
    orbit.forward(10)

def move_backward():
    orbit.backward(10)

def move_left():
   new_heading = orbit.heading()+10
   orbit.setheading(new_heading)

def move_right():
    new_heading = orbit.heading() - 10
    orbit.setheading(new_heading)
 ```
 4. **Defining Movement Functions**
 
Four functions are defined to control the turtle's movement:

 - `move_forward()` moves the turtle forward by 10 pixels.
 - `move_backward()` moves the turtle backward by 10 pixels.
 - `move_left()` turns the turtle left by 10 degrees.
 - `move_right()` turns the turtle right by 10 degrees.
 
 ```python
    def clear():
    orbit.clear()
    orbit.penup()
    orbit.home()
    orbit.pendown()
 ```
 5. **Defining Clear Function**
 
Another function is defined to clear the screen and reset the turtle's position to the center of the screen. The clear() function clears the turtle's trail, lifts the turtle's pen up, moves the turtle to the center of the screen, and puts the pen back down.

```python
#Event Listener
window.listen()
window.onkey(move_forward,"w")
window.onkey(move_backward,"s")
window.onkey(move_left,"a")
window.onkey(move_right,"d")
window.onkey(clear,"c")
```
6. **Setting up Event Listener**

The code sets up an event listener using the `listen()` method on the window object. This allows the program to respond to user input. Four key bindings are defined using the `onkey()` method:


  - When the `w` key is pressed, the `move_forward()` function is called.
  - When the `s` key is pressed, the `move_backward()` function is called.
  - When the `a` key is pressed, the `move_left()` function is called.
  - When the `d` key is pressed, the `move_right()` function is called.
  - When the `c` key is pressed, the `clear()` function is called.

```python
   window.exitonclick()
```
7. Exiting the Program

The` exitonclick()` method is called on the window object to keep the window open until the user clicks on it, allowing them to view their drawings.

8. In summary, the code sets up a simple drawing application that allows users to move a turtle around the screen and create drawings using basic keyboard input. It sets up event listeners to detect keyboard input, and responds to the input by calling specific functions to control the turtle's movement. The `clear()` function is defined to clear the screen, and the `exitonclick()` method is used to keep the window open until the user clicks on it.
