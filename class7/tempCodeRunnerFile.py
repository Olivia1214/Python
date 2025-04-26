n = int(input("請輸入整數："))
for i in range(2, n):
    if n % i == 0:
        print(i)
if n % i != 0:
    print("此為質數")