'''
a = [10 , 20 , 15 ,  18 , 12]
k = 3
Shift  right  list  'a'  for  'k'  times   --->  [15 , 18 , 12 , 10 , 20]

def   rotate(a):  #  'a'  is  list
	shift   right  only  once
	[10 , 20 , 15 , 18 , 12]   --->  [12 , 10 , 20 , 15 , 18]
#  End  of  the  function	
Read  list   'a'
Read  'k' 
call  rotate()  'k'  times
k = 3
After  1st  call   -->  [12 , 10 , 20 , 15 , 18]
After  2nd   call   -->  [18 , 12 , 10 , 20 , 15]
After  3rd   call   -->  [15 , 18 , 12 , 10 , 20]
'''
def rotate(a):
    if ch == 'right':
        x = a[-1]
        a.pop()
        a.insert(0, x)
    else:
        x = a[0]
        a.pop(0)
        a.append(x)

a = eval(input('Enter list: '))
k = int(input('Enter k: '))
ch = input('Enter left or right: ').lower()

for i in range(k):
    rotate(a)
print(a)

# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   list)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
#  Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j ,  'Hyd' , True]
f = filter(lambda  x  :  False ,  list)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda  x : x , list)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
# Find outputs
import  time
def  disp(f):
	while  True:
		try:
			print(next(f))
			time . sleep(1)
		except:
			break
list = [10 , 0 ,  -25 , () , (25,) , 'Hyd', '' , [] , 10.8 , 0.0 , [10 , 20] , True , False]
f1 = filter(lambda  x : None  , list)
print('Filter  f1')
disp(f1)
f2 = filter(None  , list)
print('Filter  f2')
disp(f2)

# Find outputs  (Home  work)
import  time
list = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

# Find  outputs (Home  work)
import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda  x : x[1]  >=  12 , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

# Find  outputs (Home  work)
import   time
list = [{'Roll Num' :  10 , 'Stud Name' : 'Rama Rao' , 'Marks' : 75} ,
          {'Roll Num' :  20 , 'Stud Name' : 'Sita' , 'Marks' : 52} ,
          {'Roll Num'  :  15 , 'Stud Name' : 'Kiran' , 'Marks' : 65} ,
          {'Roll Num'  :  18 , 'Stud Name' : 'Amar' ,  'Marks' : 48} ,
          {'Roll Num' :  5 , 'Stud Name' : 'Rajesh' , 'Marks' : 82}]  
f = filter(lambda  x :  x['Marks'] >= 60 , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

# Find  outputs (Home  work)
import  time
def  disp(f):
	while  True:
		try:
			print(next(f))
			time . sleep(1)
		except:
			break
list = [{'country' : 'India' , 'sale' : 150.5} ,
          {'country' : 'china' , 'sale' : 200.2} ,
          {'country' : 'USA' , 'sale' : 300.3} ,
          {'country' : 'UK' , 'sale' : 210.4} ]
f1 = filter(lambda  x  :   x['country'] . startswith('U') , list)
print('Filter  f1')
disp(f1)
f2 = filter(lambda  x  :  x['sale']  >=  200  , list)
print('Filter  f2')
disp(f2)

# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f1 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  thru  filter  object  with   next   function')
How  to  iterate  thru  filter  object  with  next()  function
print('Iterate  thru  filter  object  with   for  loop')
How  to  iterate  thru  filter  object  with  for  loop
print('Unpack  filter  object :  ' ,  ???)
print('filter  object  converted  to   list  :  ' ,  ???)

#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
def odd(x):
    return x % 2 != 0
num = range(1, 21)
f = filter(odd, num)
for i in f:
    print(i)

'''
Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set
'''
def vowels(x):
    return x in 'AEIOU'
s = input('Enter string: ')
s = s.upper()   
f = filter(vowels, s)
print(set(f))

# Nested  filter  i.e.  filter  on  filter
import   time
list =  [ (10 , 'Rama' , 10000.0) ,
            (20, 'Sita' , 7000.0) ,
            (15 , 'Rajesh' , 15000.0) ,
            (5 , 'Amar' ,  12000.0) ,
            (18 , 'Ramesh' , 8000.0) ]
f = filter(lambda  x :  x[1] . startswith('R')  , filter(lambda  x :  x[2] >= 10000 , list))
while   True:
	try:
		print(next(f))
		time .  sleep(1)
	except:
		break
'''
(10, 'Rama', 10000.0)
(15, 'Rajesh', 15000.0)
'''