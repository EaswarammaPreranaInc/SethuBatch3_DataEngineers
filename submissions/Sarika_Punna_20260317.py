a=eval(input("Enter list"))
b=[]
c=[]
for i in a:
    if i[0] not in b:
        b.append(i[0])
for i in b:
    d=[]
    for j in a:
        if j.startswith(i):
            d.append(j)
    c.append(d)
print(c)
