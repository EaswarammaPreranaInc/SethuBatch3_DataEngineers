#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a)           #"Rama Rao"
print(type(a))     #<class 'str'>
print(id(a))       #address of object a 
b = 'Hyd'
print(b)           #'Hyd'
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)           #'''Hyd is green city.
                       Hyd is hitec city.
                       Hyd is beautiful city.'''


# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a')#print(a[0])
print(How  to  print  'y'  of  object  'a')#print(a[1])
print(How  to  print  'd'  of  object  'a')#print(a[2])
print(a[3])                                #error no index 3
print(How  to  print  'd'  of  object  'a')#print(a[-1])
print(How  to  print  'y'  of  object  'a')#print(a[-2])
print(How  to  print  'H'  of  object  'a')#print(a[-3])
print(a[-4])                               #error no index -4
print(a[0] == a[-3])                       #True
a[2] = 'c'                                 #error string is immutable
print(25[0])                               #error non sequence can't be indexed 
print('25'[0])                             #2
print(True[1])                             #error non sequence can't be indexed 
print('True'[1])                           #r

#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)                               #'HydHydHyd'
print(a * 2)                               #'HydHyd'
print(a * 1)                               #'Hyd'
print(a * 0)                               #' '
print(a * -1)                              #' '
print(25 * 3)                              #75
print('25' * 3)                            #'252525
print('25' * 4.0)                          #error can't be repeated with float number 
print(3 * 'Hyd')                           #'HydHydHyd'
print('25' * True)                         #'25'

# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))                            #'Hyd' address of object a 
a = a * 3  #  It  is  valid  (or)  invalid  #valid
print(a , id(a))                            #'HydHydHyd' address of object a 


# len()  function  (Home  work)
print(len('Hyd'))                            #3
print(len('Rama Rao'))                       #8
print(len('9247'))                           #4
print(len(''))                               #0
print(len(' '))                              #1
print(len(689))                              #error can't be find length for non sequences

# Find  outputs  (Home  work)
a = """"Hyd"""
print(a)                                     #"Hyd
print(len(a))                                #4
print(a[0])                                  #"
print("""Hyd"""")                            #Hyd" 
b = """""Hyd""
print(b)                                     #syntax error
print(len(b))                                #error

# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])   # a[7: 12 : 1]string from indexes 7 to 11 i.e Dayal
print(a[7 : ])                   #string from indexes 7 to end i.e Dayal Sarma
print(a[ : 6])                   #string from indexes 0 to 5 i.e Sankar
print(a[ : ])                    #string from indexes 0 to 18 i.e Sankar Dayal Sarma
print(a[:  : ])                  #string from indexes 0 to 18 i.e Sankar Dayal Sarma
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2])                #string from indexes 0 to 18 in steps of 2 i.e 'sna aa am'(even indexes)
print(a[1 : : 2])                #string from indexes 0 to 18 in steps of 2 i.e 'akrDylsra'(odd indexes)
print(a[-5 : -1])                #string from indexes -1 to -5 i.e 'amras'
print(a[::-1])  #a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1])#string from indexes -1 to -4 in steps of -1 i.e 'amra'
print(a[ : : -2])#string from indexes -1 to -18 in steps of -2 i.e 'arslyDrka'
print(a[3 : -3])#string from indexes 3 to -3 in i.e  'kar Dayal Sa'
print(a[2 : -5])#string from indexes 2 to -5 in i.e  'nkar Dayal '
print(a[-1:-5])#string from indexes -1 to -5 i.e 'amra'
print(a[3 : 3])#string from indexes 3 to 3 in i.e  ' '



#   0      1      2      3      4       5       6           7       8       9     10     11     12      13  14       15      16     17
#   S      a      n      k      a       r                  D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1


#  Find  outputs  (Home  work)
a =  'A'
print(a[1])# Error 
print(a[1:])#''
