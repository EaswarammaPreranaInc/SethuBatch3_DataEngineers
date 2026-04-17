#  Find  outputs  (Home  work)
a = "Rama Rao" 
print(a) #Rama Rao
print(type(a)) #<class 'str'>
print(id(a)) #Address of object Rama Rao
b = 'Hyd'
print(b) #Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) #Hyd is green city. 
          Hyd is hitec city. 
          Hyd is beautiful city. 


# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a') # a[0]
print(How  to  print  'y'  of  object  'a') # a[1]
print(How  to  print  'd'  of  object  'a') #a[2]
print(a[3])  #Error
print(How  to  print  'd'  of  object  'a') #a[-3]
print(How  to  print  'y'  of  object  'a') #a[-2]
print(How  to  print  'H'  of  object  'a') #a[-1]
print(a[-4]) #Error
print(a[0] == a[-3]) #True
a[2] = 'c' 
print(25[0])   #Error
print('25'[0]) #2
print(True[1]) #Error
print('True'[1]) #r


#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) #HydHydHyd
print(a * 2) #HydHyd
print(a * 1) #Hyd
print(a * 0) #Empty string
print(a * -1) #Empty string
print(25 * 3) #75
print('25' * 3) #252525
print('25' * 4.0)  #Error float 
print(3 * 'Hyd') #HydHydHyd
print('25' * True) #25

# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a)) #Hyd , Address of object Hyd
a = a * 3  #  It  is  valid  (or)  invalid - ->#valid
print(a , id(a)) #HydHydHyd , Address of object a*3

# len()  function  (Home  work)
print(len('Hyd')) #3
print(len('Rama Rao')) #8
print(len('9247')) #4
print(len('')) #0
print(len(' ')) #1
print(len(689)) #Error not a string

# Find  outputs  (Home  work)
a = """"Hyd"""
print(a) #"Hyd
print(len(a)) #4
print(a[0]) #"
print("""Hyd"""")   #Error extra "
b = """""Hyd"""
print(b)  #""Hyd
print(len(b)) #5

# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) #a[7:12:1]string from indexes 7 to 11 in steps of 1 
print(a[7 : ]) #a[7:18:1] --> string from 7 to 17 in steps of 1
print(a[ : 6])   #a[0:6:1] --> string from 0 to 6 in steps of 1
print(a[ : ])  #a[0:18:1] --> string from 0 to 17 in steps of 1 
print(a[:  : ])  #a[0:18:1] --> string from 0 to 17 in steps of 1 
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2]) #a[0:18:2] --> string from indexes 0 to 17 in steps of 2 
print(a[1 : : 2])  #a[1:18:2] -->string from indexes 1 to 17 in steps of 2
print(a[-5 : -1]) #a[-5:-1:-1]-->string from indexes -5 to -2 in steps of -1
print(a[::-1])  # a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string 
print(a[-1:-5:-1]) #string from indexes -1 to -4 in steps of -1
print(a[ : : -2]) #a[-1:-19:-2]--> string from indexes -1 to -18 in steps of -2
print(a[3 : -3]) #a[3:-3:1]-->string from indexes 3 to -2 in steps of 1
print(a[2 : -5]) #a[2:-5:1]-->string from indexes 2 to -4 in steps of 1
print(a[-1:-5]) #a[-1:-5:-1]-->string from indexes -1 to -4 in steps of -1
print(a[3 : 3]) #a[3:3:1]-->string from indexes 3 to 2 in steps of 1



#  0      1      2      3      4     5      6      7       8     9     10    11     12      13     14       15      16     17
#  S      a      n      k      a     r             D       a     y      a     l             S       a       r       m       a
# -18   -17    -16    -15    -14   -13    -12    -11     -10    -9     -8    -7     -6     -5      -4       -3      -2      -1

#  Find  outputs  (Home  work)
a =  'A'
print(a[1]) #Error no index no. 1
print(a[1:]) #

