"""
請使用者輸入身高(公尺)h以及體重(公斤)w
透過下面公式計算出BMI數值並顯示計算結果
bmi = w/h**2
EX:
請輸入身高:1.7
請輸入體重:50
你的BMI為17.301038062283737
"""

r = input("請輸入身高(公尺):")
r = float(r)
w = input("請輸入體重(公斤):")
w = float(w)
bmi = w / r**2
print("你的BMI為" + str(bmi))
if bmi >= 14.8 and bmi <= 20.7:
    print("體重正常")
elif bmi < 14.8:
    print("體重過輕")
else:
    print("體重過重")
