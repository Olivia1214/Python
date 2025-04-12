import turtle as t

t.speed(1)
t.right(60)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.done()

# for 的組成有三個部分
# 1. 起始值
# 2. 終止值
# 3. 變化量
for i in range(0, 100, 20):  # range 0~99 20個一數
    print(i)

# for 迴圈繪製正方形
import turtle as t

t.speed(1)
for i in range(4):
    t.forward(100)
    t.right(90)
t.done()

import turtle as t

t.shape("circle")
t.color("red")
t.speed(0)

for i in range(0, 58):
    t.stamp()
    t.penup()
    t.right(25)
    t.forward(i + 20)

t.done()
