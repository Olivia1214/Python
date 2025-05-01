s = int(input("請輸入起始數字："))
e = int(input("請輸入結束數字："))

for i in range(s, e + 1):
    for j in range(2, i):
        if i % j == 0:
            print(i)
