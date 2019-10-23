#Program Description: The following program will use turtle graphics to draw
#polygons based on the user's input of how many sides it will have.

#Author: Madeline Rodriguez

#Imports turtle graphics and random
from turtle import *
import random

#The sides function will take in the user's input of number of sides and check to
#see if it is more than 3 or less than 3
def main():
    numSides = int(input('Enter the number of sides, less than 3 to exit: '))

    #This loop will call the polygon function if the number of sides is greater
    #than 3, if not it will display a thank you message
    while numSides >= 3:
        polygon(numSides)
        numSides = int(input('Enter the number of sides, less than 3 to exit: '))
    else:
        print('Thanks for using the polygon generator program.')

#The polygon function will calculate the polygon's side length and border width
#using the number of sides inputted along with the line(border) and fill(shape)
#color
def polygon(x):

    #Calculates the polygon's side length
    sidelength = 600/x
    
    # Specify the colors list to choose the line color and fill color.
    colors = ['coral', 'gold', 'brown', 'red', 'green', 'blue', 'yellow',
              'purple', 'orange', 'cyan', 'pink', 'magenta', 'goldenrod']

    #Randomly selects the color of the fill(shape)
    shapecolor = random.choice(colors)

    #Randomly selects the color of the fill(border)
    bordercolor = random.choice(colors)

    #Calculates the size of the border width
    bordersize = (x%20) + 1

    #Calls the makePolygon function to draw the shape
    makePolygon(x, sidelength, bordercolor, bordersize, shapecolor)

# The makePolygon function draws a polygon with the number of sides,
# side length, border color, border width, and fill color as specified.
def makePolygon (sides, length, borderColor, width, fillColor):

    #Clears the window for any previous drawing
    clear()
    
    #Calculates the angles of the polygon
    angle = 360/sides

    #Gives the the shape of the turtle to be a turtle
    shape("turtle")

    #Assigns the pen it's color
    pencolor(borderColor)

    #Assigns the color that the shape will be fill in with
    fillcolor(fillColor)

    #Assigns the pen it's width size
    pensize(width)

    #Using the length and angle sizes specified it will begin to draw the shape
    begin_fill()
    while True:
        if sides != 0:
            forward(length)
            left(angle)
            sides -= 1
        else:
            break
    end_fill()

#Displays to user what the program will create  
print('This program will draw a polygon with 3 or more sides.' + '\n')

#Call the main function
main()
