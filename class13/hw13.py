# 水果店價格查詢系統
# 1. 顯示所有水果名稱和價格
# 2. 顯示功能 : 新增水果, 修改水果, 刪除水果, 離開系統
# 3. 選擇功能
# 4. 新增水果 : 輸入水果名稱和價格, 並新增至水果清單內
# 6. 修改水果 : 輸入水果名稱和價格
# 7. 刪除水果 : 輸入水果名稱
# 8. 離開系統
# (皆須顯示水果名稱和價格)

print("=== 水果店價格查詢系統 ===")

fruits = {"蘋果": 10, "香蕉": 20, "橘子": 30}
print(fruits)

while True:
    print("請選擇一個功能")
    print("1. 新增水果")
    print("2. 修改水果")
    print("3. 刪除水果")
    print("4. 離開系統")
    choice = input("請選擇一個功能(1-4): ")
    if choice == "1":
        print("請輸入水果名稱和價格")
        name = input("請輸入水果名稱: ")
        price = input("請輸入水果價格: ")
        fruits[name] = int(price)
        print(f"新增水果 {name} 成功")
        print(fruits)
    elif choice == "2":
        print("請輸入水果名稱")
        name = input("請輸入水果名稱: ")
        if name in fruits:
            price = input("請輸入水果價格: ")
            fruits[name] = int(price)
            print(f"修改水果 {name} 成功")
            print(fruits)
        else:
            print("此水果不存在")
    elif choice == "3":
        print("請輸入水果名稱")
        name = input("請輸入水果名稱: ")
        if name in fruits:
            del fruits[name]
            print(f"刪除水果 {name} 成功")
            print(fruits)
        else:
            print("此水果不存在")
    elif choice == "4":
        print("再見!")
        break
    else:
        print("請輸入有效的功能")
