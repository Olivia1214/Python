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
