# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)#a  : 10 \t  b :  20
f1(b = 30 , a = 40)#a  : 40 \t  b :  30
f1(50 , 60)#error because positional arguments are not allowed
f1(70 , b = 80)#error because positional argument 70 positional argument
f1(a = 15 , 25)#error because positional argument is not comes after the keyword argument

#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)#a  :  10  \t  b :  20 \t  c  : 30
f1(a = 40 , b = 50 , c = 60)#a  :  40  \t  b :  50 \t  c  : 60
f1(c = 100 , b = 90 , a = 80)#a  :  80  \t  b :  90 \t  c  : 100 
f1(70 , 80 , c = 90)#error because b in not a positional argument
f1(70 , 80 , 90)#error because b 80 and 90 are not positional arguments
f1(c = 15 , b = 25 , 35)#a  :  35  \t  b :  25  \t  c  :  15
# Identify error (Home  work)
def   f1(a  , b , *):#error because atleast one argument after *
        pass
#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)#a  :  10  \t  b  :  20
f1(a = 30 ,  b = 40)#error because a and b should be positional arguments
f1(50 , b = 60)#error because b should be positional argument
f1(a = 70 , 80)#error a should be positional argument
# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)#a  :  10  \t  b :  20  \t  c  :  30 
f1(40 , 50 , c = 60)#a  :  40  \t  b :  50  \t  c  :  60 
f1(a = 70 , b = 80 , c = 90)#error because a and b should be positional arguments
f1(a = 100 , b = 110 , 120)#error because a and b should be positional arguments
f1(a = 130 , 140 , c = 150)#error because a should be positional argument
f1(160 , b = 170 , 180)#error because b should be positional argument
f1(190 , b = 200 , c = 210)#error because b should be positional argument
 # Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)#a:10  \t  b:20  \t  c:30  \t  d:40  \t  e:50 \t  f:60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)#error because b should be positional argument
f1(1 , 2 , 3 , 4 , 5 , f = 6)#error because e should be key word argument
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)#a:10  \t  b:20  \t  c:30  \t  d:40  \t  e:50 \t  f:60
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)#a:10  \t  b:20  \t  c:30  \t  d:40  \t  e:50 \t  f:60
# Identify error (Home  work)
def  f1(/ , a , b ,  c):#error because before / no arguments 
        pass
def   f2(a , b , c , *):#error because after * atleast one argument 
        pass
 # Identify  error  (Home  work)
def  f4(* , a , b , c , /):#error because * all arguments should be key word arguments and before /all arguments should be positional keywords
	        pass
 # Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)#1st  function :30
def  f1(y):
	print('2nd  function : ' , y)#2st  function :20
def  f1(z):
	print('3rd  function : ' , z)#3st  function :30
f1(z = 10)
f1(y = 20)
f1(x = 30)
 # Default  arguments  demo  program
def   add(a , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100))   #  150
print(add(100 , 200))  #  330
print(add(100 , 200 , 300))  #   600
print(add(100 , c = 200))#320
print(add(c = 100 , b = 200 , a = 300))#600
print(add(c = 100 , a = 200))#320
print(add())#error expected arguments
print(add(a = 100 , 200))#320
print(add(100 ,  , 300))#error  
print(add(100 ,  b , 300)#error 
      
# Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d):#error because after default argument non default argument is not permitted
	pass
def   f2(b , d , a = 10 , c = 20):#error because order is missing
	pass
 #  Find  outputs (Home  work)
def   f1(a = 10):
        print(a) 
# End  of  the  function
f1(20)#20
f1()#error
f1(a = 30)#30
 # Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))#330
print(add(100 , 200 , 300))#620
print(add(100 , 200 , 300 , 400))#1000
print(add(b = 100 , a = 200))#
print(add(100 , 200 , d = 300))#610
print(add(d = 100 , a = 200 , b = 300))#
print(add(c = 100 , d = 200 , 300 , 400))#1000
print(add(100 , 200 , c = 300 , x = 400))#error
print(add())#errir
#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))#10
print(f1())#error
print(f2(20))#20
print(f2())#error
 # Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)
disp('$')
disp()
disp(n = 5)
disp(5)
disp(n = 7 , ch = '%')
disp(7 , '@')
disp(7 , n = 6)
disp(ch = '!' ,  5)
# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
# End  of the function
print(power(2 , 6))#64
print(power(5))#25
print(power(b = 3 , a = 4.5))#91.125
print(power(3 + 4j))#
print(power(True))#1
def   power(b = 2 , a):
 	 pass
#  Find outputs  (Home  work)
def   add(a , b):
	print('2-argument  function')
	return a + b
def  add(a , b , c):
	print('3-argument  function')
	return a + b + c
def  add(a  = 1 , b  = 2 , c   = 3 , d = 4):
	print('4-argument  function')
	return a + b  + c + d
# End  of  the  function
print(add(10 , 20 , 30 , 40))#100
print(add(50 , 60 , 70))184
print(add(80 , 90))#177
print(add(100))#109
print(add())#10
# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)#170
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)#220
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)#55
#end
disp(10 , 20 , 30)
disp(40 , 50 , 60 , 70)
disp(80 , 90)
 # Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))#70
print(add())#error
print(add(a = 50))#70
print(add(b = 60 , a = 70))#130
print(add(80 , 90))#error because and b should be default arguments
 # Find  outputs(Home  work)
def   add(a = 10 , b , c):
        pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))#error
print(add(b = 60 , c = 70))#error
print(add(c = 80 , b = 90 , a = 100))#error
print(add(c = 25 , a = 43))#error
print(add(1 , 2 , 3))#error 
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):
		pass
  
Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)#[3,9,5,[6 , 7 , 8]]
#end  of  the  function
print('__defaults__  :  ' , f1.__defaults__)#([],)
f1(3)
print('__defaults__  :  ' , f1.__defaults__)#([3],)
f1(4 , [1 , 2 , 3])
print('__defaults__  :  ' , f1.__defaults__)#([3],)
f1(9)
print('__defaults__  :  ' , f1.__defaults__)#([3,9],)
f1(40 , [10 , 20 , 30])
print('__defaults__  :  ' , f1.__defaults__)#([3,9],)
f1(5)
print('__defaults__  :  ' , f1.__defaults__)#([3,9,5],)
f1([6 , 7 , 8])
print('__defaults__  :  ' , f1.__defaults__)#([3,9,5,[6 , 7 , 8]],)
# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1._defaults_)#([],)
print(f1(3))#[0,1,4]
print('_defaults  :  ' , f1._defaults_)#([0,1,4],)
print(f1(4 , [10 , 20 , 15 , 18]))#[10 , 20 , 15 , 18,0,1,4,9]
print('_defaults  :  ' , f1._defaults_)#([0,1,4],)
print(f1(5))#[0,1,4,0,1,4,9,16]
print('_defaults  :  ' , f1._defaults_)#([0,1,4,0,1,4,9,16],)
print(f1(a = [100 , 200 , 300],   x = 6 ))#[100 , 200 , 300,0,1,4,9,16,25]
print('_defaults  :  ' , f1._defaults_)#([0,1,4,0,1,4,9,16],)
print(f1(6))#[0,1,4,0,1,4,9,16,0,1,4,9,16,25]
print('_defaults  :  ' , f1._defaults_)#([0,1,4,0,1,4,9,16,0,1,4,9,16,25],)
Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)#HydSec
	print('b :  ' , b)#[1,2,3,1,2,3,1,2,3]
# End of the function
print('Default Values  :  ' , f1 . __defaults__)#('Hyd',[])
f1()
print('Default Values  :  ' , f1 . __defaults__)#('Hyd', [1, 2, 3])
f1()
print('Default Values  :  ' , f1 . __defaults__)#Default Values  :   ('Hyd', [1, 2, 3, 1, 2, 3])
f1()
#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)#(10, 20, 15, 18)<\n><class 'tuple'><\n>4
f1()#()<\n><class 'tuple'><\n>0
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})#([10, 20], (30, 40, 50), {60, 70, 80, 90})<\n><class 'tuple'><\n>3
f1('Hyd')#('Hyd',)<\n><class 'tuple'><\n>1
tpl = (100 , 200 , 150)
f1(tpl)#((100, 200, 150),)<\n><class 'tuple'><\n>1
f1(t = (10 , 20 , 30)) #   Error
#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function (Home  work)
def  avg(*a):
	Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #   Average  of  10 , 20 , 15 , 18   15.7
print(avg(25 , 10.8 , True))  #   Average  of  25 , 10.8 , True   12.266666666666667
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))#14.26
print(avg())#0
print(avg(25))#25.0
print(avg(3 + 4j , 5 + 6j))#(4+5j)
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))#error
# Write  a  function  to  concatenate  strings  passed  to  the  function ? (Home  work)
def  concat(*a):
	Write  code  to  return  join  of  all  the  strings  passed  to  the  function  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  #  Sankar<space>Dayal<space>Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))#Hyd <space>Is<space>Green<space>City
print(concat('Python', 'Is', 'A', 'Great', 'Language'))#Python <space>Is<space>A<space>Great<\n>Language
,.
print(concat())#empty
print(concat('Python'))#error
print(concat(1, 2, 3))#error
 #Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)#a : 10      b  :  (20, 30, 40)
f1(50 , 60)#a : 50      b  :  (60,)
f1(70)#a : 70      b  :  ()
f1(a = 80)#a : 80      b  :  ()
f1(b = (10 , 20 , 30) , a = 40)#error
f1()#a : 25      b  :  ()
f1(a = 10 , (20 , 30 , 40))#error
f1(25 , b = (10 , 20 , 30))#error
f1(25 , a = (10 , 20 , 30))#error
f1((10 , 20 , 30) , 10 , 20 , 30)#a : (10, 20, 30)      b  :  (10, 20, 30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30)#error
# Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)#a  :  (10, 20, 30)       b  :  40
f1(50 , b = 60)#a  :  (50,)       b  :  60
f1(b = 70)#a  :  ()       b  :  70
f1(b = 10 , a = (20 , 30 , 40))#error
f1(b = 10 , (20 , 30 , 40))#error
f1()#error
f1(10 , 20 , 30 , (10 , 20 , 30))#error
f1(10 , 20 , 30 , 40)#error
f1(25)#error
f1(10 , 20 , 30 , b = (10 , 20 , 30))#a  :  (10, 20, 30)       b  :  (10, 20, 30)
#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)#a  :  10      b  :  (20, 30, 40)      c  :  50
f1(60 , 70 , c = 80)#a  :  60      b  :  (70,)      c  :  80
f1(90 , c = 100)#a  :  90      b  :  ()      c  :  100
f1(a = 1 , 2 , c = 3)#error
f1(1 , 2 , 3)#error
f1(a = 1 , b = 2 , c = 3)#error
f1(a = 25 , 100 , 200 , 300 , c = 35)#error
# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):#invalid
        pass
def  f2(*a , b):#valid
        pass
def  f3(a , *b):#valid
        pass
def  f4(a , b):#valid
        pass
def    f5(a , *b , c):#valid
        pass
def   f6( * , a , *b , c):#invalid
       pass
def   f7(a , *b , c ,  /):#invalid
       pass
# Find  outputs  (Home  work)
def   f1(*a):
	print(a)#([10 , 20] , {30 , 40} , (50 , 60))
	print(type(a))#<class 'tuple'>
	for  x  in  a:
		print(x)#[10 , 20]<\n><class 'list'><\n>{30 , 40}<\n><class 'set'><\n> (50 , 60)<\n><class 'tuple>
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))
