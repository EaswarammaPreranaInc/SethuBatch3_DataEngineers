-->#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) # Rama Rao
print(type(a)) #<class 'str'>
print(id(a)) # address of the object Rama Rao
b = 'Hyd'
print(b) # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # Hyd is green city.
           Hyd is hitec city.
           Hyd is beautiful city.


--># Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a') # 'Hyd'[0]
print(How  to  print  'y'  of  object  'a') # 'Hyd'[1]
print(How  to  print  'd'  of  object  'a') # 'Hyd'[2]
print(a[3])  # ERROR because no char at index 3
print(How  to  print  'd'  of  object  'a') # 'Hyd'[-1]
print(How  to  print  'y'  of  object  'a') # 'Hyd'[-2]
print(How  to  print  'H'  of  object  'a') # 'Hyd'[-3]
print(a[-4]) # ERROR because no char at index -4
print(a[0] == a[-3]) #True
a[2] = 'c' # ERROR because we can't replace str
print(25[0])  # ERROR because 25 is not identified as str as there are no quotes present
print('25'[0]) # 2
print(True[1]) # ERROR because True is not identified as str as there are no quotes present
print('True'[1]) # r

-->#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) #'HydHydHyd'
print(a * 2) #'HydHyd'
print(a * 1) #'Hyd'
print(a * 0) # Empty str
print(a * -1) # Empty str
print(25 * 3) # 75
print('25' * 3) #'252525'
print('25' * 4.0) # ERROR float can't be used in repetation operator
print(3 * 'Hyd') # 'HydHydHyd'
print('25' * True) # '25' because True=1 when operation is performed on True

--># Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a)) #'Hyd' address of the object 'Hyd'
a = a * 3  #  It  is  valid  (or)  invalid # Valid 
print(a , id(a)) # 'HydHydHyd' address of the object 'HydHydHyd'

--># len()  function  (Home  work)
print(len('Hyd')) # 3
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('')) #0
print(len(' ')) #1
print(len(689)) # ERROR because 689 is not written as str


--># Find  outputs  (Home  work)
a = """"Hyd"""
print(a) # "Hyd
print(len(a)) # 4
print(a[0]) # " 
print("""Hyd"""") # ERROR because it should be in 3 double quotes only
b = """""Hyd"""
print(b)  # ""Hyd
print(len(b)) # 5

--># Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) # a[7:13:1] --> string  from  indexes  7  to  12  in  step  of  1  i.e.'Dayal '
print(a[7 : ])  # a[7:18:1] --> string  from  indexes  7  to  17  in  step  of  1  i.e.'Dayal Sarma'
print(a[ : 6])  # a[0:6:1] --> string  from  indexes  0  to  5  in  step  of  1  i.e.'Sankar '
print(a[ : ])  # a[0:18:1] --> string  from  indexes  0  to  17  in  steps  of  1  i.e.'Sankar Dayal Sarma'
print(a[:  : ])  # a[0:18:1] --> string  from  indexes  0  to  17  in  steps  of  1  i.e.'Sankar Dayal Sarma'
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2]) #  string  from  indexes  0  to  17 in steps of 2 i.e. Sna aa am
print(a[1 : : 2]) #  string  from  indexes  1  to  17  in  steps  of  2  i.e. akrDylSra
print(a[-5 : -1]) #  a[-5:-1:1] --> string  from  indexes  -5  to -2   in  steps  of  1  i.e. Sarm
print(a[::-1])  #   a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string (amraS layaD raknaS)
print(a[-1:-5:-1]) # string  from  indexes  -1  to -4  in  steps  of  -1  i.e. amra
print(a[ : : -2]) # a[-1 : -19 : -2]  ---> string  from  indexes  -1  to -18  in  steps  of  -2  i.e. arSlyDrka
print(a[3 : -3]) # a[3:-3:1] --> string  from  indexes 3 from start till -4 from end in  step  of 1  i.e. kar Dayal Sa
print(a[2 : -5]) # a[2:-5:1] --> string  from  indexes 2 from start till -6 from end in  step  of 1  i.e. 'nkar Dayal '
print(a[-1:-5]) # a[-1:-5:1] --> Empty str ''
print(a[3 : 3]) # a[3:3:1] --> Empty str ''


#   0      1      2      3      4       5       6           7       8       9     10     11     12           13      14       15      16     17
#   S      a      n      k      a       r                   D       a       y      a      l                   S       a        r       m      a
#  -18   -17     -16    -15    -14     -13     -12         -11     -10     -9     -8     -7     -6           -5      -4       -3      -2     -1


-->#  Find  outputs  (Home  work)
a =  'A'
print(a[1]) #ERROR because index 1 has no char written
print(a[1:]) # Empty str
