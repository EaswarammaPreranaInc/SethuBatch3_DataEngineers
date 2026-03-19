lst = list(eval(input("Enter the strings: ")))
result =  []
c=[]

for x in lst:
    if x[0] not in result:
        result.append(x[0])
for x in result:
    d=[]
    for y in lst:
        if x==y[0]:
            d.append(y)
    c.append(d)
print(c)
