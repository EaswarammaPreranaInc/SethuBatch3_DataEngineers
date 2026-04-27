# Identify  Error  (Home  work)
class c4:
    def __iter__(self):
        print('__iter__  method ')   # prints when loop starts
        return self                 # returns object

itr = c4()
for x in itr:  #  ERROR 
    print(x)

# ERROR:
# __iter__ exists but __next__ is missing
#'c4' object is not an iterator





#Identify  Error
class c5:
    def __iter__(self):
        print('__iter__  method ')   
        #no return - returns None

itr = c5()
for x in itr:   # ERROR
    print(x)

# ERROR:
# __iter__ must return iterator object but returns None
#iter() returned non-iterator of type 'NoneType'








 # Identify  Error
class c6:
    def iter(self):                      #  wrong name (should be __iter__)
        return reversed([10 , 20 , 15 , 18])
    def next(self):                      #  wrong name (should be __next__)
        print('next  method')            # prints but no return

a = c6()
print(dir(c6))                          # prints class attributes

for x in a:                             #  ERROR
    print(x)

# ERROR:
# 'c6' object is not iterable

while True:
    print(next(a))   # ERROR

# ERROR:
#'c6' object is not an iterator

a.next()    # prints: next  method









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
#Elements  of  iterator  with  for  loop
#__iter__    method
#1 2 3 4 5             
            
print('Elements  of  iterator  with  next()  function')
while    True:
	element = next(a)
	print(element)
	if  element  ==  10:
		break
#Elements  of  iterator  with  next()  function	    
#6 7 8 9 10	    
	    
#end  of  while  loop
print('Elements  of  iterator  with  for  loop')
for   element   in    a:
	print(element)
	if  element  ==  15:
		break
#Elements  of  iterator  with  for  loop
#__iter__    method	    
#11 12 13 14 15	    
	    

	    


# Object   'a'  --->c1()






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

#  object  'r'  --->remote()


#output
# Tv 9
# Espn
# Zee Tv
# ETV


 '''
Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20

Hint: Use  for  loop
'''
class numbers:
    def __iter__(self):
        for i in range(10, 21):
            yield i

for x in numbers():
    print(x)



 '''
Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Hint :  Use  for  loop
'''
class Powers:
    def __iter__(self):
        for i in range(8):
            yield 2 ** i

for x in Powers():
    print(x)

    


 '''   (Home  work)
1) 1st  input  ---> 'Hyd is green city'
    2nd  input  --->  'Green'
	What  are  the  outputs  --->Green is found between indexes 7 and 11

2) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'red'
    What  are  the  outputs  --->red is not found
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
	What  are  the  outputs  ---> does not start with city
                                      ends with city

2) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'Hyd'
    What  are  the  outputs  --->starts with Hyd
                                 does not end with Hyd

3) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'is'
    What  are  the  outputs  --->does not start with is
                                 does not end with is
	
4) 1st  input  --->  'One  for  all  and  all  for  one'
    2nd  input ---> 'one'
    What  are  the  outputs  --->starts with One
                                 ends with one
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
What  are  the  outputs  ---> is -index 4 to 5
                              IS - index 24 to 25
                              Is - index 41 to 42
                              iS - index 46 to 47
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
#output
y is  at index :  1
I is  at index :  4
e is  at index :  9
E is  at index :  10
i is  at index :  14
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

# OUTPUT:
# m index 0
# 9 index 2
# K index 4
# d index 6
# 5 index 8
# E index 10
