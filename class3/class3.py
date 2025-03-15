# class3
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
