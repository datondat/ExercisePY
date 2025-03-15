def perfect(a):
    s=0
    for i in range(1,int(a/2)+1):
        if a%i==0:
            s=s+i
    if s==a: return True
    else : return False
for i in range(1,10000):
    if perfect(i):
        print(i,end='  ')