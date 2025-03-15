a= int(input("nhập cạnh thứ nhất:"))
b= int (input("nhập cạnh thứ hai:"))
c= int(input("nhập cạnh thứ ba:"))
if a+b>c or a+c>b or b+c>a:
    if a*a+b*b==c*c or a*a+c*c==b*b or a*a==b*b+c*c:
        print("tam giác vuông")
    elif (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
        print("tam giác cân")
    elif a==b==c :
        print("tam giác đều")
    else: print("tam giác thường")
else:print("không phải tam giác")