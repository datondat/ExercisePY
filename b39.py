a=[]
n=int(input())
for i in range(0,n):
    a.append([])
    for j in range(2):
        a[i].append(pow(i+1,j+1))
print(a)