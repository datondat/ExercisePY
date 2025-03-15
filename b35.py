a = []
n = int(input("nhập số phần tử của dãy:"))
for i in range(n):
    a.append(int(input("nhập vào phần tử thứ "+ str(i+1)+": ")))

for i in range(n):
    if(a[i])%2==1:
        print(a[i])