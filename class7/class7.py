# 質數判斷
n = int(input("請輸入整數："))
ans = "是質數"
for i in range(2, n):
    if n % i == 0:
        ans = "不是質數"

print(f"{n}{ans}")
