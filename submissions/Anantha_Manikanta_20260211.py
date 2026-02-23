1) #  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) # Rama Rao
print(type(a)) # class <str>
print(id(a)) # 230440
b = 'Hyd'
print(b) # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # Hyd is green city.
           Hyd is hitech city.
           Hyd is beautiful city.

2) # Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a') # a[0]
print(How  to  print  'y'  of  object  'a') # a[1]
print(How  to  print  'd'  of  object  'a') # a[2]
print(a[3])                                 # Error because there are letters only upto 2nd index
print(How  to  print  'd'  of  object  'a') # a[-1]
print(How  to  print  'y'  of  object  'a') # a[-2]
print(How  to  print  'H'  of  object  'a') # a[-3]
print(a[-4]) # Error because there are letters only upto -3rd index
print(a[0] == a[-3]) # True
a[2] = 'c' 
print(25[0]) # Error because int cannot be used to access
print('25'[0]) # 2
print(True[1]) # Error because Boolean cannot be used to access
print('True'[1]) # T

3) #  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) # HydHydHyd
print(a * 2) # HydHyd
print(a * 1) # Hyd
print(a * 0) # Empty String ('')
print(a * -1) # Error because cant multiply the string -1 times
print(25 * 3) # 75
print('25' * 3) # 252525
print('25' * 4.0) # Error because cannot multiply the string with float
print(3 * 'Hyd') # HydHydHyd
print('25' * True) # 25

4) # Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a)) # Hyd 1200
a = a * 3  #  It  is  valid  (or)  invalid # Itis Valid
print(a , id(a)) # HydHydHyd 1500

5) # len()  function  (Home  work)
print(len('Hyd')) # 3
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('')) # 0
print(len(' '))# 1
print(len(689)) # 3

6) # Find  outputs  (Home  work)
a = """"Hyd"""
print(a) # Hyd
print(len(a)) # 3
print(a[0]) # H
print("""Hyd"""") # Hyd
b = """""Hyd"""
print(b)  # Error
print(len(b)) # Error

7) # Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) # Dayal
print(a[7 : ]) # Dayal Sarma
print(a[ : 6]) # Sankar
print(a[ : ]) # Sankar Dayal Sarma
print(a[:  : ]) # Sankar Dayal Sarma
print(a[1 : 10 : 2])  # akrDy
print(a[0 : : 2]) # Sna aa am
print(a[1 : : 2]) # akrylSra
print(a[-5 : -1]) # Sarm
print(a[::-1])  # amraS layaD raknaS
print(a[-1:-5:-1]) # amra
print(a[ : : -2]) # arSla rnkS
print(a[3 : -3]) # kar Dayal Sa
print(a[2 : -5]) # nkar Dayal
print(a[-1:-5]) # amras
print(a[3 : 3]) # Empty String

8) #  Find  outputs  (Home  work)
a =  'A'
print(a[1]) # Error
print(a[1:]) # Error