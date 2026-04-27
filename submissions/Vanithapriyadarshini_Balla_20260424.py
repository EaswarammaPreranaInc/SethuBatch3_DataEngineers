# Identify  Error  (Home  work)
class   c4:
	def  __iter__(self):
		print('_iter_  method ')#_iter_  method
		return   self
# End  of  the  class
itr = c4()
for  x  in   itr: # __iter__() executed, itr is self and self is itr which is not a iterator
	print(x)

# Identify  Error
class   c5:
	def  _iter_(self):
		print('_iter_  method ')#_iter_  method
# End  of  the  class
itr = c5()
for  x  in   itr: # __iter__() executed , itr is None
	print(x)

# Identify  Error
class   c6:
        def   iter(self):
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):
                print('next  method')
# End  of  the  class
a  =  c6()
print(dir(c6))# list 
for  x  in  a:   # error
        print(x)
while  True:
	print(next(a))  # error
a . next()

# Find  outputs(Home  work)
class   c1:
	def   __init__(self):
		self . x =  1
	def   __iter__(self):
		print('_iter_    method')#_iter_    method
		return  self
	def   __next__(self):
		value =  self . x
		self . x  +=  1
		return  value # 1
# End  of  the  class
a = c1()
print('Elements  of  iterator  with  for  loop')#Elements  of  iterator  with  for  loop
for   element   in   a:# __iter__() and next() executed, a is self , self is a
	print(element)# 1 2 3 4 5 
	if  element  ==  5:
               break
print('Elements  of  iterator  with  next()  function')# Elements  of  iterator  with  next()  function
while    True:
	element = next(a) 
	print(element)# 6 7 8 9 10 
	if  element  ==  10:
		break
#end  of  while  loop
print('Elements  of  iterator  with  for  loop')#Elements  of  iterator  with  for  loop
for   element   in    a:
	print(element)# 11 12 13 14 15
	if  element  ==  15:
		break


# Object   'a'  ---> x=15

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
r = Remote()# 
for  x   in    r:# __iter__() and __next__() executed , r is self, self is r
	print(x)# Tv9 Espn 'Zee Tv' ETV
	time . sleep(1)

#  object  'r'  --->list = ['Tv 9' , 'Espn' , 'Zee Tv' , 'ETV'], index = 4


#Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20
import time
class c1:
    def __init__(self):
        self.x=9
    def __iter__(self):
        return self
    def __next__(self):
        self.x+=1
        if self.x <=20:
            return self.x
        raise StopIteration
itr=c1()
for y in itr:
    print(y)
    time.sleep(0.5)


#Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7
import time
class c2:
    def __init__(self):
        self.pow=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.pow+=1
        if self.pow<=7:
            return 2**self.pow
        raise StopIteration
p=c2()
for y in p:
    print(y)
    time.sleep(0.5)


#1) 1st  input  ---> 'Hyd is green city'
    #2nd  input  --->  'Green'
	#What  are  the  outputs  --->

# 2) 1st  input  --->  'Hyd is green city'
#     2nd  input ---> 'red'
#     What  are  the  outputs  --->

import   re
string = input('Enter  any  string  :  ') 
pattern = input('Enter  pattern  :   ')  
m  =  re . search(pattern , string , re . IGNORECASE)
print(type(m))# <class re>
if  m:
	print(F'{m . group()}  is found  between  indexes  {m . start()}   and   {m . end() - 1}')
	#Group is found btw indexes 7 and 11
else:
	print(pattern , ' is  not  found ')# red is not Found 


import  re
str = input('Enter  any  string  :  ') #'Hyd is green city'    'Hyd is green city'
pattern = input('Enter  pattern  :   ')  # 'city'      'Hyd'
m = re . search('^' + pattern ,  str , re . IGNORECASE)# None
if  m:
	print(F'{str}  starts  with   {m . group()}')
else:
	print(F'{str}  does  not  start  with  {pattern}')# 'Hyd is green city' does not start with city
m = re . search(pattern + '$' , str  , re . IGNORECASE)
if   m:
	print(F'{str}  ends  with ' , m . group())
else:
	print(F'{str}  does  not  end  with  {pattern}')# 'Hyd is green city'  ends with Hyd


import re
string  =  input('Enter  any  string  :  ')# Hyd is green city . Hyd is hitech city
pattern = input('Enter  pattern  to  be  searched : ') # is
itr = re . finditer(pattern , string , re . IGNORECASE)
ctr = 0
while  True:
	try:
		m = next(itr)
		print(F'{m . group()}  is  between  indexes  {m . start()}  and  {m . end() - 1}')
		ctr += 1 # 2 # is between indexes 4 and 5, # is between indexes 24 and 25
	except  StopIteration:
		break
print('Found ' , ctr ,' times') # Found 2 times

# Find  outputs (Home  work)
import  re
itr  =  re . finditer('[IEY]' , 'Hyd Is greEn citY', re . IGNORECASE)
while  True:
	try:
		m = next(itr)
		print(m . group() , 'is  at index : ' , m . start())
	except  StopIteration:
		break
	
'''y is  at index :  1
I is  at index :  4
e is  at index :  9
E is  at index :  10
i is  at index :  14
Y is  at index :  16'''

# Find  outputs (Home  work)
import   re
itr  =  re . finditer('[A-Za-z0-9]' , 'm$9 K,d%5@E&')
while  True:
	try:
		m = next(itr)
		print(m . group() , ' is  at  index :  ' , m . start())
	except:
		break
'''
m  is  at  index :   0   
9  is  at  index :   2
K  is  at  index :   4
d  is  at  index :   6
5  is  at  index :   8
E  is  at  index :   10'''