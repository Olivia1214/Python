# 質數判斷
n = int(input("請輸入整數："))
ans = "是質數"
for i in range(2, n):
    if n % i == 0:
        ans = "不是質數"

print(f"{n}{ans}")

# for ...else
# 當 for 迴圈正常結束時, 執行 else 區塊內的程式
# example:
for i in range(5):
    print(i)
else:
    print("for 迴圈正常結束")

# while ...else
# 當 while 迴圈正常結束時, 執行 else 區塊內的程式
# example:
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("while 迴圈正常結束")

# 迴圈的 break 可以用來跳出所屬的迴圈, 所以判斷break屬於哪個迴圈時, 必須要注意縮排
# example:
for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            break
        print(f"i:{i}, j:{j}")

import time

t = int(input("請輸入倒數計時的時間(秒)："))
for i in range(t, -1, -1):
    print(i)
    time.sleep(1)
else:
    print("時間到！")
