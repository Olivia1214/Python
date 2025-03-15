try:
    h = float(input("請輸入身高(公尺):"))
    w = float(input("請輸入體重(公斤):"))
    bmi = w / h**2
    print(f"你的BMI為:{bmi}")

except:
    print("請輸入有效的數字")
