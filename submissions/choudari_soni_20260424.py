# Identify  Error  (Home  work)
class   c4:
	def  __iter__(self):
		print('__iter__  method ')
		return   self
# End  of  the  class
itr = c4()
for  x  in   itr:
	print(x)
#error because __next__ is missing

# Identify  Error
class   c5:
	def  __iter__(self):
		print('__iter__  method ')
# End  of  the  class
itr = c5()
for  x  in   itr:
	print(x)
#error because __iter__ method returns none

 # Identify  Error
class   c6:
        def   iter(self):
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):
                print('next  method')
# End  of  the  class
a  =  c6()
print(dir(c6))
for  x  in  a:   
        print(x)
while  True:
	print(next(a))  
a . next()
#error because c6 is not iterable 

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
# Zee Tv
# ETV
# Find  outputs (Home  work)
import  re
itr  =  re . finditer('[IEY]' , 'Hyd Is greEn citY', re . IGNORECASE)
while  True:
	try:
		m = next(itr)
		print(m . group() , 'is  at index : ' , m . start())
	except  StopIteration:
		break

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
# m  is  at  index :   0
# 9  is  at  index :   2
# K  is  at  index :   4
# d  is  at  index :   6
# 5  is  at  index :   8
# E  is  at  index :   10

'''
Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20
Hint: Use  for  loop
'''
class Numbers:
    def __iter__(self):
        for i in range(10, 21):   # 21 because end is exclusive
            yield i
n = Numbers()
for x in n:
    print(x)

'''
Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Hint :  Use  for  loop
'''
class PowerOfTwo:
    def __iter__(self):
        for i in range(8):   # 0 to 7
            yield 2 ** i
p = PowerOfTwo()
for x in p:
    print(x)

