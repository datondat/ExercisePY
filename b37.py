a=[]
i=0
while True:
    a.append(input())
    if a.count(a[i])>1:a[i]=""
    if(a[i])==" ":
        break
    i+=1
for i in range(len(a)):
    if a[i]!="":
        print(a[i])