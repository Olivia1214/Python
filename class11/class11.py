# 複製 List, 避免原本的變數被修改
L = ["Hello", "World"]
L2 = L.copy()  # 使用 copy() 複製 List
print(L2)  # ['Hello', 'World']
L2[0] = "Python"  # 修改 L2
print(L)  # ['Hello', 'World']
print(L2)  # ['Python', 'World']
# 這跟變數的 = 賦值不同, 一般情況下會開兩個記憶體空間
# 在 List 的情況下使用  = 會讓兩個變數名稱指向同一個記憶體空間
# 這導致修改一個 List 會影響另一個 List
# 所以在需要複製 List 時, 可以使用 copy() 方法

# remove : 移除 List 中指定的元素(只會移除第一個找到的)
L = ["Hello", "World", "Python"]
L.remove("World")  # 移除 World
print(L)  # ['Hello', 'Python']

# pop : 移除並回傳 List 中的元素
L = ["Hello", "World", "Python"]
# 不給索引時, 移除最後一個元素
L.pop()  # 移除最後一個元素
print(L)  # ['Hello', 'Python']
s = L.pop(1)  # 移除索引為1的元素, 並回傳該值
print(s)  # World
print(L)  # ['Hello']

"""
你是一位「購物小幫手」！幫媽媽記下要買的東西，還能修改、刪除，或是看看清單裡有什麼。
📋 你可以做這些事：
程式會在每一步自動顯示目前的購物清單。
1️⃣ 新增東西
    ➕ 加到清單最後（append）
    📌 新增到清單中的某個位置（insert）
2️⃣ 修改東西
    ✏️ 輸入編號，換掉舊項目
3️⃣ 刪除東西
    ❌ 用名稱刪除（remove）
    🗑️ 用位置刪除（pop）
4️⃣ 離開程式
    👋 不想逛了就回家！
===========================================================================
購物清單：
目前清單是空的！
功能選單：
1. 新增東西
2. 修改東西
3. 刪除東西
4. 離開程式
請輸入你的選擇 (1-4)：1
新增選單：
a. 加到尾端
b. 插入指定位置
請選擇方法 (a/b)：a
請輸入要新增的物品：milk
milk 已加入清單！
購物清單：
0. milk
功能選單：
1. 新增東西
2. 修改東西
3. 刪除東西
4. 離開程式
請輸入你的選擇 (1-4)：1
新增選單：
a. 加到尾端
b. 插入指定位置
請選擇方法 (a/b)：a
請輸入要新增的物品：bread
bread 已加入清單！
購物清單：
0. milk
1. bread
功能選單：
1. 新增東西
2. 修改東西
3. 刪除東西
4. 離開程式
請輸入你的選擇 (1-4)：1
新增選單：
a. 加到尾端
b. 插入指定位置
請選擇方法 (a/b)：b
請輸入要新增到清單中的物品：egg
請輸入位置 (0 為第一個)：1
egg 已新增到清單中的位置 1！
購物清單：
0. milk
1. egg
2. bread
功能選單：
1. 新增東西
2. 修改東西
3. 刪除東西
4. 離開程式
請輸入你的選擇 (1-4)：2
修改選單：
請輸入要修改的物品編號：0
請輸入新的物品：soy milk
物品已修改！
購物清單：
0. soy milk
1. egg
2. bread
功能選單：
1. 新增東西
2. 修改東西
3. 刪除東西
4. 離開程式
請輸入你的選擇 (1-4)：3
刪除選單：
a. 依名稱刪除
b. 依位置刪除
請選擇方法 (a/b)：a
請輸入要刪除的物品名稱：egg
egg 已從清單中移除。
購物清單：
0. soy milk
1. bread
功能選單：
1. 新增東西
2. 修改東西
3. 刪除東西
4. 離開程式
請輸入你的選擇 (1-4)：3
刪除選單：
a. 依名稱刪除
b. 依位置刪除
請選擇方法 (a/b)：b
請輸入要刪除的物品編號：0
soy milk 已從清單中移除。
購物清單：
0. bread
功能選單：
1. 新增東西
2. 修改東西
3. 刪除東西
4. 離開程式
請輸入你的選擇 (1-4)：4
再見！

"""

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
