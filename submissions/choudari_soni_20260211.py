#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a)  #Rama Rao
print(type(a))  #<class 'str'>
print(id(a))  #address of the object "Rama Rao"
b = 'Hyd'
print(b)  #Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)     #Hyd is green city.
	      Hyd is hitec city.
	      Hyd is beautiful city.
_________________________________________

# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a')    # Hyd[0]
print(How  to  print  'y'  of  object  'a')    # Hyd[1]
print(How  to  print  'd'  of  object  'a')    # Hyd[2]

print(a[3])   #error because a has only 3 characters
print(How  to  print  'd'  of  object  'a')    # Hyd[-1]
print(How  to  print  'y'  of  object  'a')    # Hyd[-2]
print(How  to  print  'H'  of  object  'a')    # Hyd[-3]
print(a[-4])  # error because a has only 3 characters 
print(a[0] == a[-3])  # Yes
a[2] = 'c' 
print(25[0])   # error because sting is always inside the quotes
print('25'[0]) # 2
print(True[1]) # error because no string

print('True'[1]) # r
__________________________________________________

#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)    # HydHydHyd
print(a * 2)    # HydHyd'
print(a * 1)    # Hyd
print(a * 0)    # Empty string
print(a * -1)   # Error because repetation cannot take negative values
print(25 * 3)   # 75
print('25' * 3) # 252525
print('25' * 4.0)  # error because  there is a float number
print(3 * 'Hyd')  #error because repetation and string in wrong place
print('25' * True)  # 25

________________________________________________

# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))  # 'Hyd'  address of the object 'Hyd'
a = a * 3  #  It  is  valid  (or)  invalid   # valid 
print(a , id(a))  # HydHydHyd address of the object HydHydHyd
_______________________________________________

# len()  function  (Home  work)
print(len('Hyd'))    # 3
print(len('Rama Rao')) # 8
print(len('9247'))     # 4
print(len(''))         # 0
print(len(' '))        # 1
print(len(689))       # error because 689 in not a string
_____________________________________________


# Find  outputs  (Home  work)
a = """"Hyd"""
print(a)  # "Hyd
print(len(a))  # 4
print(a[0])    # "
print("""Hyd"""")   # error because there are 4 qutoes
b = """""Hyd"""
print(b)      #"" Hyd
print(len(b))  # 5
____________________________________________


# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])   #a[7 : 12:1] (string  from  indexes  7 to   11  in  steps  of  1) i.e:Dayal
print(a[7 : ])     # a[7 : 18:1]( string  from  indexes  7  to   17 in  steps  of  1) i.e: Dayal Sarma
print(a[ : 6])     # a[0 : 6:1] (string  from  indexes  0  to   5  in  steps  of  1) i.e:Sankar
print(a[ : ])     # a[0 : 18:1]( string  from  indexes  0  to   17 in  steps  of  1) i.e:Sankar Dayal Sarma
print(a[:  : ])   # a[0: 18:1] (string  from  indexes  0 to   17  in  steps  of 1 )i.e:Sankar Dayal Sarma

print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2])    # a[0: 18:2] (string  from  indexes  0 to  17  in  steps  of 2) i.e: sna aa am
print(a[1 : : 2])   # a[1: 18:2] (string  from  indexes 1   to   17 in  steps  of 2) i.e: akrDylSra
print(a[-5 : -1])  # a[-5: -2:1] (string  from  indexes  -5  to   -2 in  steps  of) 1 i.e:sarm

print(a[::-1])      # a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1])  #(string  from  indexes  -1  to   -6 in  steps  of  -1)  i.e. amras
print(a[ : : -2])   #a[-1 : -19: -2] (string  from  indexes  -1  to   -18  in  steps  of  -2) i.e. arSlyDrka
print(a[3 : -3])    #a[3 : -3:1](string  from  indexes  3  to   -4  in  steps  of  1) i.e.kar Dayal Sa
print(a[2 : -5])    #a[2 : -5:1](string  from  indexes  2 to   -6 in  steps  of  1) i.e.nkar Dayal 
print(a[-1:-5])    #a[-1:-5:1](string  from  indexes  -1 to   -6 in  steps  of  1) i.e.amraS 
print(a[3 : 3])    # Empty String



#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1
____________________________________________________


#  Find  outputs  (Home  work)
a =  'A'
print(a[1])   #error  because there is no index value 1
print(a[1:])  #empty string