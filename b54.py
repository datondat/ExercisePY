def noi(a):
    p=a[0]
    for i in range(len(s)):
        if i==len(s)-1:p+=" and "+ s[i]
        elif i>0:p+= ", " +s[i]
    return p
s=[]
while True:
    x= input()
    if x=="":
        break
    s.append(x)
print(noi(s))