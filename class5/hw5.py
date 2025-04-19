import turtle as t

t.color("black")
t.speed(10)

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

import turtle as t
import time

t.left(90)

t.speed(0)

for j in range(60):
    t.right(6 * j)
    t.forward(100)
    time.sleep(1)
    t.home()
    t.left(90)
    t.clear()

t.done()

n = int(input("請輸入正整數："))
for i in range(1, n + 1):
    if i % 3 == 0 or i % 7 == 0:
        print(i)

n = int(input("請輸入箭頭大小："))
for i in range(1, n + 1):
    print(f" " * (n - i) + "*" * (2 * i - 1))
    # 這時會印出空格加上*的結果

for i in range(1, n + 1):
    print(f" " * (n - 1) + "*")
