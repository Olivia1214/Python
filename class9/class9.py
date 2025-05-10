import random as r

# random.randrange 設定範圍的方式跟 range 一樣, 特性也一樣不包含最後一個數字
# random.randrange 的功能是隨機取得一個數字, range 是產生一組數字
print(r.randrange(10))  # 從0~9中隨機取得一個數字
print(r.randrange(1, 10))  # 從1~9中隨機取得一個數字
print(r.randrange(1, 10, 2))  # 從[1, 3, 5, 7, 9]中隨機取得一個數字

# random.randint 設定範圍的方式必須要有開始跟結束, 且包含最後一個數字
# 不能跳數字抽籤
print(r.randint(1, 10))  # 從1~10中隨機取得一個數字

import random as r

# 數字猜測遊戲(需提示再大一點或小一點)
n = r.randint(1, 100)
g = int(input("請輸入你的猜測(1~100):"))
while g != n:
    if n > g:
        print("再大一點")
    elif n < g:
        print("再小一點")
    g = int(input("請輸入你的猜測(1~100):"))

print("恭喜猜中了")

# List 清單 (List)
# List 可以存入很多資料, 每筆資料用`,`隔開
# List 可以存入不同型態的資料
# List 最外層用[]包起來
L = [1, 2, 3, 4, 5]  # 數字
print(L)
# 不同型態混合
L = [1, 2, 3, 4, 5, "Hello", ["World", 6]]  # 數字, 字串, List
print(L)

# List 取值
# List 取值方式跟字串一樣, 用[]來取值
# List 取值方式跟字串一樣, 也可以用[:]取值
# List 當中資料的編號(index)都從0開始
L = [1, 2, 3, 4, 5]
print(L[0])  # 取得第一個值
print(L[1])  # 取得第二個值
print(L[2])  # 取得第三個值

# List 取值方式跟字串一樣, 也可以用[:]取值
# 設定範圍的方式跟 range 一樣, 特性也一樣不包含最後一個數字
print(L[1:4:2])  # 取出第二個到第四個值, 間隔2個
print(L[0:3])  # 取出第一個到第三個值
print(L[:3])  # 取出第一個到第三個值
print(L[3:])  # 取出第四個到最後一個值
print(L[:])  # 取出全部值

# list len 列表長度
L = [1, 2, 3, 4, 5]
print(len(L))  # 取得List長度, 也就是List當中有幾筆資料

# 務必不要跟index編號混淆, index 是資料的編號, len 是資料的數量

# len 可以搭配 for 迴圈使用來取得 List 當中的所有資料
for i in range(len(L)):  # 這邊的 i 是 index
    print(L[i])

for i in L:  # 這邊的 i 是資料
    print(i)

# 要使用哪一種方式讀取 List 當中的資料, 要看使用的情境當中會不會需要index

# 升級版果汁機(用List來儲存資料)(while迴圈中不可出現果汁選項)
j_l = ["蘋果汁", "柳橙汁", "葡萄汁", "楊桃汁", "系統關閉"]
b = 0
while b != len(j_l):
    for i in range(len(j_l)):
        print(f"{i + 1}.{j_l[i]}")
    try:
        b = int(input("請輸入你的選擇(編號): "))
        if b < len(j_l):
            print(f"你的選擇是{j_l[b-1]}")
        elif b == len(j_l):
            break
        else:
            print("輸入錯誤, 請重新輸入")
    except:
        print("輸入錯誤, 請重新輸入")
