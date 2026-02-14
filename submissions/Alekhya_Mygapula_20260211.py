PYTHON HOMEWORK DAY3
ALEKHYA MYGAPULA



a = "Rama Rao"
print(a) #Rama Rao
print(type(a)) #<class string>
print(id(a))  #address of the object Rama Rao
b = 'Hyd'
print(b)  # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)  #Hyd is green city.Hyd is hitec city.Hyd is beautiful city.



a = 'Hyd'
print(How  to  print  'H'  of  object  'a') #Hyd[0]
print(How  to  print  'y'  of  object  'a') #Hyd[1]
print(How  to  print  'd'  of  object  'a') #Hyd[2]
print(a[3])   #Error due to not correct syntax
print(How  to  print  'd'  of  object  'a') #Hyd[-1]
print(How  to  print  'y'  of  object  'a') #Hyd[-2]
print(How  to  print  'H'  of  object  'a')#Hyd[-3] 
print(a[-4]) #Error no index value
print(a[0] == a[-3]) #true
a[2] = 'c'  #error
print(25[0])   #Error
print('25'[0]) #25
print(True[1]) #Error
print('True'[1]) #r



a = 'Hyd'
print(a * 3) #HydHydHyd
print(a * 2) #HydHyd
print(a * 1) #Hyd
print(a * 0) #nothing will print
print(a * -1)#nothing will print
print(25 * 3) #75
print('25' * 3) #252525
print('25' * 4.0)  #Error
print(3 * 'Hyd') #HydHydHyd
print('25' * True) 25


a = 'Hyd'
print(a , id(a))  #Hyd , addressof the object Hyd
a = a * 3  #  It  is  valid  (or)  invalid #HydHydHyd
print(a , id(a))#  #Hyd , addressof the object Hyd




print(len('Hyd')) #3
print(len('Rama Rao' )) #8
print(len('9247')) #4
print(len(''))#0
print(len(' ')) #1
print(len(689)) #Error len not works


a = """"Hyd"""
print(a) #Error
print(len(a))
print(a[0]) 
print("""Hyd"""")   #Error
b = """""Hyd""" 
print(b)  
print(len(b))



a = 'Sankar Dayal Sarma'
print(a[7 : 12]) #Dayal
print(a[7 : ]) #Dayal Sarma
print(a[ : 6])   #Sankar
print(a[ : ])  #Sankar Dayal Sarma
print(a[:  : ])  #Sankar Dayal Sarma
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2]) #SnarDylSra
print(a[1 : : 2]) #akr ayaam
print(a[-5 : -1]) #Sarm
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1]) #amra
print(a[ : : -2]) #ara aa nkS
print(a[3 : -3]) #kar 
print(a[2 : -5]) #nkar Dayal
print(a[-1:-5])#Error
print(a[3 : 3]) # Empty



#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1



a =  'A'
print(a[1]) #Error due to no index 
print(a[1:]) #empty string