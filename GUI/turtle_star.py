import turtle

col = ('red', 'yellow','green','blue','white','cyan')

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(10000)

i = 1
while i > 0:
    t.color(col[i%6])
    t.forward(i*1)
    t.left(150)
    t.width(2)
    i += 1