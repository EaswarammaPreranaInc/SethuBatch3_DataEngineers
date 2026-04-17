a = ['Swathi', 'Anand', 'Srinivas', 'Zebra', 'King', 'Amar']
b = []   # unique first letters
c = []   # final nested list
for i in a:
    if i[0] not in b:
        b.append(i[0])
for ch in b:
    d = []
    for i in a:
        if i[0] == ch:
            d.append(i)
    c.append(d)
print(c)