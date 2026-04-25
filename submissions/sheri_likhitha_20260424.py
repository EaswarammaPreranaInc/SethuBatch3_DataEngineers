# Identify  Error  (Home  work)
class   c4:
	def  __iter__(self):
		print('__iter__  method ')	#__iter__ method
		return   self
# End  of  the  class
itr = c4()		#error c4 object is not an iterator
for  x  in   itr:
	print(x)



# Identify  Error
class   c5:
	def  __iter__(self):
		print('__iter__  method ')  #__iter method__
# End  of  the  class
itr = c5()
for  x  in   itr:
	print(x)	#error returned non-iterator of type 'nonetype'



# Identify  Error
class   c6:
        def   iter(self):	#error python expects __iter__ method
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):	#error python expects __next__ method
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
print('Elements  of  iterator  with  for  loop')  #Elements  of  iterator  with  for  loop	
for   element   in   a:
	print(element)	#__iter__method
	if  element  ==  5:    #1 <next> 2 <next> 3 <next> 4 <next> 5
               break
print('Elements  of  iterator  with  next()  function')		#Elements  of  iterator  with  next()  function
while    True:
	element = next(a)
	print(element)		#6 <next> 7 <next> 8 <next> 9 <next>10 
	if  element  ==  10:
		break
#end  of  while  loop
print('Elements  of  iterator  with  for  loop')	#Elements  of  iterator  with  for  loop
for   element   in    a:
	print(element)		#__iter__method
	if  element  ==  15:	#11 <next> 12 <next> 13 <next> 14 <next> 15
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


#outputs:
Tv 9
Espn
Zee Tv
ETV





class Numbers:
    def __iter__(self):
        for i in range(10, 21):
            yield i

# usage
n = Numbers()
for x in n:
    print(x)






class PowersOfTwo:
    def __iter__(self):
        for i in range(8):   # 0 to 7
            yield 2 ** i

# usage
p = PowersOfTwo()
for x in p:
    print(x)










