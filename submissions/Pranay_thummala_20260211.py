#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) 		# Rama Rao
print(type(a)) 		# <class 'str'>
print(id(a))		# 135954579937968
b = 'Hyd' 
print(b) 		# Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)    

#Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.

# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a') 	# print(a[0])
print(How  to  print  'y'  of  object  'a') 	# print(a[1])
print(How  to  print  'd'  of  object  'a') 	# print(a[2])
print(a[3])   					# Error
print(How  to  print  'd'  of  object  'a') 	# print(a[2])
print(How  to  print  'y'  of  object  'a') 	# print(a[1])
print(How  to  print  'H'  of  object  'a') 	# print(a[0])
print(a[-4]) 		# error
print(a[0] == a[-3]) 	# True
a[2] = 'c' 		# Error
print(25[0]) 		# Error
print('25'[0]) 		# 2
print(True[1]) 		# Error
print('True'[1]) 	# r


a = 'Hyd'

print(a * 3) 		# HydHydHyd
print(a * 2) 		# HydHyd
print(a * 1) 		# Hyd
print(a * 0) 		# 
print(a * -1) 		# 
print(25 * 3) 		# 75
print('25' * 3) 	# 252525
print('25' * 4.0) 	# Error
print(3 * 'Hyd') 	# HydHydHyd
print('25' * True) 	# 25


# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))  	# Hyd 133454886394672
a = a * 3  #  It  is  valid  (or)  invalid
print(a , id(a))	# HydHydHyd 133454886411760


# len()  function  (Home  work)
print(len('Hyd')) 	# 3
print(len('Rama Rao')) 	# 8
print(len('9247')) 	# 4
print(len('')) 		# 0
print(len(' ')) 	# 1
print(len(689)) 	# error



# Find  outputs  (Home  work)
a = """"Hyd"""
print(a) 	# "Hyd
print(len(a))  	# 4
print(a[0]) 	# "
print("""Hyd"""") # Error
b = """""Hyd"""
print(b) 	# ""Hyd
print(len(b))  	# 5


a = 'Sankar Dayal Sarma'

print(a[7 : 12]) 	# Dayal
print(a[7 : ]) 		# Dayal Sarma
print(a[ : 6]) 		# Sankar
print(a[ : ])  		# Sankar Dayal Sarma
print(a[:  : ]) 	# Sankar Dayal Sarma
print(a[1 : 10 : 2]) 	# akrDy
print(a[0 : : 2]) 	# SnarDylSra
print(a[1 : : 2]) 	# aka aa am
print(a[-5 : -1]) 	# Sarm
print(a[::-1]) 		# amraS layaD raknaS
print(a[-1:-5:-1]) 	# amra
print(a[ : : -2]) 	# arSlaa rknS
print(a[3 : -3]) 	# kar Dayal Sa
print(a[2 : -5]) 	# nkar Dayal 
print(a[-1:-5]) 	# 
print(a[3 : 3]) 	#


#  Find  outputs  (Home  work)
a = 'A'
print(a[1]) 	# error
print(a[1:]) 	#
