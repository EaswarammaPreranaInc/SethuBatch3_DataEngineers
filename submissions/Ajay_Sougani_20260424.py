# Identify  Error  (Home  work)
class   c4:
	def  __iter__(self):
		print('__iter__  method ')
		return   self
# End  of  the  class
itr = c4()
for  x  in   itr:
	print(x) # itr is  not  iterable  because  it  does  not  have  __next__()  method

# Identify  Error
class   c5:
	def  __iter__(self):
		print('__iter__  method ')
# End  of  the  class
itr = c5()
for  x  in   itr:
	print(x) # iter() returns  None  and  for  loop  raises  TypeError: 'NoneType' object is not iterable

# Identify  Error
class   c6:
        def   iter(self):
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):
                print('next  method')
# End  of  the  class
a  =  c6()
print(dir(c6)) # iter(), next()
for  x  in  a:   
        print(x) # a is not  iterable becoz __iter__() method is not in c6 class
while  True:
	print(next(a)) #  c6 is not an iterator because it does not have __iter__() method, and __next__() method
a . next() # next method

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
print('Elements  of  iterator  with  for  loop') # Elements  of  iterator  with  for  loop
for   element   in   a:
	print(element) # 1 2 3 4 5
	if  element  ==  5:
               break
print('Elements  of  iterator  with  next()  function') # Elements  of  iterator  with  next()  function
while    True:
	element = next(a)
	print(element) # 6 7 8 9 10
	if  element  ==  10:
		break
#end  of  while  loop
print('Elements  of  iterator  with  for  loop') # Elements  of  iterator  with  for  loop
for   element   in    a:
	print(element) # 11 12 13 14 15
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
	print(x) # Tv 9'Tv 9' <1sec>\n 'Espn' <1sec>\n 'Zee Tv' <1sec>\n 'ETV' StopIteration
	time . sleep(1)


class c1:
    def __init__(self):
        self.start = 20
        self.stop = 9
        self.step=-1
    def __iter__(self):
        return reversed(range(self.start, self.stop, self.step))
    def __next__(self):
        return self.__iter__()
c = c1()
for x in c:
    print(x)


class c1:
    def __init__(self):
        self.x = 2
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <8:
            result = pow(self.x, self.current)
            self.current += 1
            return result
        else:
            raise StopIteration
c = c1()
while True:
    try:
        print(next(c))
    except StopIteration:
        break



1) 1st  input  ---> 'Hyd is green city'
    2nd  input  --->  'Green'
	What  are  the  outputs  --->

2) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'red'
    What  are  the  outputs  --->
'''
import   re
string = input('Enter  any  string  :  ') # Hyd is green city
pattern = input('Enter  pattern  :   ') # 'Green' or 'red'  
m  =  re . search(pattern , string , re . IGNORECASE)
print(type(m)) # <class 're.Match'>
if  m:
	print(F'{m . group()}  is found  between  indexes  {m . start()}   and   {m . end() - 1}') # for input Green : Green is found  between  indexes  7   and   11 
else:
	print(pattern , ' is  not  found ') # for input Red :'Red  is  not  found' 


'''
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
str = input('Enter  any  string  :  ') # 'Hyd is green city'
pattern = input('Enter  pattern  :   ') # 'city' , 'Hyd' , 'is' , 'one'
m = re . search('^' + pattern ,  str , re . IGNORECASE)
if  m:
	print(F'{str}  starts  with   {m . group()}') 
else:
	print(F'{str}  does  not  start  with  {pattern}') # 'Hyd is green city does not start with city'
m = re . search(pattern + '$' , str  , re . IGNORECASE)
if   m:
	print(F'{str}  ends  with ' , m . group()) # 'Hyd is green city ends with city'
else:
	print(F'{str}  does  not  end  with  {pattern}')
	
# outputs :
# str = 'Hyd is green city'
# pattern = 'city'
# Hyd is green city does not start with city
# Hyd is green city ends with city
# str = 'Hyd is green city'
# pattern = 'Hyd'
# Hyd is green city starts with Hyd
# Hyd is green city does not end with Hyd
# str = 'Hyd is green city'
# pattern = 'is'
# Hyd is green city does not start with is
# Hyd is green city does not end with is
# str = 'One  for  all  and  all  for  one'
# pattern = 'one'   
# One  for  all  and  all  for  one does not start with one
# One  for  all  and  all  for  one ends with one


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
# outputs:
# string  =  'Hyd is green city. Hyd IS hitec city. Hyd Is hiS city'
# pattern = 'is'
# 'is' is  between  indexes  4  and  5
# 'is' is  between  indexes  23  and  24
# 'is' is  between  indexes  42  and  43
# 'is' is  between  indexes  46  and  47
# Found 4 times

# Find  outputs (Home  work)
import  re
itr  =  re . finditer('[IEY]' , 'Hyd Is greEn citY', re . IGNORECASE)
while  True:
	try:
		m = next(itr)
		print(m . group() , 'is  at index : ' , m . start())
	except  StopIteration:
		break
# Output :
# y is  at index :  1
# I is  at index :  4
# e is  at index :  9
# E is  at index :  10
# i is  at index :  14
# Y is  at index :  16

# Find  outputs (Home  work)
import   re
itr  =  re . finditer('[A-Za-z0-9]' , 'm$9 K,d%5@E&')
while  True:
	try:
		m = next(itr)
		print(m . group() , ' is  at  index :  ' , m . start())
	except:
		break
# Output:
# m  is  at  index :   0
# 9  is  at  index :   2
# K  is  at  index :   4
# d  is  at  index :   6
# 5  is  at  index :   8
# E  is  at  index :  10

