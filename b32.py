x=int(input("1.dịch \n2.giải\n"))
if x==1:
    s=input("nhập vào đây:")
    s1=""
    for i in range(len(s)):
        if (ord(s[i])>64) and (ord(s[i])<91):
            if ord(s[i])+3>90:
                s1=s1+chr(ord(s[i])+3-26)
            else: s1=s1+chr(ord(s[i])+3)
        elif (ord(s[i])>96) and (ord(s[i])<123):
            if ord(s[i])+3>123:
                s1=s1+chr(ord(s[i])+3-26)
            else: s1=s1+chr(ord(s[i])+3)
        else: s1=s1+s[i]
    print(s1)
else:
    s = input("nhập vào đây:")
    s1 = ""
    for i in range(len(s)):
        if (ord(s[i]) > 64) and (ord(s[i]) < 91):
            if ord(s[i]) - 3 < 65:
                s1 = s1 + chr(ord(s[i]) - 3 + 26)
            else:
                s1 = s1 + chr(ord(s[i]) - 3)
        elif (ord(s[i]) > 96) and (ord(s[i]) < 123):
            if ord(s[i]) - 3 <97:
                s1 = s1 + chr(ord(s[i]) - 3 + 26)
            else:
                s1 = s1 + chr(ord(s[i]) - 3)
        else:s1=s1+s[i]
    print(s1)