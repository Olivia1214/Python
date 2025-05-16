import random as r

# 數字猜測遊戲(需提示再大一點或小一點)(需要提示縮小過後的輸入範圍)
low = 1
high = 100
n = r.randint(1, 100)
g = int(input(f"請輸入你的猜測({low}~{high}):"))
while g != n:
    if n > g:
        print("再大一點")
        low = g
    elif n < g:
        print("再小一點")
        high = g
    g = int(input(f"請輸入你的猜測({low}~{high}):"))

print("恭喜猜中了")