s = int(input("請輸入起始數字："))
e = int(input("請輸入結束數字："))

ans = "是質數"

for i in range(s, e + 1):
    for j in range(2, i - 1):
        if i % j == 0:
            ans = "不是質數"
            if ans == "是質數":
                print(i)