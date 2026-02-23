a = "Rama Rao"
print(a) # Rama Rao
print(type(a))# <class 'str'>
print(id(a)) #1712567
b = 'Hyd'
print(b) # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) #Hyd is green city.
#Hyd is hitec city.
#Hyd is beautiful city

a = 'Hyd'
# print(How  to  print  'H'  of  object  'a') = a[0]
#print(How  to  print  'y'  of  object  'a') = a[1]
#print(How  to  print  'd'  of  object  'a') = a[2]
#print(a[3])   # error
#print(How  to  print  'd'  of  object  'a') = a[-1]
#print(How  to  print  'y'  of  object  'a') = a[-2]
#print(How  to  print  'H'  of  object  'a') = a[-3]
#print(a[-4]) error
print(a[0] == a[-3])# True
# a[2] = 'c' error
#print(25[0]) error   
print('25'[0]) # 2 
#print(True[1])# error
print('True'[1])#r

a = 'Hyd'
print(a * 3) #HydHydHyd
print(a * 2) #HydHyd
print(a * 1) # Hyd
print(a * 0) 
print(a * -1)
print(25 * 3) #75
print('25' * 3)#252525
#print('25' * 4.0) # error
#print(3 * 'Hyd') #HydHydHyd 
print('25' * True)#25


#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))  # Hyd, 17465
a = a * 3  #  It  is  valid  (or)  invalid = valid
print(a , id(a)) #HydHydHyd , 20653636


print(len('Hyd')) #3
print(len('Rama Rao'))#8
print(len('9247'))#4
print(len(''))#0
print(len(' '))#1
# print(len(689))#error

a = """"Hyd"""
print(a) #"Hyd
print(len(a)) #4
print(a[0]) # "
#print("""Hyd"""") = Error
b = """""Hyd"""
print(b)  # ""Hyd
print(len(b))#5

a = 'Sankar Dayal Sarma'
print(a[7 : 12])  # Dayal
print(a[7 : ])  # Dayal Sarma
print(a[ : 6]) # Sankar  
print(a[ : ]) # Sankar Dayal Sarma 
print(a[:  : ])  # Sankar Dayal Sarma
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2]) #sna aa am
print(a[1 : : 2]) #akrDylSra
print(a[-5 : -1]) # arma
print(a[::-1])  #    a[-1 : -19 : -1]  ---> this for reversing string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1])#amra
print(a[ : : -2]) # arSlyDrka
print(a[3 : -3]) # kar Dayal Sa
print(a[2 : -5]) #nkar Dayal
print(a[-1:-5])# never ends
print(a[3 : 3]) # if it is stop at 4 then only 3 will be printed or else empty string
