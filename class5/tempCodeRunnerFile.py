n = int(input("請輸入箭頭大小："))
for i in range(1, n + 1):
    print(f" " * (n - i) + "*" * (2 * i - 1))
    # 這時會印出空格加上*的結果

for i in range(1, n + 1):
    print(f" " * (n - 1) + "*")
