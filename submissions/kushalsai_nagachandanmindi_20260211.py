#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a)		# Rama Rao
print(type(a))	# class ‘str’
print(id(a))		# address of the object ‘a’
b = 'Hyd'
print(b)		# Hyd
c = '''Hyd is green city.	
Hyd is hitec city.	
Hyd is beautiful city.'''		# Hyd is green city.	
print(c)				   Hyd is hitec city.	
   Hyd is beautiful city.
# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object 'a') # a[0]
print(How  to  print  'y'  of  object  'a') # a[1]
print(How  to  print  'd'  of  object  'a') # a[2]
print(a[3])  # Error
print(How  to  print  'd'  of  object  'a') # a[-1]
print(How  to  print  'y'  of  object  'a') # a[-2]
print(How  to  print  'H' of  object  'a') # a[-3]
print(a[-4]) # Error
print(a[0] == a[-3]) # True
a[2] = 'c'  # Error
print(25[0])   # Error
print('25'[0]) # 2
print(True[1]) # Error
print('True'[1]) # r


#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) # ‘HydHydHyd’
print(a * 2) # ‘HydHyd’
print(a * 1) # ‘Hyd’
print(a * 0) 
print(a * -1)
print(25 * 3) # 75
print('25' * 3) # ‘252525’
print('25' * 4.0)  # Error
print(3 * 'Hyd') # ‘HydHydHyd’
print('25' * True) # ‘25’
# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))  # Hyd address of the a 
a = a * 3  #  It  is  valid  (or)  invalid
print(a , id(a)) # valid HydHydHyd same address 
# len()  function  (Home  work)
print(len('Hyd')) # 3
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('')) # 0
print(len(' ')) # 1
print(len(689)) # Error
# Find  outputs  (Home  work)
a = """"Hyd"""
print(a) # “Hyd
print(len(a)) # 4
print(a[0]) “
print("""Hyd"""") # Error   
b = """""Hyd""" 
print(b)  # “”Hyd
print(len(b)) # 5
# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) # Dayal
print(a[7 : ])  # Dayal Sarma
print(a[ : 6])   # Sankar
print(a[ : ])   # Sankar Dayal Sarma
print(a[:  : ])  Sankar Dayal Sarma
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2]) # akrDy
print(a[1 : : 2]) # Sna aa am
print(a[-5 : -1]) # akrDylSra
print(a[::-1])  #  a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1]) # Sarm
print(a[ : : -2]) # amraS layaD raknaS
print(a[3 : -3]) # amra
print(a[2 : -5]) # arSlyDrka
print(a[-1:-5]) # kar Dayal Sa
print(a[3 : 3]) #

#  Find  outputs  (Home  work)
a =  'A'
print(a[1]) # Error
print(a[1:])
