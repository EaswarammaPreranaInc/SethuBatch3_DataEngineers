from Rajesh_Veerisatti_20260324 import prime
# Step 2: Function to get prime divisors
def prime_divisors(n):
    divisors = []
    
    for i in range(2, n + 1):
        if n % i == 0 and prime(i):
            divisors.append(i)
    
    return divisors
# Step 3: Read input and print results
n = int(input("Enter a number: "))

result = prime_divisors(n)

print("Prime divisors :", result)
print("Number of prime divisors :", len(result))

# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20) # a:10      b:20
f1(b = 30 , a = 40) # a:40      b:30
f1(50 , 60) # a:50      b:60
f1(70 , b = 80) # a:70  b:80
 #f1(a = 15 , 25) # after refferences two arruguments are not possible
 #Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)
f1(a = 40 , b = 50 , c = 60)
f1(c = 100 , b = 90 , a = 80)
f1(70 , 80 , c = 90)
f1(70 , 80 , 90)
# f1(c = 15 , b = 25 , 35) # after referencess two references are not possible 
 # Identify error (Home  work)
#def   f1(a  , b , *):
       # pass # * is a operator not a arugument
#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)
f1(a = 30 ,  b = 40)
f1(50 , b = 60)
# f1(a = 70 , 80) # after reference two arruguments are not possible
# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)
f1(40 , 50 , c = 60)
f1(a = 70 , b = 80 , c = 90)
# f1(a = 100 , b = 110 , 120) #  here 'a' is valid but not 'b' becz after reference two arruguments are not possible
# f1(a = 130 , 140 , c = 150) # after reference two arruguments are not possible
# f1(160 , b = 170 , 180) # first and second arruguments are valid but not 3rd becz after the refference two arruguments are not permited
f1(190 , b = 200 , c = 210)
# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)
f1(1 , 2 , 3 , 4 , 5 , f = 6)
#f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) # 
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)
# Identify error (Home  work)
# def  f1(/ , a , b ,  c):
       #  pass # / is a opperator but not refferce arrgument
# def   f2(a , b , c , *):
       # pass  * is a opperator but not refferce arrgument
# Identify  error  (Home  work)
# def  f4(* , a , b , c , /): 
	               # pass  * is a arrgument but not / opperator refferce arrgument

# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
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
print(add(100 , c = 200))
print(add(c = 100 , b = 200 , a = 300))
print(add(c = 100 , a = 200))
print(add())
# print(add(a = 100 , 200)) # after refference two arrguments are not permited
#print(add(100 ,  , 300)) # here 2nd arrugument is missing
#print(add(100 ,  b , 300)) #  here 2nd arrugument is str object but int and strs are not concate nate

# Identify  Error
#def   f1(a = 10 ,  b ,  c = 20 ,  d):
	#pass in 'a' having two arruguments which is not possible
def   f2(b , d , a = 10 , c = 20):
	pass
#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)
f1()
f1(a = 30)
# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))
print(add(100 , 200 , 300))
print(add(100 , 200 , 300 , 400))
print(add(b = 100 , a = 200))
print(add(100 , 200 , d = 300))
print(add(d = 100 , a = 200 , b = 300))
# print(add(c = 100 , d = 200 , 300 , 400)) # 'c' is valid but 'd' having 3 arrguments which is not possible
print(add(100 , 200 , c = 300 , x = 400))
print(add())
#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))
print(f1())
print(f2(20))
print(f2())
 # Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6) # ------
disp('$') # $
disp() #
disp(n = 5) # <5spaces>
disp(5) # 5
disp(n = 7 , ch = '%') # %%%%%%%
disp(7 , '@') # @@@@@@@
disp(7 , n = 6) # 42
# disp(ch = '!' ,  5) # it is valid for strs ,spcl chars but not operators
# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
# End  of the function
print(power(2 , 6))
print(power(5))
print(power(b = 3 , a = 4.5))
print(power(3 + 4j))
print(power(True))
# def   power(b = 2 , a): 
 	# pass # str and int are not 
 # Find outputs  (Home  work)
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
print(add(10 , 20 , 30 , 40))
print(add(50 , 60 , 70))
print(add(80 , 90))
print(add(100))
print(add())
# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)
disp(40 , 50 , 60 , 70)
disp(80 , 90)
 # Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))
print(add())
print(add(a = 50))
print(add(b = 60 , a = 70))
print(add(80 , 90))
 # Find  outputs(Home  work)
#def   add(a = 10 , b , c):
        #pass # after reference three arguments are not possible
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))
print(add(b = 60 , c = 70))
print(add(c = 80 , b = 90 , a = 100))
print(add(c = 25 , a = 43))
print(add(1 , 2 , 3))
#def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):
		#pass # 'a' is defined in def function  bis defined here but 'c' is nor not defined here and function
                
# Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 . __defaults__)
# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1._defaults_)
f1(3) # 
print('_defaults_  :  ' , f1._defaults_)
f1(4 , [1 , 2 , 3])
print('_defaults_  :  ' , f1._defaults_)
f1(9)
print('_defaults_  :  ' , f1._defaults_)
f1(40 , [10 , 20 , 30])
print('_defaults_  :  ' , f1._defaults_)
f1(5)
print('_defaults_  :  ' , f1._defaults_)
f1([6 , 7 , 8])
print('_defaults_  :  ' , f1._defaults_)
# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1._defaults_)
print(f1(3))
print('_defaults  :  ' , f1._defaults_)
print(f1(4 , [10 , 20 , 15 , 18]))
print('_defaults  :  ' , f1._defaults_)
print(f1(5))
print('_defaults  :  ' , f1._defaults_)
print(f1(a = [100 , 200 , 300],   x = 6 ))
print('_defaults  :  ' , f1._defaults_)
print(f1(6))
print('_defaults  :  ' , f1._defaults_)
# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . _defaults_)
f1()
print('Default Values  :  ' , f1 . _defaults_)
f1()
print('Default Values  :  ' , f1 . _defaults_)
f1()
#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)
f1()
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
f1('Hyd')
tpl = (100 , 200 , 150)
f1(tpl)
f1(t = (10 , 20 , 30)) #   Error
#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function (Home  work)
def  avg(*a):
        print(avg(*a))	#Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #   Average  of  10 , 20 , 15 , 18
print(avg(25 , 10.8 , True))  #   Average  of  25 , 10.8 , True
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg())
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))
# Write  a  function  to  concatenate  strings  passed  to  the  function ? (Home  work)
def  concat(*a):
	print(concat(*a)) # Write  code  to  return  join  of  all  the  strings  passed  to  the  function  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  #  Sankar<space>Dayal<space>Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat(1, 2, 3))
#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)
f1(50 , 60)
f1(70)
f1(a = 80)
f1(b = (10 , 20 , 30) , a = 40)
f1()
# f1(a = 10 , (20 , 30 , 40)) # after refference does not support to having two argguments
f1(25 , b = (10 , 20 , 30))
f1(25 , a = (10 , 20 , 30))
f1((10 , 20 , 30) , 10 , 20 , 30)
#f1(a = (10 , 20 , 30) , 10 , 20 , 30)# # after refference does not support to having too many  argguments
f1(25 , b = (10 , 20 , 30))
# Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)
f1(50 , b = 60)
f1(b = 70)
f1(b = 10 , a = (20 , 30 , 40))
# f1(b = 10 , (20 , 30 , 40)) # after refference does not support to having two argguments
f1(25 , b = (10 , 20 , 30))
f1()
f1(10 , 20 , 30 , (10 , 20 , 30))
f1(10 , 20 , 30 , 40)
f1(25)
f1(10 , 20 , 30 , b = (10 , 20 , 30))
#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)
f1(60 , 70 , c = 80)
f1(90 , c = 100)
# f1(a = 1 , 2 , c = 3) # 2nd oppendent should be sets or lists or dict ortuples
f1(1 , 2 , 3)
f1(a = 1 , b = 2 , c = 3)
# f1(a = 25 , 100 , 200 , 300 , c = 35) # after 'a' refference containing three arruguments are not supported
# Which  of  the  following  are  valid  ?  (Home  work)
# def   f1(*a , *b):
        #pass
def  f2(*a , b):
        pass
def  f3(a , *b):
        pass
def  f4(a , b):
        pass
def    f5(a , *b , c):
        pass
# def   f6( * , a , *b , c):
       # pass
#def   f7(a , *b , c ,  /):
      # pass
# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))
# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
# End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
disp()
# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()
# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)
#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)  
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)
 