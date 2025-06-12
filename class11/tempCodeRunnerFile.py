shopping_list = []

new_item = 0

print("購物清單：")
print("目前清單是空的！")
print("功能選單：")
print("1. 新增東西")
print("2. 修改東西")
print("3. 刪除東西")
print("4. 離開程式")

while True:
    try:
        ans = int(input("請輸入你的選擇 (1-4)："))
    except:
        print("請輸入有效的數字號碼")
    else:
        if ans == 1:
            print("新增選單：")
            print("a. 加到尾端")
            print("b. 插入指定位置")
            while True:
                try:
                    add = input("請選擇方法 (a/b)：")
                except:
                    print("請輸入有效的數字號碼")
                else:
                    if add == "a":
                        print("請輸入要新增的物品：")
                        item = input()
                        shopping_list.append(item)
                        print(item, "已加入清單！")
                        print("目前購物清單：", shopping_list)
                        break
                    elif add == "b":
                        print("請輸入要新增到清單中的物品：")
                        item = input()
                        print("請輸入位置 (0 為第一個)：")
                        pos = int(input())
                        shopping_list.insert(pos, item)
                        print(item, "已新增到清單中的位置", pos, "！")
                        print(item, "已加入清單！")
                        print("目前購物清單：", shopping_list)
                        break
                    else:
                        print("請輸入有效的數字號碼")
        elif ans == 2:
            print("修改選單：")
            print("請輸入要修改的物品編號：")
            shopping_list[item] = new_item
            print("物品已修改！")
            print("購物清單：")
            print(new_item)
        elif ans == 3:
            print("刪除選單：")
            print("a. 依名稱刪除")
            print("b. 依位置刪除")
            while True:
                try:
                    del_method = input("請選擇方法 (a/b)：")
                except:
                    print("請輸入有效的數字號碼")
                else:
                    if del_method == "a":
                        print("請輸入要刪除的物品名稱：")
                        shopping_list.remove(item)
                        print(item, "已從清單中移除。")
                        print("目前購物清單：", shopping_list)
                        break
                    elif del_method == "b":
                        print("請輸入要刪除的物品編號：")
                        shopping_list.pop(item)
                        print(item, "已從清單中移除。")
                        print("目前購物清單：", shopping_list)
                        break
                    else:
                        print("請輸入有效的數字號碼")
        elif ans == 4:
            print("再見！")
            break
        else:
            print("請輸入有效的數字號碼")
