a = "Rama Rao"
print(a)            # Rama Rao
print(type(a))      # <class 'str'>
print(id(a))        # Some address (suppose 1000)

b = 'Hyd'
print(b)            # Hyd

c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)
# Hyd is green city.
# Hyd is hitec city.
# Hyd is beautiful city.

***

a = 'Hyd'

print(a[0])      # H
print(a[1])      # y
print(a[2])      # d

print(a[3])      # Error (index out of range)

print(a[2])      # d
print(a[1])      # y
print(a[0])      # H

print(a[-4])     # Error (index out of range)

print(a[0] == a[-3])   # True

a[2] = 'c'      # Error (string is immutable)

print(25[0])     # Error (int is not subscriptable)
print('25'[0])   # 2
print(True[1])   # Error (bool not subscriptable)
print('True'[1]) # r

***

a = 'Hyd'

print(a * 3)     # HydHydHyd
print(a * 2)     # HydHyd
print(a * 1)     # Hyd
print(a * 0)     # (empty string)
print(a * -1)    # (empty string)

print(25 * 3)    # 75
print('25' * 3)  # 252525
print('25' * 4.0) # Error (cannot multiply by float)

print(3 * 'Hyd') # HydHydHyd
print('25' * True)  # 25

***

a = 'Hyd'
print(a , id(a))   # Hyd  Some address (1000)

a = a * 3          # Valid
print(a , id(a))   # HydHydHyd  New address (2000)

***


print(len('Hyd'))       # 3
print(len('Rama Rao'))  # 8
print(len('9247'))      # 4
print(len(''))          # 0
print(len(' '))         # 1
print(len(689))         # Error (int has no length)

***


a = """"Hyd"""
print(a)        # "Hyd
print(len(a))   # 4
print(a[0])     # "

print("""Hyd"""")   # Error (invalid syntax)

b = """""Hyd"""
print(b)        # ""Hyd
pri

nt(len(b))   # 5

***

a = 'Sankar Dayal Sarma'

print(a[7 : 12])   # Dayal
print(a[7 : ])     # Dayal Sarma
print(a[ : 6])     # Sankar
print(a[ : ])      # Sankar Dayal Sarma
print(a[: : ])     # Sankar Dayal Sarma

print(a[1 : 10 : 2])  # akrDy
print(a[0 : : 2])     # Sna aaalSra
print(a[1 : : 2])     # akrDylSrm

print(a[-5 : -1])     # Sarm
print(a[::-1])        # amraS layaD raknaS
print(a[-1:-5:-1])    # amra
print(a[: : -2])      # arSlaa ankS

print(a[3 : -3])      # kar Dayal Sa
print(a[2 : -5])      # nkar Dayal
print(a[-1:-5])       # (empty string)
print(a[3 : 3])       # (empty string)

***

a = 'A'

print(a[1])     # Error (index out of range)
print(a[1:])    # (empty string)