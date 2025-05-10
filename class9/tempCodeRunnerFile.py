# 升級版果汁機(用List來儲存資料)(while迴圈中不可出現果汁選項)
j_l = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]
b = 0
while b != 4:
    print(j_l)
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
