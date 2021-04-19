# Program ID: DRAW SQUARE
# Author: Courtney Ng
# Period: 7
# Program Description:


from turtle import*


def draw_pentagon(size):
    for x in range(0,5):
        forward(size)
        left(72)


color ('dark red', 'lavender')
begin_fill()


draw_pentagon(200)

end_fill()
done ()
