#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a)  #"Rama Rao"
print(type(a)) # class string
print(id(a)) #address of the object 
b = 'Hyd'
print(b) #'Hyd'
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)#'Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'





# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a')#a[0]
print(How  to  print  'y'  of  object  'a')#a[1]
print(How  to  print  'd'  of  object  'a')#a[2]
print(a[3])  #'d'
print(How  to  print  'd'  of  object  'a')#[-1]
print(How  to  print  'y'  of  object  'a')#[-2]
print(How  to  print  'H'  of  object  'a')#[-3]
print(a[-4])#Error
print(a[0] == a[-3]) #'H'
a[2] = 'c' 
print(25[0])   #Error
print('25'[0]) #2
print(True[1]) #Error
print('True'[1])#r






#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)#'HydHydHyd'
print(a * 2)#'HydHyd'
print(a * 1)#'Hyd'
print(a * 0)#
print(a * -1)#
print(25 * 3)#75
print('25' * 3)#'252525'
print('25' * 4.0)  #'252525'
print(3 * 'Hyd')#'HydHydHyd'
print('25' * True)#'25'






# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a)) #'Hyd', address of the object
a = a * 3  #  It  is  valid  (or)  invalid #invalid
print(a , id(a))# Error





# len()  function  (Home  work)
print(len('Hyd')) # 3
print(len('Rama Rao')) # 8
print(len('9247'))  # 4
print(len(''))  # 0
print(len(' ')) # 1
print(len(689)) #Error







# Find  outputs  (Home  work)
a = """"Hyd"""
print(a) #'Hyd'
print(len(a)) # 3
print(a[0]) #'H'
print("""Hyd"""") # 'Hyd'   
b = """""Hyd"""
print(b)  # 'Hyd'
print(len(b)) # 3



# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) # Dayal
print(a[7 : ]) # Dayal sarma 
print(a[ : 6])   # Sankar
print(a[ : ])  # Sankar Dayal Sarma
print(a[:  : ])  # Sankar Dayal Sarma
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2]) # Sna aa am
print(a[1 : : 2]) # akrdylsra
print(a[-5 : -1]) # Sarm
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1]) # amra
print(a[ : : -2]) # arSlyDrka
print(a[3 : -3]) #kar Dayal Sa
print(a[2 : -5]) # nkar Dayal 
print(a[-1:-5]) # amra
print(a[3 : 3]) # k



#   0      1      2      3      4       5       6           7       8       9     10     11       12           13     14       15      16     17
#   S      a      n      k      a       r                   D       a       y      a       l                  S       a        r       m       a
#  -18   -17     -16    -15     -14    -13    -12         -11     -10      -9     -8      -7      -6          -5     -4       -3      -2      -1















#Find  outputs  (Home  work)
a =  'A'
print(a[1])# 'A'
print(a[1:])# 'A'