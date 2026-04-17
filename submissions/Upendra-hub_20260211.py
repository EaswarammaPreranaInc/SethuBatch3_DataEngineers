Home work (11-02-2026)

a = "Rama Rao"
print(a)                 # Rama Rao
print(type(a))           # <class 'str'>
print(id(a))             # (some integer value which is memory address like “123456789” location)

b = 'Hyd'
print(b)                 # Hyd

c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)                 # Hyd is green city.
                        # Hyd is hitec city.
                        # Hyd is beautiful city.
a = 'Hyd'

print(a[0])              # H
print(a[1])              # y
print(a[2])              # d
print(a[3])              # IndexError

print(a[2])              # d
print(a[1])              # y
print(a[0])              # H

print(a[-4])             # IndexError
print(a[0] == a[-3])     # True

a[2] = 'c'               # TypeError (strings are immutable)

print(25[0])             # TypeError
print('25'[0])           # 2
print(True[1])           # TypeError
print('True'[1])         # r
a = 'Hyd'

print(a * 3)             # HydHydHyd
print(a * 2)             # HydHyd
print(a * 1)             # Hyd
print(a * 0)             # (empty string)
print(a * -1)            # (empty string)

print(25 * 3)            # 75
print('25' * 3)          # 252525
print('25' * 4.0)        # TypeError

print(3 * 'Hyd')         # HydHydHyd
print('25' * True)       # 25
a = 'Hyd'
print(a , id(a))         # Hyd (some id value)

a = a * 3                # Valid
print(a , id(a))         # HydHydHyd (different id value)
print(len('Hyd'))        # 3
print(len('Rama Rao'))   # 8
print(len('9247'))       # 4
print(len(''))           # 0
print(len(' '))          # 1
print(len(689))          # TypeError
a = """"Hyd"""
print(a)                 # "Hyd
print(len(a))            # 4
print(a[0])              # "

print("""Hyd"""")        # SyntaxError

b = """""Hyd"""
print(b)                 # ""Hyd
print(len(b))            # 5
a = 'Sankar Dayal Sarma'

print(a[7 : 12])         # Dayal
print(a[7 : ])           # Dayal Sarma
print(a[ : 6])           # Sankar
print(a[ : ])            # Sankar Dayal Sarma
print(a[:  : ])          # Sankar Dayal Sarma

print(a[1 : 10 : 2])     # akrDy
print(a[0 : : 2])        # SnkrDylSra
print(a[1 : : 2])        # aaaa arma
print(a[-5 : -1])        # Sarm
print(a[::-1])           # amraS layaD raknaS
print(a[-1:-5:-1])       # amra
print(a[ : : -2])        # ara aa knS
print(a[3 : -3])         # kar Dayal Sa
print(a[2 : -5])         # nkar Dayal 
print(a[-1:-5])          # (empty string)
print(a[3 : 3])          # (empty string)
a = 'A'

print(a[1])              # IndexError
print(a[1:])             # (empty string)