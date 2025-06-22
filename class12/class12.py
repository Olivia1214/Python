# index 尋找指定元素在 List 中第一次出現的位置
# 如果元素不存在會產生錯誤, 所以使用前先檢查元素是否存在\
L = [1, 3, 2, 4, 5]
print(L.index(3))  # 找到數字 3 在索引位置 1

# count 統計某個元素在 List 中出現的次數
# 適合用來檢查重複資料
L = ["Hello", "World", "Python", "Hello"]
print(L.count("Hello"))  # 找到字串 "Hello" 出現2次

# sort 將 List 中的元素進行排序, 預設事由小到大(升序排列)
# 注意 : 這個方法會直接修改原本的 List, 不會產生新的 List
L = [1, 3, 2, 4, 5]
L.sort()
print(L)  # [1, 2, 3, 4, 5]

# sort(reverse=True) 將 List 中的元素由大到小(降序排列)
# reverse=True 參數可以讓排序結果相反
L = [1, 3, 2, 4, 5]
L.sort(reverse=True)
print(L)  # [5, 4, 3, 2, 1]

# reverse 將 List 中元素的順序完全顛倒
# 不是排序, 只是將元素的順序完全顛倒
L = [1, 3, 2, 4, 5]
L.reverse()
print(L)

# List 和字串有很多相似的操作方式
# 我們可以像操作字串一樣使用 List

# 合併兩個 List : 使用 + 運算子江兩個 List 連接在一起
# 會產生全新的 List, 不會修改原本的 List
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2  # 把 L1 和 L2 合併成一個全新的 List
print(L3)  # [1, 2, 3, 4, 5, 6]

# 重複 List 中的內容 : 使用 * 運算子讓 List 內容重複多次
# 這在需要建立重複資料時很有用
L = [1, 2, 3]
L = L * 3  # 重複 L 中的內容 3 次
print(L)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 不同資料型態之間的轉換
print(range(10))  # range 物件本身看不到具體內容, 只是一個範圍描述
print(list(range(10)))  # 將 range 物件轉換成 List
print(list("Hello"))  # 將字串轉換成 List, 每個字元都會變成獨立的元素

# split 將字串分割成 List
# 處理文字資料時很常用
s = "Hello World"
L = s.split("")  # 以空白字元分割
print(L)
calendar = "2020/12/25"
L = calendar.split("/")  # 以 "/" 分割日期字串
print(L)

# join 將 List 中的多個元素合併成一個完整的字串
# 可指定連接符號
L = ["Hello", "World"]
s = " ".join(L)  # 將 List 中的元素合併成一個字串, 以空白字元連接
print(s)

birthday = "2012/12/14"
birthday = birthday.split("/")
birthday = "-".join(birthday)
print(birthday)
