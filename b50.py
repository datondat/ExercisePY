from random import randint

def password():
    s=''
    x=int(input("số ký tự của mật khẩu: "))
    for i in range(x):
        c=randint(33,126)
        s=s+chr(c)
    print(s)
password()