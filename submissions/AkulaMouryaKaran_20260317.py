a = ['Swathi', 'Anand', 'Srinivas', 'Zebra', 'King', 'Amar']
b = []
c = []

for x in a:
    if x[0] not in b:
        b.append(x[0])

print(b)

for y in b:
    c.append([])
    for x in a:
        if x[0] == y:
            c[-1].append(x)
print(c)
