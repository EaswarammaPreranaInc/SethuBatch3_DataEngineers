#Python Homework (Feb 11 2026)
#  Find outputs (Homework)
a = "Rama Rao"
print(a) # Rama Rao
print(type(a)) #<class str>
print(id(a)) #adress of object Rama Rao (1000)
b = 'Hyd'
print(b) #Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.

# Index   demo program (Homework)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a') #print(a[0])
print(How  to  print  'y'  of  object  'a') #print(a[1])
print(How  to  print  'd'  of  object  'a') #print(a[2])
print(How  to  print  'd'  of  object  'a') #print(a[-1])
print(How  to  print  'y'  of  object  'a') #print(a[-2])
print(How  to  print  'H'  of  object  'a') #print(a[-3])
print(a[-4]) #error there is no index -4
print(a[0] == a[-3]) #True
a[2] = 'c' #Error str is immutable
print(25[0])   #error non - sequence cannot be sliced since there is no indexing
print('25'[0]) #2
print(True[1]) #error there is no indexing for non-sequences so slicing is not possible 
print('True'[1]) #u

#  Find  outputs  (Homework)
a = 'Hyd'
print(a * 3) # prints 3 times as a single string with 9 characters HydHydHyd
print(a * 2) # HydHyd
print(a * 1) #Hyd
print(a * 0) #empty string 
print(a * -1) #empty string 
print(25 * 3) #75
print('25' * 3) #252525
print('25' * 4.0) #Error cannot multiply with float number
print(3 * 'Hyd') #HydHydHyd
print('25' * True) #25  (‘25’*1=25)

# Tricky program
#  Find  outputs  (Homework)
a = 'Hyd'
print(a, id(a)) # Hyd 1000(address of object Hyd)
a = a * 3  #  It  is  valid  (or)  invalid #valid
print(a, id(a)) #HydHydHyd 2000 now a refers to object HydHydHyd

# len()  function  (Homework)
print(len('Hyd')) #3 
print(len('Rama Rao')) #8
print(len('9247')) #4
print(len('')) #0
print(len(' ')) #1
print(len(689)) #Error integer cannot have length

# Find  outputs  (Homework)
a = """"Hyd"""
print(a) #Hyd
print(len(a)) #3
print(a[0]) #H
print("""Hyd"""")   # Hyd
b = """""Hyd"""
print(b)  # Hyd
print(len(b)) #3

# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) #Dayal (String from indexes 7 to 11 in step 1)
print(a[7 : ]) #Dayal Sarma(String from indexes 7 to 17 in step 1)
print(a[ : 6])   #Sankar (String from indexes 0 to 6 in step 1)
print(a[ : ])  #Sankar  Dayal Sarma(String from indexes 0 to 17 in step 1)
print(a[:  : ])  #Sankar Dayal Sarma (String from indexes 0 to 17 in step 1)
print(a[1 : 10 : 2])  #  string from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2]) #Sna aa am(String from indexes 0 to 17 in step 2)
print(a[1 : : 2]) #akrDylSra(String from indexes 1 to 17 in step 2)
print(a[-5 : -1])  #Sarm(String from indexes -5 to -1 in step -1)
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1]) #layaD
print(a[ : : -2]) #Dylrka
print(a[3 : -3]) #Kar Dayal Sar
print(a[2 : -5]) #nkar Dayal 
print(a[-1:-5]) # amraS
print(a[3 : 3]) #Empty String

#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1


#  Find outputs (Homework)
a = 'A'
print(a[1]) #error no index 1
print(a[1:]) #error
