import turtle as t

t.color("black")
t.speed(5)

t.penup()
t.forward(200)
t.penup()
t.right(90)
t.forward(75)
t.left(90)

for i in range(8):
    t.stamp()
    t.penup()
    t.right(135)
    t.forward(160)
    t.left(90)

t.home()
t.done()
