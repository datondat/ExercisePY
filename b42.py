def giaithua(x):
    t=1
    while x>0:
        t=t*x
        x-=1
    return t
a=int(input())
print(giaithua(a))