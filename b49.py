def prime(x):
    if x<2:
        return False
    else:
        for i in range(2,int(x**0.5)):
            if x%i==0: return False
    return True
a=int(input())
if prime(a):
    print("là số nguyên tố")
else:
    print("không là số nguyên tố")