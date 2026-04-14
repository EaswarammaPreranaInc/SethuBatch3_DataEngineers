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
from prog10 import rat
a=rat()
b=rat()
c=rat()
a.get()
b.get()
c . add(a , b)
print('Sum : ',c)
c . sub(a , b) 
print('Difference : ',c)
c . mul(a , b) 
print('Multiplication : ',c)
if b.nr!=0:
    c. div(a , b)
    print('Division : ',c)
else:
    print('Division is not permitted')



'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
from prog10a import rat
a=[rat(),rat(),rat(),rat(),rat(),rat()]
for i in range(2):
    a[i].get
a[2].add(a[0],a[1])
print("Sum : ",a[2])
a[3].sub(a[0],a[1])
print("Difference : ",a[3])
a[4].mul(a[0],a[1])
print("Multiplication : ",a[4])
if a[1].nr!=0:
    a[5].div(a[0],a[1])
    print("Division : ",a[5])
else:
    print("Division not permitted")








# mod1.py  (Home  work)
print('Hyd')  # Hyd
print('Sec')  # Sec
print('Cyb')  # Cyb
#print('India')
#print('USA')



# Find  outputs  (Home  work)
import  mod1
import  mod1
import  mod1  

# Hyd
# Sec
# Cyb

# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()
importlib . reload(mod1) # Hyd
# Sec
# Cyb

print()
importlib . reload(mod1)  # Hyd
# Sec
# Cyb

importlib . reload('mod1')  # error  argument should be mod1 but not string mod1
reload(mod1)  # error as there is no module name



#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))   # All the dir of sys 
print()
print()
print(dir(time))  # All the dir of time
print()
print(dir(math))  # All the dir of math


#  Find  outputs  (Home  work)
import  cal
print(dir(cal))  # All the members of cal and object of cal and environment variables



#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())  # returns all the members of current module , object and environment variables
print(type(dir()))   # <class 'list'>
print(type(dir))   # <class 'string'>







'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '__name__' . startswith('__')  ?  --->  True

2) What  is  the  result  of  '__spec__' . endswith('__')  ?  --->  True

3) What  is  the  result  of  'spec__' . startswith('__')  ?  --->  False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''



#  Find  outputs
print(dir())  
print()
import  cal
print()
print(dir())  # All the members of cal module , object and environment variables



#  Find  outputs
print(dir())   
print()
from  cal  import  *
print()
print(dir())  # All the members of cal module , object and environment variables





#  Find  outputs
print(dir())
print()
from  cal  import  add , mul , x
print()
print(dir())  # All the members of cal module , object and environment variables




# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path))
import  cal



# Save  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
How  to  print  number  of  directories  (or)  folders  in  sys.path
How  to  append  c:\sairam  folder  to  sys.path
How  to  print  number  of  directories  (or)  folders  in  sys.path
How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder



