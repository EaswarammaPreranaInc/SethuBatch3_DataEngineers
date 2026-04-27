# Identify  Error  (Home  work)
class   c4:
	def  __iter__(self):
		print('__iter__  method ')
		return   self  #error-iter method can only return iterator
# End  of  the  class
itr = c4()
for  x  in   itr:
	print(x)



# Identify  Error
class   c5:
	def  __iter__(self):
		print('__iter__  method ')  #__iter__ method is not returning anything.so None is returned by default(which is not an iterator)
# End  of  the  class
itr = c5()
for  x  in   itr:
	print(x)




# Identify  Error
class   c6:
        def   iter(self):  #it must be __iter__
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):  #it must be __next__
                print('next  method')
# End  of  the  class
a  =  c6()
print(dir(c6))  #all methods of c6 class-iter and next
for  x  in  a:  #error-since there is no __iter__
        print(x)
while  True:
	print(next(a))     #error-since there is no __next__
a . next()  #next method




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


# Object   'a'  --->x=1


'''
Elements  of  iterator  with  for  loop
__iter__    method
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
__iter__    method
11
12
13
14
15
'''



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

#  object  'r'  --->list = ['Tv 9' , 'Espn' , 'Zee Tv' , 'ETV'], index = -1

'''
Tv 9
Espn
Zee Tv
ETV
'''



'''
Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20

Hint: Use  for  loop
'''

class c1:
    def __init__(self):
        self.x=9
    def __iter__(self):
        return self
    def __next__(self):
         self.x+=1
         if self.x==21:
             raise StopIteration
         return self.x
a=c1()
for x in a:
    try:
        print(x)
    except StopIteration:
        break




'''
Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Hint :  Use  for  loop
'''

class c1:
    def __init__(self):
        self.x=-1
    def __iter__(self):
        return self
    def __next__(self):
         self.x+=1
         if self.x==8:
             raise StopIteration
         return pow(2,self.x)
a=c1()
for x in a:
    try:
        print(x)
    except StopIteration:
        break




'''   (Home  work)
1) 1st  input  ---> 'Hyd is green city'
    2nd  input  --->  'Green'
	What  are  the  outputs  ---><class 'Match'>
	green  is found  between  indexes  7   and   11

2) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'red'
    What  are  the  outputs  ---><class 'Match'>
	red is not found
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





'''   (Home  work)
1) 1st  input  ---> 'Hyd is green city'
    2nd  input  --->  'city'
	What  are  the  outputs  --->Hyd is green city does not start with city
	                             Hyd is green city ends with city

2) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'Hyd'
    What  are  the  outputs  --->Hyd is green citystarts with Hyd
	                             Hyd is green citydoes not end with Hyd

3) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'is'
    What  are  the  outputs  --->Hyd is green city does not start with is
	                             Hyd is green city does not end with is
	
4) 1st  input  --->  'One  for  all  and  all  for  one'
    2nd  input ---> 'one'
    What  are  the  outputs  --->One  for  all  and  all  for  one starts with one
	                             One  for  all  and  all  for  one does not end with one

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
What  are  the  outputs  --->is is between indexes 4 and 5
                             is is between indexes 23 and 24
                             is is between indexes 42 and 43
                             is is between indexes 46 and 47
							 Found 4 times							 
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
'''
y is at index: 1
I is at index: 4
e is at index: 9
E is at index: 10
i is at index: 14
Y is at index: 6
'''



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
m is at index : 0
9 is at index : 2
K is at index : 4
d is at index : 6
5 is at index : 8
E is at index : 10
'''