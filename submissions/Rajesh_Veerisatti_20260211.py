#  Find  outputs 
a = "Rama Rao"
print(a) #Rama Rao
print(type(a)) #<class 'str'>
print(id(a)) #(address of object Rama Rao given by pvm)
b = 'Hyd'
print(b) # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # Hyd is green city.
         #  Hyd is hitec city.
          #  Hyd is beautiful city.


# Index   demo  program 
a = 'Hyd'
''' print(How  to  print  'H'  of  object  'a') # index a[0]
print(How  to  print  'y'  of  object  'a')  # index a[1]
print(How  to  print  'd'  of  object  'a')  # index a[2]
# print(a[3])   # error bcz there is no 4 char in str
print(How  to  print  'd'  of  object  'a')  # index a[2]
print(How  to  print  'y'  of  object  'a')  # index a[1]
print(How  to  print  'H'  of  object  'a') # index a[0]
'''
# print(a[-4]) # error bcz there is only 3 char in str
# print(a[0] == a[-3])  # True 
# a[2] = 'c'  # error this is invalid in python it run by immutable 
# print(25[0])  # error no mention str
print('25'[0]) # 2
# print(True[1]) # error no mention str
print('True'[1]) # r
#  Find  outputs  (Home work)


a = 'Hyd'
print(a * 3) #'HydHydHyd'
print(a * 2) #'HydHyd'
print(a * 1)# ' Hyd'
print(a * 0)#
print(a * -1)#
print(25 * 3)#75
print('25' * 3)#252525
# print('25' * 4.0)  #error bcz float thing is repeat only int I'll do
print(3 * 'Hyd')# 'HydHydHyd'
print('25' * True)#25


# Tricky  program
#  Find  outputs  
a = 'Hyd'
print(a , id(a)) #Hyd,address of str Hyd by pvm
a = a * 3  #  It  is  valid  (or)  invalid # this is valid here it's create new with a
print(a , id(a)) #'HydHydHyd', address of the str HydHydHyd
# len()  function  (Home  work)
print(len('Hyd'))#3
print(len('Rama Rao'))#8
print(len('9247'))#4
print(len(''))#0
print(len(' '))#1
#print(len(689))# error there is no length for int


# Find  outputs  (Home  work)
a = """"Hyd"""
print(a)# "Hyd
print(len(a))#4
print(a[0])#"
# print("""Hyd"""")   # error bcz after the str" are indicative one that are not closed
b = """""Hyd"""
print(b)  #""Hyd
print(len(b)) # 5


# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) # str frm indexs 7 to 11 in steps of 1--Dayal
print(a[7 : ]) # str frm indexs 7 to 17 in steps of 1---Dayal Sarma
print(a[ : 6])   # str frm indexs 0 to 5 in steps of 1---- Sankar
print(a[ : ])  #  str frm indexs 0 to 17 in steps of 1--- Sankar Dayal Sarma
print(a[:  : ])    # str frm indexs 0 to 17 in steps of 1--- Sankar Dayal Sarma
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2])   # str frm indexs 0 to 17 in steps of 2--- Sna aa am
print(a[1 : : 2])   # str frm indexs 1 to 17 in steps of 2--- akrDylSra
print(a[-5 : -1])  # str frm indexs -5to -2 in steps of -1--- Sarm
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1])  # str frm indexs -1to -4 in steps of -1--- amra
print(a[ : : -2]) #  string  from  indexes  -1  to   -18  in  steps  of  -2---   ar aya nS
print(a[3 : -3])  # str frm indexs -15 to-4 in steps of -1--- kar Dayal Sa
print(a[2 : -5]) # str frm -16 to-6 in steps of 1--- nkar Dayal 
print(a[-1:-5]) #
print(a[3 : 3]) # equal range ....empty



#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1


#  Find  outputs  (Home  work)
a =  'A'
 # print(a[1])--- error length is 1 index is 0
 # print(a[1:])--- error length is 1 index is 0