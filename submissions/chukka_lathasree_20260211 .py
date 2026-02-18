#  Find  outputs  (Home  work)
a = "Rama Rao"---> # string
print(a) ---> #Rama Rao
print(type(a)) ---> # string object
print(id(a)) ----> # Adress of object
b = 'Hyd' ---> String 
print(b) ---> # Hyd 
c = '''Hyd is green city. ---> 
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) ----> Hyderabad is green city
               Hyderabad is hitec city
               Hyderabad is beautiful city.

# Index   demo  program  (Home  work)
a = 'Hyd' ---> #length of object Hyd have H=0, y=1,d=2
print(How  to  print  'H'  of  object  'a') ---> index is 0
print(How  to  print  'y'  of  object  'a')----> index is 1
print(How  to  print  'd'  of  object  'a')----> index is 2
print(a[3]) ---> Error
print(How  to  print  'd'  of  object  'a')---> negative index value start from end of the string -1 to -length of the string i.e d=-1
print(How  to  print  'y'  of  object  'a')---> y=-2
print(How  to  print  'H'  of  object  'a')---> d=-3
print(a[-4])---# Error
print(a[0] == a[-3]) ---> a[0]=H, a[-3]=h
a[2] = 'c' ---> # Error
print(25[0])---> # 25   
print('25'[0])---> # Error
print(True[1]) ---> # Error
print('True'[1]) ---> # Error

#  Find  outputs  (Home work)
a = 'Hyd' 
print(a * 3) ---> HydHydHyd
print(a * 2) ----> HydHyd
print(a * 1)--->Hyd
print(a * 0)---> 0
print(a * -1)---> 0
print(25 * 3)---> 0
print('25' * 3)---->0
print('25' * 4.0)  --->0
print(3 * 'Hyd')---> HydHydHyd
print('25' * True)---> 0

# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))  ---> Hyd, address of object
a = a * 3  #  It  is  valid  (or)  invalid ---> invalid
print(a , id(a)) ---> error

# len()  function  (Home  work)
print(len('Hyd')) ---> 0 1 2
                       H y d = 3
print(len('Rama Rao'))  ---> R a m a   R a o = 8
                             0 1 2 3 4 5 6 7     
print(len('9247')) ---> 9 2 4 7 = 4
                        0 1 2 3 
print(len('')) ---> Error 
print(len(' ')) ----> Error
print(len(689))---> Error = 3

# Find  outputs  (Home  work)
a = """"Hyd""" 
print(a) ----> Hyd
print(len(a)) ---> H y d = 3
                   0 1 2
print(a[0])---> Error
print("""Hyd"""") ----> Hyd    
b = """""Hyd"""
print(b)  --> # Hyd
print(len(b)) ---> H y d = 3
                   0 1 2

# Find  outputs
a = 'Sankar Dayal Sarma' 
 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 - 8  -7 -6 -5 -4 -3 -2 -1
  S   a   n   k   a   r        D   a    y  a  l     S  a  r  m  a
 0    1   2   3   4   5   6    7   8    9  10 11 12 13 14 15 16 17
print(a[7 : 12]) ---> # Dayal 
print(a[7 : ]) ---> #Error
print(a[ : 6])   ---> Error
print(a[ : ])  ---> Error
print(a[:  : ])  ---> Error
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2]) ---> # S n a  a a  a m
print(a[1 : : 2]) --> # a k r d  l s r a
print(a[-5 : -1]) ---> # S l a y a D r a k n a S
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1]) --> # a m r a S 
print(a[ : : -2]) ---> # string  from  indexes  -1  to   -18  in  steps  of  -2  i.e. Reverse  string

print(a[3 : -3]) --->

print(a[2 : -5]) 
print(a[-1:-5]) --> string  from  indexes  -1  to   -18  in  steps  of  -5  i.e. Reverse  string

print(a[3 : 3]) --> string  from  indexes  3 to   17  in  steps  of  3  i.e k  y  r




#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1

#  Find  outputs  (Home  work)
a =  'A'
print(a[1]) ---> 1
print(a[1:]) ---> ankar Daal Sarma
