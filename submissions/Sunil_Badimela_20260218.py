# Find  outputs (Home  work)
a = 25.7
print(id(a))     #some memory address

print(a)     #25.7

a = 35.6
print(id(a))     #new memory address

print(a)     #35.6

b = True
print(id(b))     #Prints memory address of True

b = False
print(id(b))     #id of False

c = None
print(id(c))     #Prints memory address of None

c = None
print(id(c))     #Reassigning None does NOT create a new object







#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))     #Prints memory address of string 'Hyd'

a[1] = 'e'   #Error  'str' object does not support item assignment

a = 'Sec'     #Now a refers to a new string object

print(id(a))     #New memory address will be printed

b = (10 , 20 , 15 , 18)  #Prints memory address

print(id(b))     #Tuple is immutable

b[2] = 19  #Error  'tuple' object does not support item assignment

b = (30 , 40 , 35 , 32)     #New tuple object created

print(id(b))     #New memory address printed

c = range(5)     
print(id(c))     #range object is immutable

c[3] = 10     #Error 'range' object does not support item assignment

c = range(5)     #New range object created

print(id(c))     #New memory address printed









# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)     #True

c = 'Hyd'
d = 'Hyd'
print(c  is  d)     #True

e = False
f = False
print(e  is  f)     #True

g = range(10)
h = range(10)
print(g  is  h)     #False










#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)     #False

c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)     #False

e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)     #True

g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)     #False










# Find outputs (Home work)
print(10 + 20)    #30

print(10.8 + 20.6)    #31.4

print(3 + 4j + 5 + 6j)    #(8+10j)

print(True + False)    #1

print('Hyder' + 'abad')    #Hyderabad

print('Sankar' + 'Dayal' + 'Sarma')    #SankarDayalSarma

print('10' + '20')    #1020

print([10 , 20 , 30] + [1 , 2 , 3])    #[10, 20, 30, 1, 2, 3]

print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))    #(25, 10.8, 'Hyd', (3+4j), True, None)

print({10 , 20} + {30 , 40})    # error Sets do not support +

print({10 : 'Hyd'} + {20 : 'Sec'})    #error Dictionaries do not support +

print(range(4) + range(5))    #error Range does not support +

print(10 + '20')    #error Cannot add int and string

print([10 , 20 , 30] + 5)    #error

print([10 , 20 , 30] + (40 , 50 , 60))    #error List + Tuple not allowed










# Find outputs (Home work)
print(25 * 3)    #75

print(10.8 * 25.6)    #276.48

print(True * False)    #0

print((3 + 4j) * (5 + 6j))    #(-9+38j)

print(3 + 4j * 5 + 6j)    #(3+26j)

print('25' * 3)    #252525

print(3 * '25')    #252525

print('Hyd' * 4)    #HydHydHydHyd

print([10 , 20 , 15] * 2)    #[10, 20, 15, 10, 20, 15]

print((25, 10.8, 'Hyd', True) * 3)    #(25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)

print([10 , 20 , 15] * 3.0)    #Error:   can't multiply sequence by non-int of type 'float

print({10 , 20 , 15} * 2)    #error Set does not support *

print({10 : 20 , 30 : 40} * 2)    #error

print([10] * [20])    #error Error: can't multiply sequence by non-int of type 'list'






