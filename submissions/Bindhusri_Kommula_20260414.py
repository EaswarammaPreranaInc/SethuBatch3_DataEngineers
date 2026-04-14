'''
Repeat  prog10a  with  3  objects

Eg:  c = a + b
	 print  c
	 c = a - b
	 print  c
	 c = a * b
	 print  c
	 c = a / b
	 print  c

Hint:  Import   Rat  class  defined  in  prog10a  but  do  not  define  Rat  class   again
'''



'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''



# mod1.py  (Home  work)
print('Hyd') # Hyd
print('Sec') #  Sec
print('Cyb') # Cyb
#print('India')
#print('USA')



# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1

output:
Hyd
Sec
Cyb




# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()
importlib . reload(mod1)
print()
importlib . reload(mod1)
importlib . reload('mod1')
reload(mod1)

output:
Hyd
Sec
Cyb

Hyd
Sec
Cyb

Hyd
Sec
Cyb



#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))
print()
print()
print(dir(time))
print()
print(dir(math))


#  Find  outputs  (Home  work)
import  cal
print(dir(cal))



#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())
print(type(dir())) # <class 'list'>
print(type(dir)) # <class 'builtin_function_or_method'>




'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '__name__' . startswith('__')  ?  --->  True

2) What  is  the  result  of  '__spec__' . endswith('__')  ?  --->  True

3) What  is  the  result  of  'spec__' . startswith('__')  ?  --->  False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''



# cal.py
def  add(a , b):
	return  a + b
def  sub(a , b):
	return  a - b
def  mul(a , b):
	return  a * b
def  div(a , b):
	return  a / b
class    c1:
	def    m1(self):
		pass
#End  of  the  class
x = 100
y = 200
if  __name__   ==  '__main__':
	print('Hyd')
	print('Sec')
	print('Cyb')

output:
Hyd
Sec
Cyb

['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#  Find  outputs
print(dir())
print()
import  cal
print()
print(dir())



#  Find  outputs
print(dir())
print()
from  cal  import  *
print()
print(dir())


#  Find  outputs
print(dir())
print()
from  cal  import  add , mul , x
print()
print(dir())


# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path)) # 6
import  cal



# Save  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
How  to  print  number  of  directories  (or)  folders  in  sys.path
How  to  append  c:\sairam  folder  to  sys.path
How  to  print  number  of  directories  (or)  folders  in  sys.path
How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder