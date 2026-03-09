a=input("enter the input:")
b=['A','E','I','O','U']
a=a.upper()
c=""
for i in a:
    if i in b and i not in c:
        c+=i
print(c)