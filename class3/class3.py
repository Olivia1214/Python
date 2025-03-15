# try except
# 錯誤處理
try:
    # 嘗試執行可能會出錯的程式碼
    n = int(input("input a number:"))

except:
    # 如果有錯誤發生，執行這段的程式碼
    print("you should input a number")

else:
    # 如果沒有錯誤發生，執行這段的程式碼
    print(n + 1)


try:
    h = float(input("請輸入身高(公尺):"))
    w = float(input("請輸入體重(公斤):"))
    bmi = w / h**2
    print(f"你的BMI為:{bmi}")

except:
    print("請輸入有效的數字")

# 比較運算子
print(1 == 1)  # True,1等於1
print(1 != 1)  # False,1不等於1
print(1 > 1)  # False,1不大於1
print(1 < 1)  # False,1不小於1
print(1 >= 1)  # True,1大於等於1
print(1 <= 1)  # True,1小於等於1

# 邏輯運算子
# and 代表全部條件都要成立時才會回傳True
# or 代表只要有一條條件要成立就會回傳True
# not 代表將原本的布林值反轉

print(True and True)  # True, True和True
print(True and False)  # False, True和False
print(False and False)  # False, False和False
print(True or True)  # True, True或True
print(True or False)  # True, True或False
print(False or False)  # False, False或False
print(not True)  # False, not True
print(not False)  # True, not False

password = input("請輸入密碼:")
if password == "1214":
    print("歡迎光臨Olivia")
elif password == "0428":
    print("歡迎光臨Viola")
elif password == "0603":
    print("歡迎光臨Winston")
elif password == "0922":
    print("歡迎光臨Jennifer")
else:
    print("密碼錯誤")

# if elif else 是連續的判斷，只要有一個條件成立，後面的條件就不會執行
# if 一定要有，elif可以有多個但是選用，else只能有一個但是選用

grade = input("請輸入成績(EX:90-100):")
if grade == "90-100":
    print("你的成績為A")
elif grade == "80-89":
    print("你的成績為B")
elif grade == "70-79":
    print("你的成績為C")
elif grade == "60-69":
    print("你的成績為D")
else:
    print("你的成績為E")
