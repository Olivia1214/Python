# 迴圈的 break 可以用來跳出所屬的迴圈, 所以判斷 break 屬於哪個迴圈時, 必須要注意縮排
# EX:

for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            break
        print(f"i: {i}, j: {j}")

# 這裡的 break 只會跳出內層的 for 迴圈, 外層的 for 迴圈還是會繼續執行

b = 0
while b != 4:
    print("1.蘋果汁" "2.柳橙汁" "3.葡萄汁" "4.系統關閉")
    try:
        b = int(input("請輸入你的選擇(編號): "))
        if b == 1:
            print("你的選擇是蘋果汁")
        elif b == 2:
            print("你的選擇是柳橙汁")
        elif b == 3:
            print("你的選擇是葡萄汁")
        elif b == 4:
            break
        else:
            print("輸入錯誤, 請重新輸入")
    except:
        print("輸入錯誤, 請重新輸入")

# continue
# 迴圈的 continue 可以用來跳過當前的迴圈, 繼續執行下一次的迴圈
# EX:

for i in range(5):
    if i == 2:
        continue
    print(i)

# 這裡的 continue 會跳過 i == 2 的那次迴圈, 直接執行 i == 3 的那次迴圈
# 所以輸出的結果會是 0, 1, 3, 4
# continue 也可以用在 while 迴圈中
# EX:

i = 0
while i < 5:
    if i == 2:
        continue
    print(i)
    i += 1
# continue 也要判斷所屬的迴圈, 所以要注意縮排

# 跳繩, 每當跳到十的倍數時, 就要休息一下

i = int(input("請輸入要跳繩的次數: "))
for i in range(1, i + 1):
    print(f"第{i}次跳繩")
    if i % 10 == 0:
        print("休息一下")
