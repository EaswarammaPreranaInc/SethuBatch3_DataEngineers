
#----- String Object Demo -----

a="Rama Rao"
print(a) # Rama Rao
print(type(a)) # <class 'str'>
print(id(a)) # 5000
b='Hyd'
print(b) # Hyd
c='''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # Hyd is green city.
         # Hyd is hitec city.
         # Hyd is beautiful city.

#----- Index Demo -----

a='Hyd'
print(a[0]) # H
print(a[1]) # y
print(a[2]) # d
#print(a[3]) # Error (index 3 does not exist)
print(a[-1]) # d
print(a[-2]) # y
print(a[-3]) # H
#print(a[-4]) # Error (negative index exceeds length)
print(a[0]==a[-3]) # True
#a[2]='c' # Error (string cannot be modified)
#print(25[0]) # Error (number does not support indexing)
print('25'[0]) # 2
#print(True[1]) # Error (boolean cannot be indexed)
print('True'[1]) # r

#----- String Multiplication -----

a='Hyd'
print(a*3) # HydHydHyd
print(a*2) # HydHyd
print(a*1) # Hyd
print(a*0) # 0
print(a*-1) 
print(25*3) # 75
print('25'*3) # 252525
#print('25'*4.0) # Error (string cannot be multiplied by float)
print(3*'Hyd') # HydHydHyd
print('25'*True) # 25 (True acts like 1)

#----- Tricky Program -----

a='Hyd'
print(a,id(a)) # Hyd 5000
a=a*3
print(a,id(a)) # HydHydHyd 5001 (new string created so id changes)

#----- len() Function -----

print(len('Hyd')) # 3
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('')) # 0
print(len(' ')) # 1
#print(len(689)) # Error (len() works only for strings or collections, not numbers)

#----- Triple Quote Case -----

#a=""""Hyd""" # Error (quotes are not arranged correctly)
#print(a) # Error (a was not created)
#print(len(a)) # Error (a is not defined or created)
#print(a[0]) # Error (a does not exist)
#print("""Hyd"""") # Error (extra double quote at the end)
#b="""""Hyd""" # Error (incorrect number of double quotes)
#print(b) # Error (b is not properly formed)
#print(len(b)) # Error (b is invalid)

#----- Slicing Demo -----

a='Sankar Dayal Sarma'
print(a[7:12]) # Dayal
print(a[7:]) # Dayal Sarma
print(a[:6]) # Sankar
print(a[:]) # Sankar Dayal Sarma
print(a[::]) # Sankar Dayal Sarma
print(a[1:10:2]) # akrDy
print(a[0::2]) # SnkrDylSra
print(a[1::2]) # aa ayaama
print(a[-5:-1]) # arma
print(a[::-1]) # amraS layaD raknaS
print(a[-1:-5:-1]) # amra
print(a[::-2]) # arSlayDknS
print(a[3:-3]) # kar Dayal Sa
print(a[2:-5]) # nkar Dayal
print(a[-1:-5]) # '' (start index is greater than stop)
print(a[3:3]) # '' (start and stop are same)

#----- Single Character Case -----

a='A'
#print(a[1]) # Error (only index 0 is available)
print(a[1:]) # ''