a = ['Swathi', 'Anand', 'Srinivas', 'Zebra', 'King', 'Amar']
b = []
for name in a:
    if name[0] not in b:
        b.append(name[0])
c = []
for char in b:
    d = []
    for name in a:
        if name.startswith(char):
            d.append(name)
    c.append(d)
print(c)