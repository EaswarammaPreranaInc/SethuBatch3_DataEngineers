#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a)#Rama Rao
print(type(a))#<class 'str'>
print(id(a))#address of object a
b = 'Hyd'
print(b)#Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)#'''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''



# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a')# print(a[0])
print(How  to  print  'y'  of  object  'a')#print(a[1]) 
print(How  to  print  'd'  of  object  'a')# print(a[2])
print(a[3])#error due to It is not present in the given statement
print(How  to  print  'd'  of  object  'a')# print(a[-1])
print(How  to  print  'y'  of  object  'a')# print(a[-2])
print(How  to  print  'H'  of  object  'a')# print(a[-3])
print(a[-4])#error  Due to it is not present in the given statement
print(a[0] == a[-3]) #True
a[2] = 'c' 
print(25[0]) # Error due They do not declare 
print('25'[0])#2
print(True[1]) # Error due They do not declare
print('True'[1])#r


#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)#'HydHydHyd'
print(a * 2)#'HydHyd'
print(a * 1)#'Hyd'
print(a * 0)#
print(a * -1)#
print(25 * 3)#75
print('25' * 3)#'252525'
print('25' * 4.0)# Error due to it is Decimal value
print(3 * 'Hyd')#'HydHydHyd'
print('25' * True)#25




# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))#'Hyd', address of object
a = a * 3  #  It  is  valid  (or)  invalid #valid
print(a , id(a))#HydHydHyd, address of object



# len()  function  (Home  work)
print(len('Hyd'))#3
print(len('Rama Rao'))#8
print(len('9247'))#4
print(len(''))#0
print(len(' '))#0
print(len(689))#error due to no colen

# Find  outputs  (Home  work)
a = """"Hyd"""
print(a)#Hyd
print(len(a))#4
print(a[0])#"
print("""Hyd"""")#error due It is missing one colen
b = """""Hyd"""
print(b)  #Hyd
print(len(b))#5


# Find  outputs

a = 'Sankar Dayal Sarma'
print(a[7 : 12])#  string  from  indexes  7  to  13  in  steps  of  1  i.e Dayal
print(a[7 : ]) #  string  from  indexes  7  to  18 in  steps  of  1 i.e Dayal Sarma
print(a[ : 6])# string  from  indexes  0 to   in  steps  of  1 i.e  Sankar 
print(a[ : ])# string  from  indexes  0 to  18 in  steps  of  1 i.e Sankar Dayal Sarma
print(a[:  : ]) # string  from  indexes  0 to  18 in  steps  of  1 i.e Sankar Dayal Sarma
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  11  in  steps  of  2  i.e. akrDy
print(a[0 : : 2]) #string  from  indexes  0 to  18 in  steps  of  2 i.e Sna aa ama
print(a[1 : : 2]) #string  from  indexes  1 to  18 in  steps  of  2 i.e  akrDylSra
print(a[-5 : -1]) #string  from  indexes  -1 to-5   in  steps  of  -1 i.e Sarma 
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1])#string  from  indexes  -1 to-5   in  steps  of  -1 i.e amr as 
print(a[ : : -2])# string  from  indexes  -1 to-19   in  steps  of  -2 i.e arSlyDrka
print(a[3 : -3])# string  from  indexes 3 to -4 in step of -1 of  kar Dayal S
print(a[2 : -5])# string  from  indexes 2 to -6 in step of -1 of nkar Dayal 
print(a[-1:-5])#string  from  indexes  -1 to -5   in  steps  of  -1 i.e
print(a[3 : 3])#string  from  indexes  3 to 3   in  steps  of  1 i.e 



#   0      1      2      3      4       5       6           7        8       9     10     11     12         13      14         15      16     17
#   S      a      n      k      a       r                    D       a       y      a     l                  S       a         r       m       a
#  -18   -17     -16   -15    -14      -13     -12          -11     -10     -9     -8    -7      -6          -5      -4       -3      -2      -1

#  Find  outputs  (Home  work)
a =  'A'
print(a[1])#error due to it is not present in Statement
print(a[1:])#<space>





