#  Find  outputs  (Home  work)

a = "Rama Rao"
print(a)                 # Rama Rao
print(type(a))           # <class 'str'>
print(id(a))             # address of object str

b = 'Hyd'
print(b)                 # Hyd

c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)
# Hyd is green city.
# Hyd is hitec city.
# Hyd is beautiful city.


# Index demo program (Home work)

a = 'Hyd'
print(a[0])              # H
print(a[1])              # y
print(a[2])              # d
print(a[3])              # Error: index out of range

print(a[-1])             # d
print(a[-2])             # y
print(a[-3])             # H
print(a[-4])             # Error: index out of range

print(a[0] == a[-3])     # True

a[2] = 'c'               # Error: strings are immutable

print(25[0])             # Error
print('25'[0])           # 2
print(True[1])           # Error
print('True'[1])         # r


#  Find outputs (Home work)

a = 'Hyd'
print(a * 3)             # HydHydHyd
print(a * 2)             # HydHyd
print(a * 1)             # Hyd
print(a * 0)             # empty string
print(a * -1)            # empty string

print(25 * 3)            # 75
print('25' * 3)          # 252525
print('25' * 4.0)        # Error

print(3 * 'Hyd')         # HydHydHyd
print('25' * True)       # 25


# Tricky program
# Find outputs (Home work)

a = 'Hyd'
print(a, id(a))          # Hyd and address of str

a = a * 3                # valid
print(a, id(a))          # new object address


# len() function (Home work)

print(len('Hyd'))        # 3
print(len('Rama Rao'))   # 8
print(len('9247'))       # 4
print(len(''))           # 0
print(len(' '))          # 1
print(len(689))          # Error


# Find outputs (Home work)

a = """"Hyd"""
print(a)                 # "Hyd
print(len(a))            # 4
print(a[0])              # "

print("""Hyd"""")        #Error

b = """""Hyd"""
print(b)                 # ""Hyd
print(len(b))            # 5


# Find outputs

a = 'Sankar Dayal Sarma'

print(a[7:12])           # Dayal
print(a[7:])             # Dayal Sarma
print(a[:6])             # Sankar
print(a[:])              # Sankar Dayal Sarma
print(a[::])             # Sankar Dayal Sarma

print(a[1:10:2])         # akrD
print(a[0::2])           # 0 to end, step 2
print(a[1::2])           # 1 to end, step 2

print(a[-5:-1])          # arma
print(a[::-1])           # reverse string
print(a[-1:-5:-1])       # amra
print(a[::-2])           # reverse with step 2

print(a[3:-3])           # kar Dayal Sa
print(a[2:-5])           # nkar Dayal
print(a[-1:-5])          # empty string
print(a[3:3])            # empty string


# Find outputs (Home work)

a = 'A'
print(a[1])              # Error
print(a[1:])             # empty string