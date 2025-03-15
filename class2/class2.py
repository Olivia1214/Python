# 字串運算
a = "hello"
b = "world"
c = a + " " + b  # 字串相加
print(c)

a = a * 3  # 字串乘法
print(a)

# 認識基本指令
# 指令會有名稱跟括號組成，()裡面放提供給指令的參數
# 每個參數都要用逗號分隔
m = max(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # 取最大值
print(m)

le = len("hello")  # 取字串長度
print(le)

# type()取得參數的型態
print(type(1))  # 取型態
print(type("hello"))  # 取型態
print(type(1.0))  # 取型態
print(type(True))  # 取型態

# 型態轉換
# int()轉換成整數
# float()轉換成浮點數
# str()轉換成字串
# bool()轉換成布林值

print(int("123"))  # 123
print(int(123.9999))  # 123
print(int(True))  # 1
print(int(False))  # 0
print("------------------------")

print(float("123.456"))  # 123.456
print(float(123))  # 123.0
print(float(True))  # 1.0
print(float(False))  # 0.0
print("------------------------")

print(str(123))  # "123"
print(str(123.456))  # "123.456"
print(str(True))  # "True"
print(str(False))  # "False"
print("------------------------")

print(bool(123))  # True
print(bool(0))  # False
print(bool(" "))  # False
print(bool("0"))  # True
print(bool(-1))  # True

# input()讓使用者在終端機輸入資料
# input()的括弧內可以放入"提示字串"
a = input("請輸入數字:")
# 透過input()輸入的資料都是字串
print(a + "1")  # 字串相加
print(int(a) * 30)  # 將字串轉換成整數再相加

# 運算子
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1 // 1)  # 取商
print(1 % 1)  # 取餘數
print(2**3)  # 次方

# 優先順序
# 1. ()括號
# 2. **次方
# 3. */ // % 乘 除 取商 取餘數
# 4. + - 加 減

# 正方形面積計算
r = input("請輸入正方形的邊長:")
r = int(r)  # 將字串轉換成整數
area = r * r  # 計算面積
print(f"正方形的面積為:{area}")  # 印出面積
