#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a)          # Rama Rao
print(type(a))    # <class 'str'>
print(id(a))      # address of object a

b = 'Hyd'
print(b)         #Hyd
c = '''Hyd is green city.    
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)          #  Hyd is green city.    
                  #   Hyd is hitec city.
                   #  Hyd is beautiful city.
# Index   demo  program  (Home  work)
a = 'Hyd'
 print(How  to  print  'H'  of  object  'a')  # print(a[0])
 print(How  to  print  'y'  of  object  'a')  #print(a[1])
 print(How  to  print  'd'  of  object  'a')  #print(a{2])
 print(a[3])   # error because it not contain element a[3]
 print(How  to  print  'd'  of  object  'a') # print(a[-1]) 
 print(How  to  print  'y'  of  object  'a')# print(a[-2])
 print(How  to  print  'H'  of  object  'a') # print(a[-3])
 print(a[-4]) # error because there is no element of indexes a[-4]
 print(a[0] == a[-3]) # True because both indexes indicates same element
 a[2] = 'c' # error
 print(25[0]) #error there is no 25 list  
 print('25'[0])# 2 because in 25 0th element is 2
 print(True[1]) # error 
 print('True'[1])  #r because in word True 1's place is r

#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)#HydHydHyd repeate 3 times
print(a * 2)#HydHyd repeate 2 times
print(a * 1)#Hyd repeate 1 time
print(a * 0) # no output because 0 times it not repeate
print(a * -1)# no output because -1 times it not repeate
print(25 * 3) # 75 simply multiply
print('25' * 3)#252525 3 times repeate because it is a string
print('25' * 4.0)#  no outpu because it cannot be a float 
print(3 * 'Hyd')#HydHydHyd 
print('25' * True)#25*1=25
                                                       
# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
  print(a , id(a)) # Hyd address of list hyd
  a = a * 3  #  It  is  valid  (or)  invalid #sol: valid because it reference is modified
  print(a , id(a)) # Hyd  address of object hyd

# len()  function  (Home  work)
  print(len('Hyd')) #3
  print(len('Rama Rao')) #8
  print(len('9247'))#4 it will be treated as srting
  print(len(''))#0 because no elements
  print(len(' '))#1 space is also treated as an element
  print(len(689))#error its not a string

# Find  outputs  (Home  work)
a = """"Hyd""" 
  print(a)      # "Hyd
  print(len(a)) #4
  print(a[0])#" 
  print("""Hyd"""")   #error because it as one extra "
        
b = """""Hyd"""
  print(b)  #""Hyd
  print(len(b)) # 5

# Find  outputs
a = 'Sankar Dayal Sarma'
        print(a[7 : 12]) # Dayal
        print(a[7 : ])   # Dayal Sarma 
        print(a[ : 6])  #Sankar 
        print(a[ : ])  #Sankar Dayal Sarma
        print(a[:  : ])  #Sankar Dayal Sarma
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
        print(a[0 : : 2]) #Sna aa am ,srting from indexes 0 to end of string in steps of 2
        print(a[1 : : 2]) #akrDylSra,string from indexes from 1 to end of string in steps of 2
        print(a[-5 : -1]) #Sarm
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
        print(a[-1:-5:-1])#amraS layaD raknaS,string from indexes -1 to -18 in steps of -1 
        print(a[ : : -2]) #arSlyDrka
        print(a[3 : -3]) #kS
        print(a[2 : -5]) #nkar Dayal



#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1       

#  Find  outputs  (Home  work)
#  Find  outputs  (Home  work)
a =  'A'
print(a[1])#0 ERROR NO Element
print(a[1:])# ERROR


        
