# Topic-1
#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) # Rama Rao
print(type(a)) #<class ‘str’>
print(id(a)) #str address 
b = 'Hyd'
print(b) # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # full c is printed 
# Topic-2
 # Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a') # print(a[0])
print(How  to  print  'y'  of  object  'a')# print(a[1])
print(How  to  print  'd'  of  object  'a')# print(a[2])
print(a[3]) #d
print(How  to  print  'd'  of  object  'a')# print(a[-1])
print(How  to  print  'y'  of  object  'a')# print(a[-2])
print(How  to  print  'H'  of  object  'a')# print(a[-3])
print(a[-4])#error out of range 
print(a[0] == a[-3]) # True
a[2] = 'c' # error str is immutable 
print(25[0]) # int is not reference
print('25'[0]) # 2
print(True[1]) # True is keyword 
print('True'[1]) # r
#Topic-3
 #  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) #HydHydHyd 
print(a * 2) #HydHyd
print(a * 1) #Hyd
print(a * 0) #empty str
print(a * -1) # empty str
print(25 * 3) # 75
print('25' * 3) # 252525
print('25' * 4.0)  #error only int is allowed 
print(3 * 'Hyd')  #HydHydHyd
print('25' * True) # 25
#Topic-4
 # Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd' # srt object
print(a , id(a)) #Hyd address of the str object 
a = a * 3  #  It  is  valid  (or)  invalid #valid 
print(a , id(a)) #HydHydHyd new address of the new str object

#Topic-5
 # len()  function  (Home  work)
print(len('Hyd')) #3
print(len('Rama Rao')) #8
print(len('9247')) #4
print(len('')) #0
print(len(' ')) #1
print(len(689))# error int is not taken 
#Topic-6
 Find  outputs  (Home  work)
a = """"Hyd""" # srt object 
print(a) # ”Hyd
print(len(a)) #4
print(a[0]) # ” 
print("""Hyd"""")  # error extra “ in the end
b = """""Hyd"""  # srt object
print(b)  #””Hyd
print(len(b)) #5
#Topic-7
# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) #Dayal
print(a[7 : ]) #Dayal Sarma
print(a[ : 6]) #Sankar 
print(a[ : ])  # full name 
print(a[:  : ])  # full name
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2]) # full name with even index characters 
print(a[1 : : 2]) # full name with odd index characters
print(a[-5 : -1]) # Sarm
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1]) # amra
print(a[ : : -2]) # string  from  indexes  -1  to   -18  in  steps  of  -2 i.e. Reverse  string #arSlyDrka
print(a[3 : -3]) #index 3,0,-3,-6,-9,-12,-1,5-18
#a[3: - 3: 1]  kar_Dayal_Sa
print(a[2 : -5]) #index 2,-3,-8,-13,-18
#a[2: - 5: 1]  nkar_Dayal_
print(a[-1:-5]) #index -1,-6,-11,-16
#a[-1: - 5: 1]  empty string 
print(a[3 : 3])  #index 3,6,9,12,15
#a[3: 3: 1]  empty string

#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1
#Topic-8
 #  Find  outputs  (Home  work)
a =  'A' # srt object 
print(a[1]) # error out of range 
print(a[1:]) # empty str