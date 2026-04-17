s = input('Enter String :')
vowels = set()

for ch in s:
    if ch.lower() in 'aeiou':
        vowels.add(ch.upper())

result = ''.join(vowels)
print(result)

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}

print(a['Empno'])
print(a['Ename'])
print(a['Sal'])

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}

print(a)
print(id(a))

a['Sal'] = 2000
a['Ename'] = 'Sita'
a['Empno'] = 35

print(a)
print(id(a))

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
a['Gender'] = 'M'
a['Married'] = True

print(a)

a = {}

a[10] = 'Rama'
a[20] = 'Sita'
a[15] = 'Rajesh'
a[18] = 'Kiran'

print(a)

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
# del a['Sal']
a.pop('Sal')
print(a)

a = {10: 20, 30: 40, 50: 60, 70: 80}

print(30 in a.keys())
print(60 in a.keys())
print(60 in a.values())
print(30 in a.values())
print(50 in a)
print(20 in a)
print(70 not in a.keys())
print(40 not in a.values())
print(25 not in a)

a = input('Enter dictionary: ')
print(a)
print(type(a))

b = eval(a)
print(b)
print(type(b))


a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}

b = {**a}
print(b)
print(a is b)
print(a == b)

c = a
print(a is c)
print(a == c)

a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh'}
b = {18: 'Kiran', 14: 'Amar', 20: 'Manohar'}
c = {25: 'Ramesh', 19: 'Krishna', 15: 'Radha', 14: 'Srinivas'}

d = {*a, *b, *c}
print(d)
print(type(d))

e = {**a, **b, **c}
print(e)
print(type(e))

f = a | b | c
print(f)

a = {}

n = int(input('Enter number of employees: '))

for i in range(n):
    name = input('Enter name: ')
    sal = float(input('Enter salary: '))
    a[name] = sal

print(a)


s = input('Enter string: ')

parts = s.split(',')
a = {}

for item in parts:
    key, value = item.split('=')
    a[key.strip()] = value.strip()

print(a)
