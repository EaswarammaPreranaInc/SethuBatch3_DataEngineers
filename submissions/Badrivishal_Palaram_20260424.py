1) Identify  Error 
class   c4:
	def  _iter_(self):
		print('_iter_  method ')
		return   self
# End  of  the  class
itr = c4()#Not iterable so error
for  x  in   itr:
	print(x)

2) Identify  Error
class   c5:
	def  _iter_(self):
		print('_iter_  method ')
# End  of  the  class
itr = c5()#Not iterable so error
for  x  in   itr:
	print(x)

3) Identify  Error
class   c6:
        def   iter(self):
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):
                print('next  method')
# End  of  the  class
a  =  c6()#Not iterable so error
print(dir(c6))
for  x  in  a:   
        print(x)
while  True:
	print(next(a))  
a . next()

4) outputs
class   c1:
	def   _init_(self):
		self . x =  1
	def   _iter_(self):
		print('_iter_    method')
		return  self
	def   _next_(self):
		value =  self . x
		self . x  +=  1
		return  value
# End  of  the  class
a = c1()#Error because it is not iterable
print('Elements  of  iterator  with  for  loop')
for   element   in   a:
	print(element)
	if  element  ==  5:
               break
print('Elements  of  iterator  with  next()  function')
while    True:
	element = next(a)
	print(element)
	if  element  ==  10:
		break
#end  of  while  loop
print('Elements  of  iterator  with  for  loop')
for   element   in    a:
	print(element)
	if  element  ==  15:
		break


# Object   'a'  --->

5) outputs 
import   time
class  Remote:
	def    _init_(self):
		self . list = ['Tv 9' , 'Espn' , 'Zee Tv' , 'ETV']
		self . index = -1
	def   _iter_(self):
		return  self
	def   _next_(self):
		self . index += 1
		if   self . index  ==  len(self . list):
			raise  StopIteration
		return    self . list[self . index]
# End  of  the  class
r = Remote()#Error because it is not valid
for  x   in    r:
	print(x)
	time . sleep(1)

#  object  'r'  --->

6) Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20

Hint: Use  for  loop
'''
#class Num:
    def __iter__(self):
        for i in range(10, 21):
            yield i

a = Num()

for x in a:
    print(x)

7) Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Hint :  Use  for  loop
'''
#class Pow2:
    def __iter__(self):
        for i in range(8):
            yield 2 ** i

a = Pow2()

for x in a:
    print(x)

8) HW
1) 1st  input  ---> 'Hyd is green city'
    2nd  input  --->  'Green'
	What  are  the  outputs  ---><class 're.Match'>
green is found between indexes 7 and 11

2) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'red'
    What  are  the  outputs  ---><class 'NoneType'>
'red'  is  not  found 
'''
import   re
string = input('Enter  any  string  :  ') 
pattern = input('Enter  pattern  :   ')  
m  =  re . search(pattern , string , re . IGNORECASE)
print(type(m))
if  m:
	print(F'{m . group()}  is found  between  indexes  {m . start()}   and   {m . end() - 1}')
else:
	print(pattern , ' is  not  found ')

9) HW
1) 1st  input  ---> 'Hyd is green city'
    2nd  input  --->  'city'
	What  are  the  outputs  --->Hyd is green city does not start with city
Hyd is green city ends with city

2) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'Hyd'
    What  are  the  outputs  --->Hyd is green city starts with Hyd
Hyd is green city does not end with Hyd

3) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'is'
    What  are  the  outputs  --->Hyd is green city does not start with is
Hyd is green city does not end with is
	
4) 1st  input  --->  'One  for  all  and  all  for  one'
    2nd  input ---> 'one'
    What  are  the  outputs  --->#'One  for  all  and  all  for  one'  does  not  start  with  'one'
'One  for  all  and  all  for  one'  does  not  end  with  'one'
'''
import  re
str = input('Enter  any  string  :  ') 
pattern = input('Enter  pattern  :   ')  
m = re . search('^' + pattern ,  str , re . IGNORECASE)
if  m:
	print(F'{str}  starts  with   {m . group()}')
else:
	print(F'{str}  does  not  start  with  {pattern}')
m = re . search(pattern + '$' , str  , re . IGNORECASE)
if   m:
	print(F'{str}  ends  with ' , m . group())
else:
	print(F'{str}  does  not  end  with  {pattern}')

10) What  are  the  outputs
1st  input  --->  Hyd is green city. Hyd IS hitec city. Hyd Is hiS city
2nd  input  --->  is
What  are  the  outputs  --->
'''
import re
string  =  input('Enter  any  string  :  ')
pattern = input('Enter  pattern  to  be  searched : ')
itr = re . finditer(pattern , string , re . IGNORECASE)
ctr = 0
while  True:
	try:
		m = next(itr)
		print(F'{m . group()}  is  between  indexes  {m . start()}  and  {m . end() - 1}')
		ctr += 1   
	except  StopIteration:
		break
print('Found ' , ctr ,' times')

11) Outputs
import  re
itr  =  re . finditer('[IEY]' , 'Hyd Is greEn citY', re . IGNORECASE)
while  True:
	try:
		m = next(itr)
		print(m . group() , 'is  at index : ' , m . start())
	except  StopIteration:
		break
#y is  at index :  1
I is  at index :  4
e is  at index :  9
E is  at index :  10
i is  at index :  14
Y is  at index :  16

12) Outputs
import   re
itr  =  re . finditer('[A-Za-z0-9]' , 'm$9 K,d%5@E&')
while  True:
	try:
		m = next(itr)
		print(m . group() , ' is  at  index :  ' , m . start())
	except:
		break
#m is at index : 0
9 is at index : 2
K is at index : 4
d is at index : 6
5 is at index : 8
E is at index : 10