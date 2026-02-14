# Assignement 2  -  Pankaj - 11/2/2026


#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) # prints Rama Rao
print(type(a)) # <class 'str'>
print(id(a)) # address of reference a
b = 'Hyd' 
print(b) #prints Hyd
c = '''Hyd is green city. # this is a multi line string 
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # it prints Hyd is green city. 
#           Hyd is hitec city.
#           Hyd is beautiful city.


# Index   demo  program  (Home  work)
a = 'Hyd'
# print(How  to  print  'H'  of  object  'a') # a[0] = 'H'
# print(How  to  print  'y'  of  object  'a') # a[1] = 'y'
# print(How  to  print  'd'  of  object  'a') # a[2] = 'd'
# print(a[3])  # throws an error as it does have 4 or more characters
# print(How  to  print  'd'  of  object  'a') #a[-1] = 'd'
# print(How  to  print  'y'  of  object  'a') #a[-2] = 'y'
# print(How  to  print  'H'  of  object  'a') #a[-3] = 'H'
# print(a[-4]) # throws an error
print(a[0] == a[-3]) # gives result as True
# a[2] = 'c' #throws an error as str is immutable
# print(25[0])   # throws an error as 25 is a int and it does have indexing
print('25'[0]) # prints '2'
# print(True[1]) # throws an error as True is not string
print('True'[1]) # Prints 'r'


#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) # prints 'HydHydHyd'
print(a * 2) # prints 'HydHyd'
print(a * 1) # prints 'Hyd'
print(a * 0) # prints ' ' an empty string
print(a * -1) # prints ' ' an empty string 
print(25 * 3) # prints 75 because of the integers
print('25' * 3) # '252525'
# print('25' * 4.0)  # throws an error because we cant multiply a sequence with a float
print(3 * 'Hyd') # prints 'HydHydHyd' as it is a string 
print('25' * True) # prints '25' because True == 1 when it is with operators


# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a)) # prints 'Hyd', address of string object 
a = a * 3  #  It  is  valid  (or)  invalid # yes it valid and it a is the reference to the object 'HydHydHyd'. and previous object gets deleted.
print(a , id(a)) # prints 'HydHydHyd', address of string object


# len()  function  (Home  work)
print(len('Hyd')) # prints 3 as 'Hyd' has 3 characters
# print(len('Rama Rao') # prints 8 as 'Rama Rao'has 8 characters
print(len('9247')) # prints 4 as 9247 has 4 characters
print(len('')) # prints 0 as it is a empty string
print(len(' ')) # prints 0 as it is a empty string
# print(len(689)) # prints 690 as its length is 670. 


# Find  outputs  (Home  work)
# a = """"Hyd"""
a = "Hyd"
print(a) # prints Hyd
print(len(a)) # prints 3
print(a[0]) # prints H
# print("""Hyd"""") # throws an error as it does not have equal quotes on each side of the string.
# b = """""Hyd"""
b = '"Hyd"'
print(b)  # does not throws an error as it considers it as a double double quotes string.
print(len(b)) # prints 5


# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) # prints 'Dayal'
print(a[7 : ]) # prints 'Dayal Sarma'
print(a[ : 6])   # prints 'Sankar'
print(a[ : ])  # prints 'Sankar Dayal Sarma'
print(a[:  : ])  # prints 'Sankar Dayal Sarma'
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2]) # prints 'Sna aa am'
print(a[1 : : 2]) # prints 'akrdylsra'
print(a[-5 : -1]) # prints ' Sarm'
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1]) # prints 'amra'
print(a[ : : -2]) # prints 'arslydrka'
print(a[3 : -3]) # prints 'kar dayal Sa'
print(a[2 : -5]) # prints 'kar Dayal '
# print(a[-1:-5]) # prints 'amra' -------------------------------------------------------------------------
print(a[3 : 3]) # prints ' ' empty string


#  Find  outputs  (Home  work)
a =  'A'
# print(a[1]) # throws an error as it has no 1 index
print(a[1:]) # throws an error as it has no 1 index
