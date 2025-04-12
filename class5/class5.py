import turtle as t

t.pensize(5)
t.pencolor("yellow")
t.fillcolor("yellow")
t.begin_fill()

for i in range(5):
    t.right(144)
    t.forward(100)

t.end_fill()
t.done()

# t.home()讓烏龜回到原點

t = input("請輸入數字:")
try:
    t = int(t)
    s = sum(range(t + 1))  # sum 函數用來累加數字
    print(s)
except:
    print("輸入錯誤!")

# 用迴圈顯示出九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j}={ i * j }")
