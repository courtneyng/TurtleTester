# Program ID: turtle tester
# Author: Courtney Ng
# Period: 7
# Program Description:

from turtle import*


def forward_turn(howfar):
    forward(howfar)
    left(90)


color('light blue', 'light green')
begin_fill()

forward_turn(250)
forward_turn(150)
forward_turn(100)
forward_turn(300)

end_fill()
done()