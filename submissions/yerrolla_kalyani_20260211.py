#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) # Rama Rao
print(type(a)) #<class 'str'>
print(id(a)) #prints address of the object 'Rama Rao'
b = 'Hyd'
print(b) # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) #   Hyd is green city.
			 Hyd is hitec city.
			 Hyd is beautiful city.
# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a') #a[0]
print(How  to  print  'y'  of  object  'a') #a[1]
print(How  to  print  'd'  of  object  'a') #a[2]
print(a[3])    #error due to invalid index number
print(How  to  print  'd'  of  object  'a') #a[-1]
print(How  to  print  'y'  of  object  'a') #a[-2]
print(How  to  print  'H'  of  object  'a') #a[-3]
print(a[-4])   #error due to invalid index number
print(a[0] == a[-3])    #True
a[2]='c'#error due to string is immutable not support item assignment.
print(25[0])      #error due to indexing is not supported by <class int>
print('25'[0])   #2
print(True[1])    #error due to indexing is not supported by <class bool>
print('True'[1])   #r
#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)   #HydHydHyd
print(a * 2)   #HydHyd
print(a * 1)   #Hyd
print(a * 0)   #not print anything
print(a * -1)   #not print anything 
print(25 * 3)   #75
print('25' * 3)   #252525
print('25' * 4.0)   #  error due to invalid float number in repetation
print(3 * 'Hyd')   #HydHydHyd
print('25' * True)   #25
# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))    #Hyd<space>address of the  string object'Hyd'
a = a * 3  #  It  is  valid  (or)  invalid   #valid
print(a , id(a))   #HydHydHyd<space>address of string object 'HydHydHyd'      
# len()  function  (Home  work)
print(len('Hyd'))   #3
print(len('Rama Rao'))   #8
print(len('9247'))   #4
print(len(''))   #0
print(len(' '))   #1
print(len(689))   # error due to len() is not supported by int class
# Find  outputs  (Home  work)
a = """"Hyd"""
print(a)   #"Hyd
print(len(a))  #4
print(a[0])   #"
print("""Hyd"""") #syntax error due to invalid input
b = """""Hyd"""
print(b)     #""Hyd
print(len(b))   #5
# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])    #Dayal (starting from indexes 7 to 11 in stepping of 1)
print(a[7 : ])    #Dayal Sarma (starting from indexes 7 to 18 in stepping of 1)
print(a[ : 6])      #Sanka (starting from indexes 0 to 5 in stepping of 1)
print(a[ : ])     #Sankar Dayal Sarma (starting from indexes 0 to 18 in stepping of 1)
print(a[:  : ])    # Sankar Dayal Sarma (starting from indexes 0 to 18 in stepping of 1)
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2])    #Sna aa am (starting from 0 to 18 in stepping of 2)
print(a[1 : : 2])    #akrDylsra (strting from 1 to 18in stepping of 2)
print(a[-5 : -1])    #sarm (starts from -5 to -2 in stepping of 1)
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1])   # amra(starting from -1 to -4 in stepping  of -1)
print(a[ : : -2])    #arSlyDrka(straring from 0 to 18stepping in -2)
print(a[3 : -3]) #kar Dayal sa (starting from 3 to -4 in stepping  of 1))
print(a[2 : -5])    #nkar Dayal in 
print(a[-1:-5])   #amra (starting from -1 to -4 in steps of 1)
print(a[3 : 3])    #not print anything .



#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1
              
#  Find  outputs  (Home  work)
a =  'A'
print(a[1])   #error invalid index number
print(a[1:])   #error due to invalid index number