a=[]
i=0
while True:
    a.append(int(input()))
    if a[i]==0:
        break
    i+=1
a.sort()
for i in range(len(a)):
    print(a[i])