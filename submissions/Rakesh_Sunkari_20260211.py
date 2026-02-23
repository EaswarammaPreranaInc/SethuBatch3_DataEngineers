#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) # < Rama Rao >
print(type(a)) # < class 'string' >
print(id(a)) # < address of the object >
b = 'Hyd'
print(b) # < Hyd >
c = '''Hyd is green city. 
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # <Hyd is green city. Hyd id beautiful, Hyd is beautiful city>
Hyd is hitec city.
Hyd is beautiful city.'''>


# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a') # < print a(0)) >
print(How  to  print  'y'  of  object  'a') # < print a(1)) >
print(How  to  print  'd'  of  object  'a') # < print a(2)) >
print(a[3])  # < error bez no 3 index >
print(How  to  print  'd'  of  object  'a') # < print (a[2]) >
print(How  to  print  'y'  of  object  'a') # < print (a[1]) >
print(How  to  print  'H'  of  object  'a') # < print (a[0]) >
print(a[-4]) # < Error bez no -4 index >
print(a[0] == a[-3]) # <  >
a[2] = 'c' # <  >
print(25[0])   
print('25'[0])
print(True[1]) 
print('True'[1])



#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) # < 'HydHydHyd' >
print(a * 2) # < 'HydHyd' >
print(a * 1) # < 'Hyd' >
print(a * 0) # < blank >
print(a * -1) # <  >
print(25 * 3) # < 75 >
print('25' * 3) # < '252525' >
print('25' * 4.0) # < 'error' >
print(3 * 'Hyd') # < 'HYdHydHyd' >
print('25' * True) # <  >




# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a)) # < Hyd, id of the object 'Hyd' >
a = a * 3  #  It  is  valid  (or)  invalid # <  valid >
print(a , id(a)) # < Hyd, id of the object 'Hyd' >




# len()  function  (Home  work)
print(len('Hyd')) # < 3 >
print(len('Rama Rao')) # < 8 >
print(len('9247')) # < 4 >
print(len('')) # < 1 >
print(len(' ')) #<  >
print(len(689)) # < 3 >



# Find  outputs  (Home  work)
a = """"Hyd"""
print(a) # < "Hyd" >
print(len(a)) 
print(a[0])
print("""Hyd"""")   
b = """""Hyd"""
print(b)  # <  >
print(len(b)) # 0	




# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) # string from 7 to 11 in steps of 1 i.e. dayal
print(a[7 : ]) # string from 7 to 0 in steps of 1 i.e. sankar d
print(a[ : 6])   # string from 0 to 1 in steps of 6
print(a[ : ])  # string from 0 to 18 in steps of 1 i.e. 
print(a[:  : ])  # string from 
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akr dy
print(a[0 : : 2]) # string from indexes 0 to 1 in steps of 2 i.e. 
print(a[1 : : 2]) # string from indexes 1 to 1 in steps of 2 i.e. 
print(a[-5 : -1]) # string from -5 to 
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1]) # string from indexes -1 to -4 in steps of -1 i.e. amra
print(a[ : : -2]) # string from indexes 
print(a[3 : -3]) # string from 3 to -2 in steps of 1 i.e. kar dayal sarm
print(a[2 : -5]) # string from 2 to -4 in steps of 1 i.e. nkar dayal sa
print(a[-1:-5]) # string form -1 to -4 in steps of -1 i.e. amra
print(a[3 : 3]) # string from 3 to 2 in steps of 1 i.e. kn



#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                 S       a       r       m       a
#  -18   -17     -16    -15    -14     -13    -12           -11     -10      -9      -8     -7   -6          -5      -4       -3      -2      -1





#  Find  outputs  (Home  work)
a =  'A'
print(a[1]) # <error bez no 1 index>
print(a[1:]) # <  >