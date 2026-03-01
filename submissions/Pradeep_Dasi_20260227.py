units = int(input('Enter  units :   '))   #   175

match units // 100:
    case 0:   # 0 - 99
        cost = units * 3.00
    case 1:   # 100 - 199
        cost = 100 * 3.00 + (units - 100) * 3.50
    case 2 | 3:   # 200 - 399
        cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
    case 4 | 5 | 6:   # 400 - 699
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
    case _:   # >= 700
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00

print('Bill  amount  :  ' , cost)



x = 10
a = 0
b = 1
i = 1

while i <= x - 2:
    print(a, end=' , ')
    c = a + b
    a = b
    b = c
    i += 1

print(a, end=' , ')
print(b)   # 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13


for x in [10, 20, 15, 18]:
    print(x)
# 10
# 20
# 15
# 18

for x in 'Hyd':
    print(x)
# H
# y
# d


for x in range(5):
    print(x)
# 0
# 1
# 2
# 3
# 4



for x in {10:20,30:40,50:60}.keys():
    print(x)
# 10
# 30
# 50

for x in {10:20,30:40,50:60}.values():
    print(x)
# 20
# 40
# 60


for x in {10:20,30:40,50:60}.items():
    print(x)
# (10, 20)
# (30, 40)
# (50, 60)


for x in {10:20,30:40,50:60}:
    print(x)
# 10
# 30
# 50

a = {10:20,30:40,50:60}
for x,y in a.items():
    print(x,y,sep='...')
# 10...20
# 30...40
# 50...60


for x,y in a:
    print(x,y)		# Error



for x,y in {10:20,30:40,50:60}:
    print(x,y,sep='...')	# Error


for x in 123:
    print(x)		# Error due to no sequence


for x in ():
    print(x)

for x in []:
    print(x)


for x in {}:
    print(x)


for x in set():
    print(x)


for x in '':
    print(x)

for x in range(10,10):
    print(x)

for x in range():
    print(x)		# Error due to no arguments in range


for x in (25):
    print(x)		# Error due to no sequence



for i in range(1,4):
    for j in range(1,5):
        print(i,j)
    print('Hello')
print('Bye')

#output: 
#1 1
#1 2
#1 3
#1 4
#Hello
#2 1
#2 2
#2 3
#2 4
#Hello
#3 1
#3 2
#3 3
#3 4
#Hello
#Bye



a = [25 , 10.8 , 'Hyd' , True]

print('Indexed  based  for loop')
for i in range(len(a)):
    print(i, a[i])



print('For each loop')
for x in a:
    print(a.index(x), x)



a = [25 , 10.8 , 'Hyd' , True]

print('Indexed for loop')
for i in range(len(a)-1, -1, -1):
    print(a[i])



for x in reversed(a):
    print(x)



a = [10 , 20 , 15 , 18]
b = [30 , 40 , 35 , 12 , 100 , 200 , 300]
c = []

for i in range(min(len(a), len(b))):
    c.append(a[i] + b[i])

print('3rd  list : ' , c)   # [40, 60, 50, 30]



c = []
for x in a:
    c.append(x + b[a.index(x)])

print('3rd  list : ' , c)   # [40, 60, 50, 30]



a = [25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Sec']

for i in range(2,5):
    print(a[i])
# Hyd
# True
# (3+4j)


a = [10 , 20 , 15 , 18]
for i in range(len(a)):
    a[i] += 1
print('a :  ' , a)   # a :   [11, 21, 16, 19]



b = [10 , 20 , 15 , 18]
for x in b:
    x += 1
print('b :  ' ,  b)   # b :   [10, 20, 15, 18]



n = 5
for i in range(1, n+1):
    print(' '*(n-i) + '*'*(2*i-1))



i = 1
while i <= 20:
    print(2*i, end=' , ')
    i += 1
# 2 , 4 , 6 , ... , 40




i = 1
while i <= 20:
    print(2*i-1, end=' , ')
    i += 1
# 1 , 3 , 5 , ... , 39


n = int(input('Enter n : '))
i = 1
while i <= n:
    print(i)
    i += 1


i = 10
while i >= 1:
    print(i)
    i -= 1


n = 5
s = 0
for i in range(1,n+1):
    s += 1.1*i
print(s)



s = 0
for i in range(1,21):
    s += 2*i
print(s)   # 420


s = 0
for i in range(1,21):
    s += 2*i - 1
print(s)   # 400


n = 5
s = 0
for i in range(1,n+1):
    s += i
print(s)   # 15

#output:
#1
#Sec
#Hello
#2
#Sec
#Hello
#3
#4
#Sec
#Hello
#5
#Sec
#Hello
#6
#7
#Sec
#Hello
#Outside loop



if ():
    print('Hyd')
    continue
    print('Sec')	# SyntaxError the continue should be outside
#output: 
#1
#Sec
#Hello
#2
#Sec
#Hello
#3
#Outside loop



if (10,20,30):
    print('Hyd')
    break
    print('Sec')	# SyntaxError 'break' should be outside loop