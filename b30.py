y= int(input("nhập năm:"))
if y%400==0 or (y%4==0 and y%100!=0):
    print("là năm nhuận")
else: print("không phải năm nhuận")