n = eval(input("enter a list of string : "))
b = []
for i in n:
    if i[0] not in b:
        b.append(i[0])
c = []
d = []
for i in b:
    for j in n:
        if j.startswith(i):
            d.append(j)        
    c.append(d)
    d = []

print("Nested list output : " , c )