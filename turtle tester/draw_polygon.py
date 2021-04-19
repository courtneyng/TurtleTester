# Program ID: draw_polygon
# Author: Courtney Ng
# Period: 7
# Program Description:

# gets the amount of sides and the size of the polygon
sides = int(input("Choose a number for the amount of sides"))
size = int(input("How large do you want the polygon to be?"))
#= int(input("Choose a degree for the angle"))

# lets you use turtle graphics
from turtle import*
# defines so you do not have to type same thing over and over and works for many other cases
def draw_polygon (size):
    for x in range (0, sides):
        forward (size)
        left (360/sides)


# outline color, fill color
color ('dark red', 'lavender')
begin_fill()

# will draw the polygon
draw_polygon(size)

end_fill()
done ()