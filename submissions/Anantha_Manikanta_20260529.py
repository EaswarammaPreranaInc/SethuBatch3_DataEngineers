'''
1) Producer-Consumer  problem  with  synchronization

1) Add  two  more  variables  to  buffer  object 
    i.e.  write  variable  and  cond  object

2) What  does  buf . write = True  indicate ?  --->  Thread  'p'  can  write  a  value  to  the  buffer  object
     What  does  buf . write = False  indicate ?  ---> Thread  'p'  can  not  write  a  value  to  the  buffer  object

3) Initialize  write  variable  and  cond  object  in  the  constructor  of  buffer  class

4) What  does  thread  'p'  do  (4  events) ?  ---> 
	 a) Stores  a  value  in  buf . x  when  buf . write = True	 
	 b) Modifies  buf . write = False  becoz  thread  'p'  can  not  write  another  value  to  object  buf   immediately	 
	 c) notifies  the  waiting  thread (i.e. Thread  'c')  that  a  new  value  is  available  in  buffer	 
	 d) Thread  'p'  waits  becoz  buf . write = False

5) What  does  thread  'c'  do  (4  events) ?  --->		 
	 a) Prints  buf . x  when  buf . write = False	
	 b) Modifies  buf . write = True  becoz  thread  'c'  can  not  print  same  value  again	 
	 c) Notifies  thread  'p'  that  value  is  retrieved  from  object   buf	 
	 d) Thread  'c'  waits  becoz  buf . write = True

6) Modify  store()  and  ret()  methods  as  indicated  above
    and  also  add  constructor  to  buffer  class

7) Functions  f1() , f2()  and  the  code  outside  remains  same
'''
from threading import *
import time
from random import randint
class buffer:
	def __init__(self):
		self.write = True
		self.cond = Condition()
	def store(self , y):
		self.cond.acquire()
		while self.write == False:
			self.cond.wait()
		s = current_thread().name
		self.x = y
		print(s , 'stores' , self.x)
		self.write = False
		self.cond.notify()
		self.cond.release()
	def ret(self):
		self.cond.acquire()
		while self.write == True:
			self.cond.wait()
		s = current_thread().name
		print(s , 'retrieves' , self.x)
		self.write = True
		self.cond.notify()
		self.cond.release()
def f1(buf):
	i = 1
	while True:
		buf.store(i)
		i += 1
		time.sleep(randint(1 , 4))
def f2(buf):
	while True:
		buf.ret()
		time.sleep(randint(1 , 4))
buf = buffer()
p = Thread(target = f1 , name = 'producer' , args = (buf,))
c = Thread(target = f2 , name = 'consumer' , args = (buf,))
p.start()
c.start()
print('Press ctrl + break or Fn+B to stop')

'''
2) Write  a  program  to  find  transpose  a  matrix
     Eg:  a =  [[10 , 20 ,  30 , 40] , [50 , 60 , 70 , 80] , [90 , 100 , 110 , 120]]
	 Ouput :   [[10 , 50 , 90] , [20 , 60 , 100] , [30 , 70 , 110] , [40 , 80 , 120]]

1) Input :  a =  [[10 , 20 ,  30 , 40] , [50 , 60 , 70 , 80] , [90 , 100 , 110 , 120]]	 

2) Initilaization
    --------------
	b = []	   
	row = []

3) x = [10 , 20 ,  30 , 40]
    row = [10]	
	a =  [[20 ,  30 , 40] , [50 , 60 , 70 , 80] , [90 , 100 , 110 , 120]]	 

4) x = [50 , 60 , 70 , 80]
    row = [10 , 50]
	a =  [[20 ,  30 , 40] , [60 , 70 , 80] , [90 , 100 , 110 , 120]]	 
	
5) x = [90 , 100 , 110 , 120]
    row = [10 , 50 , 90]
 	a =  [[20 ,  30 , 40] , [60 , 70 , 80] , [100 , 110 , 120]]	 
	
6) b = [[10 , 50 , 90]]	
    row = []
	
7) x = [20 , 30 , 40]
    row = [20]
	a =  [[30 , 40] , [60 , 70 , 80] , [100 , 110 , 120]]	
 
8) x = [60 , 70 , 80]
    row = [20 , 60]
	a =  [[30 , 40] , [70 , 80] , [100 , 110 , 120]]	
 
9) x = [100 , 110 , 120]
    row = [20 , 60 , 100]
	a =  [[30 , 40] , [70 , 80] , [110 , 120]]	 
	
10) b = [[10 , 50 , 90] , [20 , 60 , 100]]	
    row = []
and  so  on	
'''
def transpose(a):
	b = []
	while len(a[0]) > 0:
		row = []
		for x in a:
			row.append(x.pop(0))
		b.append(row)
	return b
a = eval(input('Enter nested list : '))
b = transpose(a)
print('Transpose = ', b)

'''
3) Write  a  function  to  print  number  of  500's , 200's , 100's , 50's , 20's , 10's , 5's ,  2's ,  1's   in  a  number

Let  input  be  2628
What  are  the  results ?  --->  500 - 5
											     100 - 1
											     20 - 1
											     5 - 1
											     2 - 1
											     1 - 1


		                       
1) List  b    --->   [5 , 0 , 1 , 0]     
		              	     
2) Let  input  be  2628
    2628 // 500 =  5
    2628 % 500 =  128
    128 // 200 =  0
    128 % 200 =  128
    128 // 100 =  1
    128 % 100 = 28
    28 // 50 = 0
    28 % 50 =  28
    and  so  on
'''
def denom(n):
	b = []
	for x in a:
		b.append(n // x)
		n = n % x
	return b
a = [500 , 200 , 100 , 50 , 20 , 10 , 5 , 2 , 1]
n = int(input('Enter any number : '))
b = denom(n)
for i in range(len(a)):
	if b[i] != 0:
		print(a[i] , '-' , b[i])
'''
3) Write  a  program  to  convert  arabic   number  to   roman  number

1000 -  M
900 - CM
500 - D
400 - CD
100 - C
90 - XC
50 - L
40 - XL
10 - X
9 - IX
5 - V
4 - IV
1 - I

Arabic  number : 3878
Roman  number :   '' + 'MMM' + '' + 'D' + '' + 
3878 // 1000 = 3
3878 % 1000 =  878
878 // 900 = 0
878 % 900 =  878
878 // 500 =  1
878 % 500 =   378
378 // 400 = 0
378 % 400 =  378
and  so  on
'''
def arabic_roman(n):
	a = [1000 , 900 , 500 , 400 , 100 , 90 , 50 , 40 , 10 , 9 , 5 , 4 , 1]
	b = ['M' , 'CM' , 'D' , 'CD' , 'C' , 'XC' , 'L' , 'XL' , 'X' , 'IX' , 'V' , 'IV' , 'I']
	s = ''
	for i in range(len(a)):
		s += b[i] * (n // a[i])
		n = n % a[i]
	return s
n = int(input('Enter arabic number : '))
r = arabic_roman(n)
print('Roman number : ' , r)