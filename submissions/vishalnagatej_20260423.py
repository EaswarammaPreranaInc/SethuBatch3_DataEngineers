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
# Elements  of  iterator  with  for  loop
# __iter__    method
# 1
# 2
# 3
# 4
# 5
# Elements  of  iterator  with  next()  function
# 6
# 7
# 8
# 9
# 10
# Elements  of  iterator  with  for  loop
# __iter__    method
# 11
# 12
# 13
# 14
# 15

#=======================================================================================================================================

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

# Tv 9 
# Espn
# Zee tv
# ETv

#=======================================================================================================================================

'''
Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20

Hint: Use  for  loop
'''

class c1:
    def __init__(self):
        self.x = 10
    def __iter__(self):
        print('__iter__ method')
        return self
    def __next__(self):
        value = self.x
        self.x += 1
        return value
    
a = c1()
for i in a:
    print(i)
    if i == 20:
        break

# __iter__ method
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20

#=======================================================================================================================================

'''
Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Hint :  Use  for  loop
'''

class c2:
    def __init__(self):
        self.x = 0
    def __iter__(self):
        print('__iter__ method')
        return self
    def __next__(self):
        if self.x > 7:
            raise StopIteration
        value = 2 ** self.x
        self.x += 1
        return value

a = c2()
for i in a:
    print(i)

# __iter__ method
# 1
# 2
# 4
# 8
# 16
# 32
# 64
# 128

#=======================================================================================================================================

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

# <class 're.match'
# Green is found  between  indexes 7   and   11

# <class 'Nonetype'>
# red is not found

#=======================================================================================================================================

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
	
# Hyd is green city  does  not  start  with  city
# Hyd is green city ends  with city

#  Hyd is green city starts with Hyd
#  Hyd is green city does  not  end  with Hyd

# Hyd is green city  does  not  start  with  is
# Hyd is green city does  not  end  with  is

# One  for  all  and  all  for  one starts with One
# One  for  all  and  all  for  one ends  with one

#=======================================================================================================================================

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

# is  is  between  indexes  4  and  5
# is  is  between  indexes  23  and  24
# is  is  between  indexes  42  and  43
# is  is  between  indexes  46  and  47
# Found 4 times

#=======================================================================================================================================

# Find  outputs (Home  work)
import  re
itr  =  re . finditer('[IEY]' , 'Hyd Is greEn citY', re . IGNORECASE)
while  True:
	try:
		m = next(itr)
		print(m . group() , 'is  at index : ' , m . start())
	except  StopIteration:
		break

# y is  at index : 1
# I is  at index : 4
# e is  at index : 9
# E is  at index : 10
# i is  at index : 14
# Y is  at index : 16

#=======================================================================================================================================

# Find  outputs (Home  work)
import   re
itr  =  re . finditer('[A-Za-z0-9]' , 'm$9 K,d%5@E&')
while  True:
	try:
		m = next(itr)
		print(m . group() , ' is  at  index :  ' , m . start())
	except:
		break

# M is  at index : 0
# 9 is  at index : 2
# K is  at index : 4
# d is  at index : 6
# 5 is  at index : 8
# E is  at index : 10