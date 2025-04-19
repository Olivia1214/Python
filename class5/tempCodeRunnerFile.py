import turtle as t
import time

t.left(84)

t.speed(0)

for j in range(60):
    t.right(6 * j)
    t.forward(100)
    time.sleep(1)
    t.home()
    t.left(90)
    t.clear()

t.done()