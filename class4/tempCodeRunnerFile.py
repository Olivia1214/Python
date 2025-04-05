import turtle as t

t.shape("circle")
t.color("red")
t.speed(5)

for i in range(0, 60):
    t.stamp()
    t.penup()
    t.right(20)
    t.forward(i+10)
    
t.done()