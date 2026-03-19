
a = ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar']

b = []   # stores unique first letters (order preserved)

# Step 1: collect unique first letters
for i in range(len(a)):
    ch = a[i][0]
    if ch not in b:
        b.append(ch)

# Step 2: group elements
c = []

for i in range(len(b)):
    d = []
    for j in range(len(a)):
        if a[j][0] == b[i]:
            d.append(a[j])
    c.append(d)

print(c)