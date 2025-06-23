# 字典 (Dictionary) 用來儲存 [key-value] 配對的資料結構
# 字典很適合用來表示有對應關係的資料, 像是商品和價格的對應

# 建立字典 使用大括號 {} , key 和 value 之間用冒號 : 隔開
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(d)

# 從字典中取得特定 key 對應的 value
# 如果 key 不存在會產生 KeyError 錯誤
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(d["蘋果"])
# print(d["梨子"])  # 會產生 KeyError '梨子' 錯誤

# 方式一 : 直接遍歷字典, 會取得所有 key
for key in d:
    print(key)  # 印出 key 名稱
    print(d[key])  # 用 key 取得對應的 value

# 方式二 : 明確使用 keys() 方法來取得所有 key
for key in d.keys():
    print(key)  # 印出 key 名稱
    print(d[key])  # 用 key 取得對應的 value

# 方式三 : 使用 values() 方法來取得所有 value
for value in d.values():
    print(value)  # 印出 value 值, 不會印出 key 名稱

# 方式四 : 使用 items() 方法來取得所有 key-value 配對
for key, value in d.items():
    print(f"{key} : {value}")  # 印出 key 名稱和 value 值的配對關係

# 新增 / 修改 字典的內容
# 直接指定 key 對應的 value , 如果 key 已經存在就是修改, 如果 key 不存在則是新增
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
d["蘋果"] = 10  # 修改 [蘋果] 對應的 value
print(d)
d["蓮霧"] = 15  # 新增一個 key-value 配對
print(d)

# 刪除字典的內容
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
d.pop("蘋果")  # 刪除蘋果
# 如果要刪除的 key 不存在會產生 KeyError 錯誤, 所以可以加上第二個參數
popitem = d.pop("蓮霧", "不存在這筆資料")  # 不會有任何變化
print(d)  # {'香蕉': 30, '橘子': 25}
print(popitem)  # 不存在這筆資料

# len 取得字典中有多少組 key-value 配對
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(len(d))

# 檢查某個 key 是否存在於字典中
# 使用前先檢查可以避免 KeyError 錯誤
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print("蘋果" in d)  # True, 存在
print("蓮霧" in d)  # False, 不存在

# 檢查某個元素有沒有在 list 中
# 使用 in 可以快速檢查某個元素是否存在於 list 中
L = [1, 2, 3, 4, 5]
print(3 in L)  # True
