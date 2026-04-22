a = [10 , 20 , 15 ,  18 , 12]
k = 3
# Shift  right  list  'a'  for  'k'  times   --->  [15 , 18 , 12 , 10 , 20]
def   rotate(a):  #  'a'  is  list
	# shift   right  only  once
	# [10 , 20 , 15 , 18 , 12]   --->  [12 , 10 , 20 , 15 , 18]
    a = a[-1:] + a[:-1]
    return a
#  End  of  the  function
# Read  list   'a'
a = eval(input("enter list: "))
# Read  'k'
k = int(input("enter no. of iterations:"))
# call  rotate()  'k'  times
for i in range(k):
    a = rotate(a)
    print(a)
# k = 3
# After  1st  call   -->  [12 , 10 , 20 , 15 , 18]
# After  2nd   call   -->  [18 , 12 , 10 , 20 , 15]
# After  3rd   call   -->  [15 , 18 , 12 , 10 , 20]

# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   list)
while  True:
	try:
		print(next(f)) # 25 <1sec> \n 10.8 <1sec> \n 3+4j <1sec> \n 'Hyd' <1sec> \n False
		time . sleep(1)
	except:
		break

#  Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j ,  'Hyd' , True]
f = filter(lambda  x  :  False ,  list)
while  True:
	try:
		print(next(f)) # Nothing will be printed as filter is returning False for all elements
		time . sleep(1)
	except:
		break
	
# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda  x : x , list)
while  True:
	try:
		print(next(f)) # 25 <1sec> \n 10.8 <1sec> \n Hyd <1sec> \n (25,) <1sec> \n 
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
print('Filter  f1') # Filter  f1
disp(f1) # nothing will be printed
f2 = filter(None  , list) 
print('Filter  f2') # Filter  f2
disp(f2) #  10 <1sec> \n -25 <1sec> \n (25,) <1sec> \n 'Hyd' <1sec> \n 10.8 <1sec> \n [10, 20] <1sec> \n True <1sec> \n False

# Find outputs  (Home  work)
import  time
list = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , list)
while   True:
	try:
		print(next(f)) # Rama Rao <1sec> \n Rajesh <1sec> \n Kiran <1sec> \n Manohar <1sec> \n Vamsi <1sec>
		time . sleep(1)
	except:
		break

# Find  outputs (Home  work)
import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda  x : x[1]  >=  12 , list)
while   True:
	try:
		print(next(f)) # ('B', 20) <1sec> \n ('C', 15) <1sec> \n ('E', 18) <1sec> \n
		time . sleep(1)
	except:
		break

# Find  outputs 
import   time
list = [{'Roll Num' :  10 , 'Stud Name' : 'Rama Rao' , 'Marks' : 75} ,
          {'Roll Num' :  20 , 'Stud Name' : 'Sita' , 'Marks' : 52} ,
          {'Roll Num'  :  15 , 'Stud Name' : 'Kiran' , 'Marks' : 65} ,
          {'Roll Num'  :  18 , 'Stud Name' : 'Amar' ,  'Marks' : 48} ,
          {'Roll Num' :  5 , 'Stud Name' : 'Rajesh' , 'Marks' : 82}]  
f = filter(lambda  x :  x['Marks'] >= 60 , list)
while   True:
	try:
		print(next(f)) # Roll Num' :  10 , 'Stud Name' : 'Rama Rao' , 'Marks' : 75 <1sec> \n 'Roll Num' :  15 , 'Stud Name' : 'Kiran' , 
		# 'Marks' : 65 <1sec> \n 'Roll Num' :  5 , 'Stud Name' : 'Rajesh' , 'Marks' : 82 <1sec> \n
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
print('Filter  f1') # Filter  f1
disp(f1) # 'country' : 'USA' , 'sale' : 300.3 <1sec> \n 'country' : 'UK' , 'sale' : 210.4
f2 = filter(lambda  x  :  x['sale']  >=  200  , list)
print('Filter  f2') # Filter  f2
disp(f2) # 'country' : 'china' , 'sale' : 200.2 <1sec> \n 'country' : 'USA' , 'sale' : 300.3 <1sec> \n 'country' : 'UK' , 'sale' : 210.4

# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f1 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  thru  filter  object  with   next   function')
# How  to  iterate  thru  filter  object  with  next()  function
while True :
    try :
        print(next(f1))
    except StopIteration :
        break
print('Iterate  thru  filter  object  with   for  loop') # Iterate  thru  filter  object  with   for  loop
# How  to  iterate  thru  filter  object  with  for  loop
f2 = filter(lambda  x  :  x  %  2  ==  0 , a)
for x in f2 :
    print(x)
f3 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Unpack  filter  object :  ' ,  *f3)
f4 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('filter  object  converted  to   list  :  ' ,  list(f4))

#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
f1 = filter (lambda x: x%2 == 0, range(20))
print(list(f1))

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
		print(next(f)) # 10, 'Rama' , 10000.0 <1sec> \n 15 , 'Rajesh' , 15000.0 <1sec> \n   
		time .  sleep(1)
	except:
		break