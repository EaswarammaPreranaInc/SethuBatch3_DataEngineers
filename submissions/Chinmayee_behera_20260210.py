#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) #Rama Rao
print(type(a)) #<class 'str'>
print(id(a)) # Address of object 'Rama Rao'
b = 'Hyd'
print(b) #HYD
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # Hyd is green city.
           Hyd is hitec city.
           Hyd is beautiful city.

# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a') # character at 'H' a[0]
print(How  to  print  'y'  of  object  'a') # character at 'y' a[1]
print(How  to  print  'd'  of  object  'a') # character at 'd' a[2] 
print(a[3])  # Error due to invalid indexes range
print(How  to  print  'd'  of  object  'a') # character at 'd' a[-1]
print(How  to  print  'y'  of  object  'a') # character at 'y' a[-2]
print(How  to  print  'H'  of  object  'a') # character at 'H' a[-3]
print(a[-4]) # Error due to invalid indexes range
print(a[0] == a[-3]) # character 'H'
a[2] = 'c' # Error due to invalid character
print(25[0])   # invalid
print('25'[0]) # character 2 
print(True[1]) # invalid 
print('True'[1]) #character 'r'

#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) #'HydHydHyd'
print(a * 2) # 'HydHyd'
print(a * 1) # 'Hyd'
print(a * 0) # empty
print(a * -1) # Error 
print(25 * 3) # 75
print('25' * 3) # '252525'
print('25' * 4.0)  # Error 
print(3 * 'Hyd') #'HydHydHyd'
print('25' * True) #25

# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a)) #'Hyd', 'Address of object 'Hyd'
a = a * 3  #  It  is  valid  (or)  invalid # valid 
print(a , id(a)) # 'HydHydHyd', 'Address of object 'Hyd'

# len()  function  (Home  work)
print(len('Hyd')) # 3
print(len('Rama Rao')) # 8
print(len('9247')) # 4 
print(len('')) # 0
print(len(' ')) # 1
print(len(689)) # Error due to 'int' object  

# Find  outputs  (Home  work)
a = """"Hyd""" 
print(a) # "Hyd
print(len(a)) # 4
print(a[0]) # "
print("""Hyd"""")  # Error 
b = """""Hyd""" 
print(b)  # ""Hyd
print(len(b)) # 5

# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) #  string  from  indexes  7  to  13  in  steps  of  1  i.e. Dayal
print(a[7 : ]) #  string  from  indexes  7  to 18 i.e. Dayal Sarma 
print(a[ : 6])  #  string  from  indexes  0 to  7  in  steps  of  1  i.e. Sankar
print(a[ : ])  #  string  from  indexes  0  to  18  in  steps  of  2  i.e. Sankar Dayal Sarma
print(a[:  : ])  #  string  from  indexes  i.e. Sankar Dayal Sarma
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  11  in  steps  of  2  i.e. akrDy
print(a[0 : : 2]) #  string  from  indexes  0  to  18  in  steps  of  2  i.e. Sna aa am 
print(a[1 : : 2]) #  string  from  indexes  1  to  18  in  steps  of  2  i.e. akrDylSra
print(a[-5 : -1]) #  string  from  indexes  -5  to  -1    i.e. Sarm
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. amraS layaD raknaS
print(a[-1:-5:-1]) # string  from  indexes  -1  to   -5  in  steps  of  -1  i.e. arma
print(a[ : : -2]) # string  from  indexes  -1  to   -18  in  steps  of  -2  i.e. arSlyDrka
print(a[3 : -3]) # string  from  indexes  3  to   -3  i.e. kar Dayal Sa
print(a[2 : -5]) # string  from  indexes  2  to   -5  i.e. nkar Dayal
print(a[-1:-5]) # empty 
print(a[3 : 3]) # empty

#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1

#  Find  outputs  (Home  work)
a =  'A'
print(a[1]) # Error due to index 
print(a[1:]) # empty