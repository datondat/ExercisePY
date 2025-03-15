def check(s):
    a=0
    b=0
    c=0
    for i in range(len(s)):
        if ord(s[i]) in range(65,91):a=a+1
        elif ord(s[i]) in range(97,123):b=b+1
        elif ord(s[i]) in range(48,58):c=c+1
    if (a>0) and (b>0) and (c>0):
        return True
    else: return False
x=""
while len(x)<8:
    x=input()
if check(x):
    print("Mạnh")
else: print("yếu")