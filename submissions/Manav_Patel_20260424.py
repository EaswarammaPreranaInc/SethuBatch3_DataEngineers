# Identify  Error  (Home  work)
class   c4:
	def  __iter__(self):
		print('__iter__  method ')  #__iter__ method
		return   self
# End  of  the  class
itr = c4()
for  x  in   itr:
	print(x)    #Error due to iter() returned non-iterator



# Identify  Error
class   c5:
	def  __iter__(self):
		print('__iter__  method ')  #__iter__ method
# End  of  the  class
itr = c5()
for  x  in   itr:
	print(x)        #Error due to iter() returned non-iterator None type



# Identify  Error
class   c6:
        def   iter(self):
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):
                print('next  method')
# End  of  the  class
a  =  c6()
print(dir(c6))      #['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'iter', 'next']
for  x  in  a:   
        print(x)        #'c6 is not iterable
while  True:
	print(next(a))  #'c6' is not iterable
a . next()



# Find  outputs(Home  work)
class   c1:
	def   __init__(self):
		self . x =  1
	def   __iter__(self):
		print('__iter__    method')     # __iter__ method
		return  self
	def   __next__(self):
		value =  self . x
		self . x  +=  1
		return  value
# End  of  the  class
a = c1()
print('Elements  of  iterator  with  for  loop')    #Elements of iterator with for loop
for   element   in   a:
	print(element)      #1  2   3   4   5
	if  element  ==  5:
               break
print('Elements  of  iterator  with  next()  function') # Elements  of  iterator  with  next()  function
while    True:
	element = next(a)
	print(element)  #6  7   8   9   10
	if  element  ==  10:
		break
#end  of  while  loop
print('Elements  of  iterator  with  for  loop')    #Elements  of  iterator  with  for loop
for   element   in    a:
	print(element)  #11 12  13  14  15
	if  element  ==  15:
		break
# Object   'a'  ---> c1 class object



# Find  outputs (Home  work)
import   time
class  Remote:
	def    __init__(self):
		self . list = ['Tv 9' , 'Espn' , 'Zee Tv' , 'ETV']
		self . index = -1
	def   __iter__(self):
		return  self
	def   __next__(self):
		self . index += 1
		if   self . index  ==  len(self . list):
			raise  StopIteration
		return    self . list[self . index]
# End  of  the  class
r = Remote()
for  x   in    r:
	print(x)        #Tv 9   Espn    Zee Tv  ETV
	time . sleep(1)

#  object  'r'  ---> Remote class object




'''
Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20

Hint: Use  for  loop
'''
def number_iterator():
    for i in range(10, 21):  # 21 is excluded, so it goes up to 20
        yield i
# Using the iterator
for num in number_iterator():
    print(num)





'''
Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Hint :  Use  for  loop
'''
def powers_of_two():
    for i in range(8):  # from 0 to 7
        yield 2 ** i
# Using the iterator
for value in powers_of_two():
    print(value)





'''   (Home  work)
1) 1st  input  ---> 'Hyd is green city'
    2nd  input  --->  'Green'
	What  are  the  outputs  --->

2) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'red'
    What  are  the  outputs  --->
'''
import   re
string = input('Enter  any  string  :  ')   #niv
pattern = input('Enter  pattern  :   ')     #srinivas
m  =  re . search(pattern , string , re . IGNORECASE)
print(type(m))  #class 're.match'
if  m:
	print(F'{m . group()}  is found  between  indexes  {m . start()}   and   {m . end() - 1}') #niv found between indexes 3 and 5
else:
	print(pattern , ' is  not  found ')
	



'''   (Home  work)
1) 1st  input  ---> 'Hyd is green city'
    2nd  input  --->  'city'
	What  are  the  outputs  --->

2) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'Hyd'
    What  are  the  outputs  --->

3) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'is'
    What  are  the  outputs  --->
	
4) 1st  input  --->  'One  for  all  and  all  for  one'
    2nd  input ---> 'one'
    What  are  the  outputs  --->
'''
import  re
str = input('Enter  any  string  :  ')  #niv
pattern = input('Enter  pattern  :   ')     #srinivas
m = re . search('^' + pattern ,  str , re . IGNORECASE)
if  m:
	print(F'{str}  starts  with   {m . group()}')
else:
	print(F'{str}  does  not  start  with  {pattern}')  #niv does not starts with srinivas
m = re . search(pattern + '$' , str  , re . IGNORECASE)
if   m:
	print(F'{str}  ends  with ' , m . group())
else:
	print(F'{str}  does  not  end  with  {pattern}')    #niv does not starts with srinivas
	




'''  (Home  work)
What  are  the  outputs
1st  input  --->  Hyd is green city. Hyd IS hitec city. Hyd Is hiS city
2nd  input  --->  is
What  are  the  outputs  --->
'''
import re
string  =  input('Enter  any  string  :  ')     #Hyd is green city. Hyd IS hitec city. Hyd Is hiS city
pattern = input('Enter  pattern  to  be  searched : ')  #is
itr = re . finditer(pattern , string , re . IGNORECASE)
ctr = 0
while  True:
	try:
		m = next(itr)
		print(F'{m . group()}  is  between  indexes  {m . start()}  and  {m . end() - 1}')  #is found between indexes 4 and 5, 23 and 24, 42 and 43, 46 and 47
		ctr += 1   
	except  StopIteration:
		break
print('Found ' , ctr ,' times')   #Found 4 times




# Find  outputs (Home  work)
import  re
itr  =  re . finditer('[IEY]' , 'Hyd Is greEn citY', re . IGNORECASE)
while  True:
	try:
		m = next(itr)
		print(m . group() , 'is  at index : ' , m . start())    
	except  StopIteration:
		break
# outputs:
# y is at index : 1
# I is at index : 4
# e is at index : 9
# E is at index : 10
# i is at index : 14
# Y is at index : 16
	



# Find  outputs (Home  work)
import   re
itr  =  re . finditer('[A-Za-z0-9]' , 'm$9 K,d%5@E&')
while  True:
	try:
		m = next(itr)
		print(m . group() , ' is  at  index :  ' , m . start()) 
	except:
		break
#output:-
#m is at index: 0
#9 is at index: 2
#K is at index: 4
#d is at index: 6
#5 is at index: 8
#E is at index: 10