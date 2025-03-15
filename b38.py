a=[]
b=[]
c=[]
while True:
    x=input()
    if x=="": break
    x=int(x)
    if x<0: a.append(x)
    elif x==0: b.append(x)
    else: c.append(x)
z=[]
z=a+b+c
print(z)