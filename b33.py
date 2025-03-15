s= input("nhập chuỗi vô đây:")
x=len(s)-1
d=0
i=0
for i in range(int(len(s)/2)):
    if s[i]==s[x]:
        d=d+1
        x=x-1
    else:
        print("không phải palindrome")
        break
if d==int(len(s)/2):
    print("là palindrome")