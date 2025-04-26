
import time

t = int(input("請輸入倒數計時的時間(秒)："))
for i in range(t, -1, -1):
    print(i)
    time.sleep(1)
else:
    print("時間到！")