# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  --->static variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  --->instance variable
		z = 30   #  What  is  variable   'z'  --->local vaiable
		c1 . m = 40   #  What  is  variable   'm'  --->static variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  --->instance variable
	c1 . q = 60   #  What  is  variable   'q'  --->static variable
	s = 70   #  What  is  variable   's'  --->local variable
#end of the function
k = 80   #  What  is  variable 'k'  --->global variable
c1 . l = 90   #  What  is  variable  'l'  --->static variable
b = c1()
b . n = 100   #  What  is  variable  'n' --->instance variable





# Find  outputs (Home work)
class  Person:
	def  __init__(self):
		self . name  =  ''
	@property
	def   name(self):
		print('getter  method')
		return  self . _name
	@name . setter
	def   name(self , value):
		print('Setter  Method')
		self .  _name = value
	@name . deleter
	def  name(self):
		print('Deleter  method ')
		del  self .  _name
	def   __del__(self):
		print('Destructor')
# End  of  the  class
p = Person()
print(p . name)
p . name = 'Vamsi'
print(p . name)
del   p . name
print(p . name)
del   p

'''
Setter method
Getter method
''
Setter method
getter method
Vamsi
Deleter method
error
Destructor
'''






# Find  outputs (Home  work)
import   time
list = [25 , 10.8 , 'Hyd' , True]
e = enumerate(list , start = 5)
while   True:
	try:
		print(next(e))
		time . sleep(1)
	except  StopIteration:
		break
print(list[5])

'''
(5,25)
(6,10.8) 
(7,'Hyd') 
(8,True)
error
'''







'''  (Home  work)
Can  string  be  enumerated ?
'''
import   time
a = input('Enter  any  string  :  ') #  Assume  that  input  is  'Hyd'
e = enumerate(a)
while   True:
	try:
		print(next(e))
		time . sleep(1)
	except  StopIteration:
		break

'''
(0,H) 
(1,y) 
(2,d)
'''







#  Can  set  be  enumerated  ?  (Home  work)
import  time
a = {25 , 10.8 , 'Hyd' , True , 3+4j}
print(a) 
b = enumerate(a)
while   True:
	try:
		print(next(b))
		time . sleep(1)
	except  StopIteration:
		break


'''
{25 , 10.8 , 'Hyd' , True , 3+4j} in any odrer
(0,25) 
(1,10.8) 
(2,'Hyd') 
(3,True)  
(4,3+4j)

'''







# Can  dictionary  be  enumerated ?   (Home  work)
import   time
def  disp(e):
	while  True:
		try:
			print(next(e))
			time . sleep(1)
		except  StopIteration:
			break
	print()
dict = {'Empno'  :  25 , 'Emp Name'  :  'Rama Rao' , 'Sal' : 10000.0}
e1 = enumerate(dict . keys())
disp(e1)
e2 = enumerate(dict . values())
disp(e2)
e3 = enumerate(dict . items())
disp(e3)
e4 = enumerate(dict , start = 5)
disp(e4)


'''
(0,Empno)
(1,Emp Name)
(2,Sal)

(0,25)
(1,Rama Rao)
(2,10000.0)

(5,Empno)
(6,Emp Name)
(7,Sal)
'''





# Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
e = enumerate(a)
for   index ,  element  in  e:
	print(F'{element:20}  ...  {b[index]}')
	time . sleep(1)

'''
Telangana            ... Hyderabad
Andhra  Pradesh      ... Amaravathi
Karnataka            ... Bangalore
TamilNadu            ... Chennai
Maharastra           ... Mumbai
'''# Find  outputs (Home  work)
import  time
list = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   list)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
'''
25 
10.8
3 + 4j
'Hyd'
False
'''

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

# no output
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
'''
25
10.8
False
3 + 4j
'Hyd'
(25,)
 '''
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
disp(f1) # nothing
f2 = filter(None  , list)
print('Filter  f2')
disp(f2) # nothing

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
'''
'Rama Rao'
'Rajesh'
'Kiran'
'Manohar'
'Vamsi'
'''
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
'''
('B' , 20)
('C' , 15)
('E' , 18)'''

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
'''
{'Roll Num' :  10 , 'Stud Name' : 'Rama Rao' , 'Marks' : 75} 
{'Roll Num'  :  15 , 'Stud Name' : 'Kiran' , 'Marks' : 65}
{'Roll Num' :  5 , 'Stud Name' : 'Rajesh' , 'Marks' : 82}'''

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
'''
Filter  f1
{'country' : 'USA' , 'sale' : 300.3}
{'country' : 'UK' , 'sale' : 210.4}
Filter  f2
{'country' : 'china' , 'sale' : 200.2} ,
{'country' : 'USA' , 'sale' : 300.3} ,
{'country' : 'UK' , 'sale' : 210.4}
'''

# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f1 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  thru  filter  object  with   next   function')
while  True:
	try:
		print(next(f1))
		time . sleep(1)
	except:
		break
f2 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  thru  filter  object  with   for  loop')
for i in f2:
	print(i)
f3 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Unpack  filter  object :  ' , *f3 )
f4 = filter(lambda  x  :  x  %  2  ==  0 , a)
print('filter  object  converted  to   list  :  ' ,  list(f4))
'''
Iterate  thru  filter  object  with   next   function
10
20
18
26
Iterate  thru  filter  object  with   for loop
10
20
18
26
Unpack  filter  object
10 20 18 26 
filter  object  converted  to   list
[10,20,18,26]
'''
#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
import   time
a = list(range(1,11))
f1 = filter(lambda  x  :  x  %  2  ==  1 , a)
while  True:
	try:
		print(next(f1))
		time.sleep(1)
	except:
		break
'''
Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set
'''

a = input('Enter string : ').upper()
s=set()
f1 = filter(lambda  x  : True if x in 'AEIOU' else  False, a )
print(set(f1))


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
(10 , 'Rama' , 10000.0) 
(15 , 'Rajesh' , 15000.0)
'''