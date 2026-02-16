#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) # Rama Rao
print(type(a)) # <class ‘str’ >
print(id(a)) # Address of str object , that is 2100000
b = 'Hyd'
print(b) # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # Hyd is green city.
                  Hyd is hitec city.
                 Hyd is beautiful city.

# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a') # Using index, print(a[o])
print(How  to  print  'y'  of  object  'a') # Using index, print(a[1])
print(How  to  print  'd'  of  object  'a') # Using index, print(a[2])
print(a[3]) # Error, there is no index ‘3’ in a.
print(How  to  print  'd'  of  object  'a') # Using  negative index, print(a[-3])
print(How  to  print  'y'  of  object  'a') # Using  negative index, print(a[-2])
print(How  to  print  'H'  of  object  'a') # Using  negative index, print(a[-1])
print(a[-4]) # Error, there is no index ‘-4’ in a.
print(a[0] == a[-3]) # It prints true, because the element of a[0] and a[-3] in ‘a’ are same.
a[2] = 'c' #  Error, str objects are immutable, they does not change.
print(25[0])  # Error, due to here 25 is int.
print('25'[0]) # 2
print(True[1]) # Error due to True is not string
print('True'[1]) # r


#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) # HydHydHyd
print(a * 2) # HydHyd
print(a * 1) # Hyd
print(a * 0) # Empty str
print(a * -1) # Empty str
print(25 * 3) # 75 because here 25 is considered as int 
print('25' * 3) # 252525
print('25' * 4.0)  # 25252525
print(3 * 'Hyd') # HydHydHyd
print('25' * True) # 25, here true is 1 due to arthimetic operation is performed.

# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a)) # Hyd, 1450000
a = a * 3  #  It  is  valid  (or)  invalid
# It is valid, where a is repeated and stored .
print(a , id(a)) # HydHydHyd , 1460000




# len()  function  (Home  work)
print(len('Hyd')) # 3
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('')) # 0, length of empty str is 0
print(len(' ')) # 1
print(len(689)) # Error due to 689 is not str, where it is int object

# Find  outputs  (Home  work)
a = """"Hyd"""
print(a) # “Hyd
print(len(a)) # 4
print(a[0]) # “
print("""Hyd"""") Error   
b = """""Hyd"""
print(b)  # ““Hyd
print(len(b)) # 5

# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) # Dayal
print(a[7 : ]) # Index starting at 7 till end with default step 1, Dayal Sarma
print(a[ : 6])  #  Index start default 0 till 5 with default step 1, Sankar
print(a[ : ])  # Full string with all default values, Sankar Dayal Sarma
print(a[:  : ]) # Sankar Dayal Sarma
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2]) # Starting with index 0, with step value 2 till end, even indexes Sna  aa  am
print(a[1 : : 2]) # Starting with index 1, with step value 2 till end, odd indexes  akrDylSra
print(a[-5 : -1]) # arm
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1]) # amra
print(a[ : : -2]) # Reverse string with step value 2, arSlyDrka
print(a[3 : -3]) # kar  Dayal Sa 
print(a[2 : -5]) # nkar Dayal
print(a[-1:-5])# Empty str, due to default positive step value +1, where we are starting from last letter from right side -1 and we can not move forward towards right side beyond last letter so empty str
print(a[3 : 3]) # 



#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1

#  Find  outputs  (Home  work)
a =  'A'
print(a[1]) # A 
print(a[1:]) # Error due to no letter at index 1 in a.       
