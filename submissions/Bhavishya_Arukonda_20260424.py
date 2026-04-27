# Identify  Error  (Home  work)
class   c4:
	def  __iter__(self):
		print('__iter__  method ')
		return   self
# End  of  the  class
itr = c4()
for  x  in   itr:
	print(x)




# Identify  Error
class   c5:
	def  __iter__(self):
		print('__iter__  method ')
# End  of  the  class
itr = c5()
for  x  in   itr:
	print(x)



# Identify  Error
class   c6:
        def   iter(self): # error __iter__
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):  # error __next__
                print('next  method')
# End  of  the  class
a  =  c6()
print(dir(c6))
for  x  in  a:   
        print(x)
while  True:
	print(next(a))  
a . next()



# Find  outputs(Home  work)
class   c1:
	def   __init__(self):
		self . x =  1
	def   __iter__(self):
		print('__iter__    method')
		return  self
	def   __next__(self):
		value =  self . x
		self . x  +=  1
		return  value
# End  of  the  class
a = c1()
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

__iter__    method
Elements  of  iterator  with  for  loop
1
2
3
4
5
Elements  of  iterator  with  next()  function
6
7
8
9
10
Elements  of  iterator  with  for  loop
11
12
13
14
15




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
	print(x)
	time . sleep(1)

#  object  'r'  --->

Tv 9
Espn
Zee Tv
ETV



'''
Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20

Hint: Use  for  loop
'''
def ten_to_twenty():
        for n in range(10, 21):  
        yield n

for value in ten_to_twenty():
    print(value)



'''
Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Hint :  Use  for  loop
'''
def powers_of_two():
    for exp in range(8):           
        yield 2 ** exp

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
string = input('Enter  any  string  :  ') 
pattern = input('Enter  pattern  :   ')  
m  =  re . search(pattern , string , re . IGNORECASE)
print(type(m))
if  m:
	print(F'{m . group()}  is found  between  indexes  {m . start()}   and   {m . end() - 1}')
else:
	print(pattern , ' is  not  found ')

<class 're.Match'>
green  is found  between  indexes  7   and   11


<class 'NoneType'>
red  is  not  found 



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


Hyd is green city does not start with city
Hyd is green city ends with  city


Hyd is green city starts with   Hyd
Hyd is green city does not end  with  Hyd


Hyd is green city does not start with is
Hyd is green city does not end  with  is


One for all and all for one starts with   One
One for all and all for one ends with  one




'''  (Home  work)
What  are  the  outputs
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

is  is  between  indexes  4  and  5
IS  is  between  indexes  20  and  21
is  is  between  indexes  36  and  37
Found  3  times




# Find  outputs (Home  work)
import  re
itr  =  re . finditer('[IEY]' , 'Hyd Is greEn citY', re . IGNORECASE)
while  True:
	try:
		m = next(itr)
		print(m . group() , 'is  at index : ' , m . start())
	except  StopIteration:
		break

I is  at index :  4
e is  at index :  9
E is  at index :  10
Y is  at index :  16



# Find  outputs (Home  work)
import   re
itr  =  re . finditer('[A-Za-z0-9]' , 'm$9 K,d%5@E&')
while  True:
	try:
		m = next(itr)
		print(m . group() , ' is  at  index :  ' , m . start())
	except:
		break


m  is  at  index :   0
9  is  at  index :   2
K  is  at  index :   4
d  is  at  index :   6
5  is  at  index :   8
E  is  at  index :   10