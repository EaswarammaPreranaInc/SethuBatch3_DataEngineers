L = eval(input("Enter list of strings:  "))
b = []
for i in L:
    if i[0] not in b:
        b.append(i[0])
c = []
for x in b:
    d = []
    for y in L: 
        if y[0] == x:
            d.append(y)     
    c.append(d)
print(c)
