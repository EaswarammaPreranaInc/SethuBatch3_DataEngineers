# Identify  Error  (Home  work)
class   c4:
	def  __iter__(self):
		print('__iter__  method ') # __iter__  method
		return   self
# End  of  the  class
itr = c4()
for  x  in   itr:
	print(x) # error: 'c4' object is not an iterator
	
# Identify  Error
class   c5:
	def  __iter__(self):
		print('__iter__  method ') # __iter__  method
# End  of  the  class
itr = c5()
for  x  in   itr:  # error: iter() returned non-iterator of type 'NoneType'
	print(x)    

# Identify  Error
class   c6:
        def   iter(self):
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):
                print('next  method')
# End  of  the  class
a  =  c6()
print(dir(c6)) # ['iter', 'next' and enviroment variables]   
for  x  in  a:   
        print(x) # TypeError: 'c6' object is not iterable
while  True:
	print(next(a))  # TypeError: 'c6' object is not an iterator
a . next() # next  method

# Find  outputs(Home  work)
class   c1:
	def   __init__(self):
		self . x =  1
	def   __iter__(self):
		print('__iter__    method') # __iter__    method
		return  self
	def   __next__(self):
		value =  self . x
		self . x  +=  1
		return  value
# End  of  the  class
a = c1()
print('Elements  of  iterator  with  for  loop')
for   element   in   a:
	print(element) # 1<next line> 2 <next line>3  <next line>4 <next line>5
	if  element  ==  5:
               break
print('Elements  of  iterator  with  next()  function')
while    True:
	element = next(a)
	print(element) # 6 <next line> 7 <next line> 8  <next line> 9  <next line> 10
	if  element  ==  10:
		break
#end  of  while  loop
print('Elements  of  iterator  with  for  loop')
for   element   in    a:
	print(element) # __iter__    method then 11 <next line> 12 <next line> 13 <next line> 14 <next line> 15
	if  element  ==  15:
		break


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
# Tv 9
# Espn
# Zee Tv
 # ETV
	
'''
Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20

Hint: Use  for  loop
'''
class c1:
    def __iter__(self):
        for i in range(10, 21):
            yield i

# usage
a = c1()
for x in a:
    print(x) 

'''
Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Hint :  Use  for  loop
'''

class c1:
    def __iter__(self):
        for i in range(0, 8):
            yield 2 ** i

# usage
a = c1()
for x in a:
    print(x) 

'''   (Home  work)
1) 1st  input  ---> 'Hyd is green city'
    2nd  input  --->  'Green'
	What  are  the  outputs  ---> <class 're.Match'>
                                  green  is found  between  indexes  7   and   11

2) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'red'
    What  are  the  outputs  --->   <class 'NoneType'>
                                    red  is  not  found
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
	
# (Home  work)
'''
1) 1st  input  ---> 'Hyd is green city'
    2nd  input  --->  'city'
	What  are  the  outputs  ---> Hyd is green city  does  not  start  with  city
Hyd is green city  ends  with  city

2) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'Hyd'
    What  are  the  outputs  ---> Hyd is green city  starts  with   Hyd
Hyd is green city  does  not  end  with  Hyd

3) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'is'
    What  are  the  outputs  ---> Hyd is green city  does  not  start  with  is
Hyd is green city  does  not  end  with  is
	
4) 1st  input  --->  'One  for  all  and  all  for  one'
    2nd  input ---> 'one'
    What  are  the  outputs  ---> One  for  all  and  all  for  one  starts  with   One
One  for  all  and  all  for  one  ends  with  one
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

'''  (Home  work)
What  are  the  outputs
1st  input  --->  Hyd is green city. Hyd IS hitec city. Hyd Is hiS city
2nd  input  --->  is
What  are  the  outputs  ---> is  is  between  indexes  4  and  5
is  is  between  indexes  38  and  39
IS  is  between  indexes  24  and  25
Is  is  between  indexes  48  and  49
is  is  between  indexes  53  and  54
Found  5  times
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


# Find  outputs (Home  work)
import  re
itr  =  re . finditer('[IEY]' , 'Hyd Is greEn citY', re . IGNORECASE)
while  True:
	try:
		m = next(itr)
		print(m . group() , 'is  at index : ' , m . start())
	except  StopIteration:
		break
# output:	
# I is  at index :  4
# e is  at index :  7
# E is  at index :  9
# Si is  at index :  13
# Y is  at index :  15    
# Find  outputs (Home  work)
import   re
itr  =  re . finditer('[A-Za-z0-9]' , 'm$9 K,d%5@E&')
while  True:
	try:
		m = next(itr)
		print(m . group() , ' is  at  index :  ' , m . start())
	except:
		break    
# Output
# m  is  at  index :   0
# 9  is  at  index :   2
# K  is  at  index :   4
# d  is  at  index :   6
# 5  is  at  index :   9
# E  is  at  index :   11	