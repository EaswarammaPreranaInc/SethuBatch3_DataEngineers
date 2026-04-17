String Output Homework

a = "Rama Rao"
print(a) #Rama Rao
print(type(a)) #class ‘str’
print(id(a)) #address of the str object ‘Rama Rao’

b = 'Hyd'
print(b) #Hyd

c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) #Hyd is green city.
#Hyd is hitec city.
#Hyd is beautiful city.


Indexing Homework

a = 'Hyd'
print(How  to  print  'H'  of  object  'a') #a[0]
print(How  to  print  'y'  of  object  'a') #a[1]
print(How  to  print  'd'  of  object  'a') #a[2]
print(a[3]) #error because str a has only 3 indexes; 0, 1, 2

print(How  to  print  'd'  of  object  'a') #a[-1]
print(How  to  print  'y'  of  object  'a') #a[-2]
print(How  to  print  'H'  of  object  'a') #a[-3]
print(a[-4]) #error because str a has only 3 negative indexes; -1, -2, -3

print(a[0] == a[-3]) #True
a[2] = 'c' #error because a[2] is an index value that is already assigned to ‘d’
 
print(25[0]) #error because int objects can not be indexed as they are non-sequenced
print('25'[0]) #2

print(True[1]) #error because bool values cannot be indexed as they are non-sequenced
print('True'[1]) #r


Outputs Homework #1

a = 'Hyd'
print(a * 3) #’HydHydHyd’
print(a * 2) #’HydHyd’
print(a * 1) #’Hyd’
print(a * 0) #empty str
print(a * -1) #empty str

print(25 * 3) #75
print('25' * 3) #’252525’
print('25' * 4.0) #error because a str cannot be multiplied a float number of times

print(3 * 'Hyd') #’HydHydHyd’
print('25' * True) #’25’


Tricky Program Outputs Homework

a = 'Hyd'
print(a , id(a)) #’Hyd’, address of the str object ‘Hyd’

a = a * 3  #  It  is  valid  (or)  invalid #valid because reference names can replace themselves
print(a , id(a)) #’HydHydHyd, address of the str object ‘HydHydHyd’


Length [len()]  Function Homework

print(len('Hyd')) #3
print(len('Rama Rao')) #8
print(len('9247')) #4
print(len('')) #0
print(len(' ')) #1
print(len(689)) #error because len() cannot be assigned to an int object


Outputs Homework #2

a = """"Hyd"""
print(a) #’Hyd’
print(len(a)) #3
... print(a[0]) #’H’
... print("""Hyd"""") #’Hyd’   
... 
... b = """""Hyd""" 
... print(b)  #’””Hyd’
... print(len(b)) #5
... SLICE Homework
... 
... a = 'Sankar Dayal Sarma'
... print(a[7 : 12]) #’Dayal’ #string from indexes 7 to 11 in steps of 1 (default)
... print(a[7 : ]) #’Dayal Sarma’ #string from indexes 7 to len (default)
... print(a[ : 6]) #’Sankar’ #string from indexes 0 (default) to 5
... print(a[ : ]) #’Sankar Dayal Sarma’ #string from indexes 0 (default) to len (default)
... print(a[:  : ]) #’Sankar Dayal Sarma’ #string from indexes 0 (default) to len (default) in steps of 1 (default)
... print(a[1 : 10 : 2]) #string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
... print(a[0 : : 2]) #’Sna aa am’ #string from indexes 0 to len (default) in steps of 2
... print(a[1 : : 2]) #’akrDylSra’ #string from indexes 1 to len(default) in steps of 2
... print(a[-5 : -1]) #’Sarm’ #string from indexes -5 to -2
... print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
... print(a[-1:-5:-1]) #’amra’ #string from indexes -1 to -4 in steps of -1
... print(a[ : : -2]) #’arSlyDrka’ #string from indexes -1 to -18 in steps of -2
... print(a[3 : -3]) #’kar Dayal Sa’ #string from indexes 3 to -4(14) in steps of 1
... print(a[2 : -5]) #’nkar Dayal ‘ #string from indexes 2 to -6(12) in steps of 1 
... print(a[-1:-5]) #empty str #string from indexes -1 to -4 which isn’t possible unless the step of -1 or so is stated
... print(a[3 : 3]) #empty str #string from indexes 3 to 2 (which isn’t possible) in steps of 1
... 
... 
... 
... 
... 0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17
... S	a	n	k 	a	r		D	a	y	a	l		S	a	r	m	a
-18	-17	-16	-15	-14	-13	-12	-11	-10	-9	-8	-7	-6	-5	-4	-3	-2	-1

