"""
輸入一組整數範圍，將範圍中的所有質數顯示於畫面上。
EX：
請輸入開始整數:10
請輸入結束整數:50
11
13
17
19
23
29
31
37
41
43
47

"""

s = int(input("請輸入起始數字："))
e = int(input("請輸入結束數字："))

for i in range(s, e + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
