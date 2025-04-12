import turtle as t

t.shape("circle")
t.color("red")
t.speed(5)

for i in range(0, 58):
    t.stamp()
    t.penup()
    t.right(25)
    t.forward(i + 20)

t.done()