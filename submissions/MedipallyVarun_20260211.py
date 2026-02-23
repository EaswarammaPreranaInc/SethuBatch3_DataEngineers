NAME: Medipally Varun 
Date : 11/02/2026





#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) # Rama Rao
print(type(a)) # class 'string'
print(id(a)) # address of object a
b = 'Hyd'
print(b) # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) #    Hyd is green city.
              Hyd is hitec city.
              Hyd is beautiful city.




# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a') # print(a[0])
print(How  to  print  'y'  of  object  'a') # print(a[1])
print(How  to  print  'd'  of  object  'a') # print(a[2])
print(a[3])  # Error because thare are only only up to 2 
print(How  to  print  'd'  of  object  'a') # print(a[2])
print(How  to  print  'y'  of  object  'a') # print(a[1])
print(How  to  print  'H'  of  object  'a') # print(a[0])
print(a[-4]) # Error there no index like -4
print(a[0] == a[-3]) #  Error where they are not equal
a[2] = 'c' 
print(25[0])   # ' '
print('25'[0]) # 25' '
print(True[1]) # 1
print('True'[1]) # r





#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) # 'Hyd Hyd Hyd'
print(a * 2) # 'Hyd Hyd'
print(a * 1) # 'Hyd'
print(a * 0) # Error can't be 0 times
print(a * -1) # Error (can't be -1 times)
print(25 * 3) # 75
print('25' * 3) # '25 25 25'
print('25' * 4.0) # '25 25 25 25' 
print(3 * 'Hyd') # 'Hyd Hyd Hyd;
print('25' * True) # '25'




# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a)) # Address of object a
a = a * 3  #  It  is  valid  
print(a , id(a)) # Address of object a





# len()  function  (Home  work)
print(len('Hyd')) # 3
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('')) # 1
print(len(' ')) # 2
print(len(689)) # error no length for integer object



# Find  outputs  (Home  work)
a = """"Hyd"""
print(a) # Hyd
print(len(a)) # 3
print(a[0]) # 'H'
print("""Hyd"""")   # Hyd
b = """""Hyd"""
print(b)  # syntax error
print(len(b)) # syntax error 


# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) # string  from  indexes  7  to  12  in  steps  of  1  i.e. 'D a y a a l '
print(a[7 : ]) # string  from  indexes  7  to  17  in  steps  of  1  i.e. 'D a y a l  s a r m a'
print(a[ : 6])   # string  from  indexes  0  to  6  in  steps  of  1  i.e. 'S a n k a r  '
print(a[ : ])  # string  from  indexes  0  to  17 in  steps  of  1  i.e. Sankar Dayal Sarma
print(a[:  : ])  # 'string  from  indexes  0  to  17  in  steps  of  1  i.e. Sankar Dayal Sarma'
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2]) #string  from  indexes  0  to  17  in  steps  of  2  i.e. ' Sna aa ama' 
print(a[1 : : 2]) #string  from  indexes  1  to  17  in  steps  of  2  i.e. 'akrDylSra'
print(a[-5 : -1]) #string  from  indexes  -5  to  -1  in  steps  of    i.e. 'Sarma'
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1]) #  string  from  indexes  -1  to   -5  in  steps  of  -1  i.e. 'amraS'
print(a[ : : -2]) #  string  from  indexes  -1  to   0  in  steps  of  -2  i.e. 'arSlyDrka'
print(a[3 : -3]) #  Error  in sytax
print(a[2 : -5]) # Error  in sytax
print(a[-1:-5])  #string  from  indexes  -1  to   -5 in  steps  of  -1  i.e. 'amraS'
print(a[3 : 3]) #string  from  indexes  3 to   3  in  steps  of  1 i.e.'k'



#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y     a      l                  S       a        r      m      a
#  -18   -17   -16      -15    -14    -13     -12          -11      -10     -9    -8     -7     -6          -5      -4       -3      -2      -1







#  Find  outputs  (Home  work)
a =  'A'
print(a[1]) # Error (index is not there)
print(a[1:])# string  from  indexes  1 to   1 in  steps  of  1 i.e. 'A'


















