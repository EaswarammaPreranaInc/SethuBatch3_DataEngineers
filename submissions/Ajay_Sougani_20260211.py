
#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) # Rama Rao
print(type(a)) # <class ‘str’>
print(id(a)) # Address of Object a
b = 'Hyd'
print(b) # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)  ‘’’ Hyd is green city.
                 Hyd is hitec city.
	   Hyd is beautiful city.’’’

# Index   demo  program  a = 'Hyd'
print(How  to  print  'H'  of  object  'a') # a[0]
print(How  to  print  'y'  of  object  'a') # a[1]
print(How  to  print  'd'  of  object  'a') # a[2]
print(a[3])  # Error string index out of range
print(How  to  print  'd'  of  object  'a') # a[-3]
print(How  to  print  'y'  of  object  'a') # a[-2]
print(How  to  print  'H'  of  object  'a') # a[-1]
print(a[-4]) # Error String index out of range
print(a[0] == a[-3]) # False
a[2] = 'c'  # 'str' object does not support item assignment
print(25[0])   # 'int' object is not subscriptable
print('25'[0]) # 2
print(True[1])  # 'bool' object is not subscriptable
print('True'[1]) # r
#  Find  outputs  a = 'Hyd'
print(a * 3) # ‘HydHydHyd’
print(a * 2) # ‘HydHyd’
print(a * 1) # ‘Hyd’
print(a * 0) # ‘’
print(a * -1) # 
print(25 * 3) # 75
print('25' * 3) # ‘252525’
print('25' * 4.0)  # can't multiply sequence by non-int of type 'float'
print(3 * 'Hyd') # ‘HydHydHyd’
print('25' * True) # 25

# Tricky  program
#  Find  outputs  a = 'Hyd'
print(a , id(a)) # ‘Hyd’  # Address of object a
a = a * 3  #  valid
print(a , id(a)) # ‘HydHydHyd’  # Address of object a
 
# len()  function  
print(len('Hyd')) # 3
print(len('Rama Rao')) #8
print(len('9247')) # 4
print(len('')) # 0
print(len(' ')) # 1
print(len(689)) # Error ‘object of type 'int' has no len()’
 
# Find  outputs  
a = """"Hyd"""
print(a) # “Hyd
print(len(a)) # 4
print(a[0]) # “
print("""Hyd"""")   # Error
b = """""Hyd"""
print(b)  # “”Hyd
print(len(b)) # 5

# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) #  Dayal
print(a[7 : ])  #  Dayal Sarma
print(a[ : 6])   # Sankar
print(a[ : ])  # Sankar Dayal Sarma
print(a[:  : ])  # Sankar Dayal Sarma
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2])  # Sna aa am
print(a[1 : : 2])  # akrDylSra
print(a[-5 : -1]) # Sarm
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string # amraS layaD raknaS
print(a[-1:-5:-1]) # amra
print(a[ : : -2])  # arSlyDrka
print(a[3 : -3]) # kar Dayal Sa
print(a[2 : -5]) # nkar Dayal 
print(a[-1:-5]) # prints Nothing
print(a[3 : 3]) #  prints Nothing



#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1
#  Find  outputs  
a =  'A' 
print(a[1]) # string index out of range
print(a[1:]) # prints Nothing

