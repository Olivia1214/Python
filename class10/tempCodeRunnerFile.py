w = ["晴天", "多雲", "雨天", "晴天", "多雲", "雷陣雨", "雨天"]
print(w)

while True:
    try:
        ans = int(input("請輸入要修改的星期數字: "))
    except:
        print("請輸入有效的數字號碼")
    else:
        if ans > len(w) or ans < 1:
            print("請輸入有效的數字號碼")
        else:
            print("你要修改的星期數字是" + str(ans))
            print("原本的天氣是" + w[ans - 1])
            n_w = input("請輸入新的天氣: ")
            w[ans - 1] = n_w
            print("修改後的天氣是" + w[ans - 1])
            print(w)
            break