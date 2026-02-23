#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) # Rama Rao
print(type(a)) # <class 'Str'>
print(id(a)) # Addres of object "Rama Rao"
a = 'Hyd' # Ref 'a' is modified to object 'Hyd'
print(a) # Hyd
a = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.''' # Multi line string
print(a) # Hyd is green city.  <next line> Hyd is hitech city. <next line> Hyd is beautiful city.                                                                                                                                                                     # Hyd is hitec city.                                                                                                                    # Hyd is beatiful city.

# Index   demo  program  (Home  work)
a = 'Hyd'
print('Hyd'[0])  #  Char  at  index  0  of  object  'Hyd'  i.e.  'H'
print('Hyd'[1])  #  Char  at  index  1   of  object  'Hyd'  i.e.  'y'
print('Hyd'[2])  #  Char  at  index  2   of  object  'Hyd'  i.e.  'd'
#print(a[3]) #  Error  :   Index  3  does  not  exist  in  'Hyd'
print('Hyd'[-1])  #  Char  at  index   -1  of  object  'Hyd'  i.e.  'd'
print('Hyd'[-2])  #  Char  at  index   -2  of  object  'Hyd'  i.e.  'y'
print('Hyd'[-3])  #  Char  at  index   -3  of  object  'Hyd'  i.e.  'H'
#print(a[-4])  #  Error  :   Index  -4  does  not  exist  in  'Hyd'
print(a[0] ==  a[-3]) #  'H' == 'H'  is  True
#a[2] = 'c'  #  Error :   'd'  can  not  be  replaced  with  'c'  as  str  object  is  immutable
#print(25[0]) #  Error : Non-sequence  (such  as  int)  is  not  indexed
print('25'[0])  #  Char  at  index  0  of  object  '25'  i.e.  '2'
#print(True[1])   #  Error :  Non-sequence  (such  as  bool)  is  not  indexed
print('True'[1])  #  Char  at  index  1   of  'True'    i.e.  'r'

#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) #  Repeats  string  thrice  i.e.  HydHydHyd
print(a * 2)  #  Repeats  string  twice   i.e.  HydHyd
print(a * 1)  #  Repeats  string  once   i.e.  Hyd
print(a * 0)  #  Repeats  string   0  times    i.e.   Empty  string
print(a * -1)  #  Repeats  string   -1   times    i.e.   Empty  string
print(25 * 3)  # 75
print('25' * 3)  #  Repeats  string  thrice  i.e. 252525
#print('25' * 4.0) #  Error due to float  operand  4.0
print(3 * 'Hyd')  #  HydHydHyd
print('25' * True)  #  Repeats  string  once   i.e.  25

# Tricky  program

#  Find  outputs  (Home work)
a = 'Hyd'  #  Ref  'a'  points  to  object   'Hyd'
print(a , id(a))  #  Hyd   <space>  Address  of  'Hyd'
a = a * 3  #  Ref   'a'  is  modified  to  a  new  string   object 'HydHydHyd'
print(a , id(a))  #  HydHydHyd    <space>   Address


# len()  function  (Home  work)
print(len('Hyd'))  # 3
print(len('Rama Rao')) # 8
print(len('9247'))  # 4
print(len('')) #  0  due  to  empty  string
print(len(' ')) #  1  due to  space
#print(len(689)) #  Error  :   Argument  should  be  a  sequence  but  689  is  not  a  sequence


# Find  outputs  (Home  work)
a = """"Hyd"""
print(a)    # Hyd
print(len(a))  # 4
print(a[0])  # 
print("""Hyd"""") #error
b = """""Hyd"""
print(b)  # "" Hyd
print(len(b)) # 5

# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])  #Dayal
print(a[7 : ])  # Dayal Sarma
print(a[ : 6])   # sankar
print(a[ : ])  # sankar Dayal sarma
print(a[:  : ])  # sankar Dayal sarma
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2]) # sna aa am
print(a[1 : : 2]) # akrDylSra
print(a[-5 : -1])  # Sarm
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1])  # amra
print(a[ : : -2])  # amSlyDkns
print(a[3 : -3])  # kar Dayal sa
print(a[2 : -5])  # nkar Dayal
print(a[-1:-5]) # nothing
print(a[3 : 3])  # nothing


#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1

#  Find  outputs  (Home  work)
a =  'A'
print(a[1]) #error
print(a[1:]) # nothing