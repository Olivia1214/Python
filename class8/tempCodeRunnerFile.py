# 跳繩, 每當跳到十的倍數時, 就要休息一下

i = int(input("請輸入要跳繩的次數: "))
for i in range(1, i + 1):
    print(f"第{i}次跳繩")
    if i % 10 == 0:
        print("休息一下")