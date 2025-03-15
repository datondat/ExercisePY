a= int(input("nhập tại đây:"))
s=''
while a>0:
    if a%2==0:
        s=s+'0'
        a=a/2
    else:
        s=s+'1'
        a=int(a/2)
while len(s)<8:
    s=s+'0'
print(s[::-1])