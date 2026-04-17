# Find outputs (Home work)
a = "Rama Rao"
print(a) #O/P : Rama Rao
print(type(a)) #O/P : <class ‘str’>
print(id(a)) #O/P : address of object “Rama Rao”
b = 'Hyd'
print(b) #O/P : Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)
'''O/P :
Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''


# Index demo program (Home work)
a = 'Hyd'
print(How to print 'H' of object 'a') #O/P : print(a[0])
print(How to print 'y' of object 'a') #O/P : print(a[1])
print(How to print 'd' of object 'a') #O/P : print(a[2])
print(a[3]) #O/P : error
print(How to print 'd' of object 'a') #O/P : print(a[-1])
print(How to print 'y' of object 'a') #O/P : print(a[-2])
print(How to print 'H' of object 'a') #O/P : print(a[-3])
print(a[-4]) #O/P : error
print(a[0] == a[-3]) #O/P : True
a[2] = 'c'
print(25[0]) #O/P : error
print('25'[0]) #O/P : 2
print(True[1]) #O/P : error
print('True'[1]) #O/P : r
# Find outputs (Home work)
a = 'Hyd'
print(a * 3) #O/P : ‘HydHydHyd’
print(a * 2) #O/P : ‘HydHyd’
print(a * 1) #O/P : ‘Hyd’
print(a * 0) #O/P : error
print(a * -1) #O/P : error
print(25 * 3) #O/P : 75
print('25' * 3) #O/P : 252525
print('25' * 4.0) #O/P : error
print(3 * 'Hyd') #O/P : error
print('25' * True) #O/P : 25 *1 =25






# Tricky program
# Find outputs (Home work)
a = 'Hyd'
print(a , id(a))
a = a * 3 # It is valid (or) invalid a = 'Hyd' , #O/P : valid
print(a , id(a))
a = a * 3 # It is valid (or) invalid #O/P :
print(a , id(a)) #O/P : ‘Hyd’ , <some address location.>
# len() function (Home work)
print(len('Hyd')) #O/P : 3
print(len('Rama Rao')) #O/P : 8
print(len('9247')) #O/P : 4
print(len('')) #O/P : 0
print(len(' ')) #O/P : 0
print(len(689)) #O/P : error


# Find outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) #O/P : _Dayal
print(a[7 : ]) #O/P : Dayal sarma
print(a[ : 6]) #O/P : Sankar
print(a[ : ]) #O/P : Sankar Dayal Sharma
print(a[: : ]) #O/P : Sankar Dayal sarma
print(a[1 : 10 : 2]) # string from indexes 1 to 9 in steps of 2 i.e. akrDy
print(a[0 : : 2]) #O/P : Sna aa am
print(a[1 : : 2]) #O/P : akrDy1Sra
print(a[-5 : -1]) #O/P : Sarm
print(a[::-1]) # a[-1 : -19 : -1] ---> string from indexes -1 to -18 in steps of -1 i.e. Reverse
string #O/P : amraS layaD raknaS
print(a[-1:-5:-1]) #O/P : amra
print(a[ : : -2]) #O/P : arSlyDrkns
print(a[3 : -3]) #O/P : kar Dayal Sar
print(a[2 : -5]) #O/P : nkar Dayal
print(a[-1:-5]) #O/P : amra
print(a[3 : 3]) #O/P : empty string
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
# S a n k a r D a y a l S a r m a
# -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# Find outputs (Home work)
a = 'A'
print(a[1]) #O/P : error
print(a[1:]) #O/P: empty
