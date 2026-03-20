Name-Dhruva Gupta
Roll Number-D238

a = ['Swathi', 'Anand', 'Srinivas', 'Zebra', 'King', 'Amar']
b = [] 
for name in a:
    first = name[0]
    if first not in b:
        b.append(first)
c = []
for letter in b:
    d = []
    for name in a:
        if name[0] == letter:
            d.append(name)
    c.append(d)
print(c)