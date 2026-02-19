Assignment 2
  

#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a)  Rama Rao
print(type(a)) <class str>
print(id(a)) address of the Rama Rao
b = 'Hyd'
print(b) Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c).  Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''



# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a')  a[0]
print(How  to  print  'y'  of  object  'a')  a[1]
print(How  to  print  'd'  of  object  'a') a[2]
print(a[3])  Error
print(How  to  print  'd'  of  object  'a') a[~1]
print(How  to  print  'y'  of  object  'a') a[-2]
print(How  to  print  'H'  of  object  'a') a[-3]
print(a[-4]) Error
print(a[0] == a[-3])  True
a[2] = 'c'  
print(25[0])  error 
print('25'[0]) 2
print(True[1]) error
print('True'[1]) r

#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) ‘HydHydHyd’
print(a * 2) ‘HydHyd’
print(a * 1) ‘Hyd’
print(a * 0) ‘’
print(a * -1)’’
print(25 * 3) 75
print('25' * 3) ‘252525’
print('25' * 4.0)  error
print(3 * 'Hyd') ‘HydHydHyd’
print('25' * True) Error

# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))  ‘Hyd’ ,address of the str Hyd
a = a * 3  #  It  is  valid  (or)  invalid  valid
print(a , id(a)). ‘HydHydHyd’,  adress of the str HydHydHyd

# len()  function  (Home  work)
print(len('Hyd')) 3
print(len('Rama Rao')) 8
print(len('9247')) 4
print(len('')) 0
print(len(' ')) 1
print(len(689)) error

# Find  outputs  (Home  work)
a = """"Hyd"""
print(a) Hyd
print(len(a)) 3
print(a[0]) H
print("""Hyd"""")   Hyd
b = """""Hyd"""
print(b)  Hyd
print(len(b)) 3



# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])  begins with 7,ends with 11 in 1step   i.e.Dayal
print(a[7 : ])  begins with 7,ends with len in 1step  i.e. Dayal sarma
print(a[ : 6])   begins with 0,ends with 5 in 1step   i.e.Sankar
print(a[ : ])  begins with 0,ends with len in 1step   i.e.Sankar Dayal Sarma
print(a[:  : ])  begins with 0,ends with len in 1step   i.e.Sankar Dayal Sarma
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2]) string  from  indexes  0  to  len  in  steps  of  2  i.e. Sna aa am
print(a[1 : : 2]) string  from  indexes  1  to  len  in  steps  of  2  i.e. akrDylSra
print(a[-5 : -1]) string  from  indexes  -1 to  -6 in  steps  of  -1 i.e. Sanka
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1]) string  from  indexes  -1 to  -6  in  steps  of  2  i.e. Sanka
print(a[ : : -2])  string  from  indexes  -1  to  -len—1 in  steps  of  2  i.e. Sna aa am
print(a[3 : -3]) error 
print(a[2 : -5]) error
print(a[-1:-5]) string  from  indexes  -1  to  -5  in  steps  of  1 i.e. Sanka
print(a[3 : 3]) n



#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1