'''
Write  a  program  to  generate  all   prime  divisors  of  a  number  also  print  how  many  prime  divisors  are  existing

Hint:  Reuse  the  prime()  function  defined  in   prog3a   but  do  not  rewrite

1) What  are  the  outputs  if  input  is  30 ?  --->  Prime divisors : [2, 3, 5]
                                                                               Number  of  prime  divisors :  3

2) What  are  the  outputs  if  input  is  84 ?  --->  Prime divisors : [2, 3, 7]
                                                                               Number  of  prime  divisors :  3

3) What  are  the  outputs  if  input  is  49 ?  --->  Prime divisors : [7]
                                                                               Number  of  prime  divisors :  1
'''
def  prime_divisors(n):
	return   list  of  all  prime  divisors  of  'n'
Read  input
call  the  function
print  results



# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)  # a  :  10   b : 20
f1(b = 30 , a = 40)  # a  :  40   b : 30
f1(50 , 60)  # Error due to positional arguments are not allowed
f1(70 , b = 80) # Error due to positional arguments are not allowed
f1(a = 15 , 25)  # Error due to Positional argument (25) after keyword argument



#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)   # a  :  10    b :  20    c  :  30
f1(a = 40 , b = 50 , c = 60)  # a  :  40    b :  50    c  :  60
f1(c = 100 , b = 90 , a = 80)  # a  :  80    b :  90    c  :  100
f1(70 , 80 , c = 90) Error due to 80 is treated as positional argument for b. But b is keyword-only
f1(70 , 80 , 90) # Error due to 80 and 90 are positional
f1(c = 15 , b = 25 , 35) # Error due to Positional argument after keyword argument




# Identify error (Home  work)
def   f1(a  , b , *):
        pass
# Error : there should be atleast one argument after * in the function header
    
    
#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)  # a  :  10    b  :  20
f1(a = 30 ,  b = 40) # Error : due to positional arguments only can be passed becoz a and b are before / in the header function
f1(50 , b = 60) # Error : b should be positional argument only
f1(a = 70 , 80) # Error : Positional argument after keyword and also a should be positional argument only
    
    
    
# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) # a  :  10    b :  20    c  :  30
f1(40 , 50 , c = 60) # a  :  40    b :  50    c  :  60
f1(a = 70 , b = 80 , c = 90) # Error : a, b should be positional Argument
f1(a = 100 , b = 110 , 120) # Error 
f1(a = 130 , 140 , c = 150) # Error
f1(160 , b = 170 , 180)  # Error
f1(190 , b = 200 , c = 210) # Error




# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) # a  :  10    b  :  20    c  :  30    d  :  40    e  :  50    f  :  60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) # Error due to b should be positional
f1(1 , 2 , 3 , 4 , 5 , f = 6) # Error due to 5 as positional
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) # Error due to Positional argument 40 after keyword argument
f1(10 , 20 , 30 , 40 , e = 50 , f = 60) # a  :  10    b  :  20    c  :  30    d  :  40    e  :  50    f  :  60




# Identify error (Home  work)
def  f1(/ , a , b ,  c):  # There should be atleast one arg before /
        pass
def   f2(a , b , c , *):   # There should be atleast one arg after *
        pass

# Identify  error  (Home  work)
def  f4(* , a , b , c , /):   # cannot use / after *
	        pass
            
            
            
            
            
            
# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z) # 3rd  function :  10
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
print(add(100 , c = 200)) # 320
print(add(c = 100 , b = 200 , a = 300)) # 600
print(add(c = 100 , a = 200)) # 320
print(add()) # Error
print(add(a = 100 , 200)) # Error Positional argument after keyword
print(add(100 ,  , 300))  # Error due to value missing
print(add(100 ,  b , 300)) # Error








# Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d): # Non-default arguments b, d are placed after default arguments
	pass
def   f2(b , d , a = 10 , c = 20):  # Correct Order NO ERROR
	pass





#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20) # 20
f1()  # 10
f1(a = 30) # 30






# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200)) # a=100, b=200, c=10, d=20=330
print(add(100 , 200 , 300)) # a=100, b=200, c=300, d=20 -> 620
print(add(100 , 200 , 300 , 400)) # 100 + 200 + 300 + 400 -> 1000
print(add(b = 100 , a = 200))  # a=200, b=100, c=10, d=20  -> 330
print(add(100 , 200 , d = 300)) # a=100, b=200, c=10, d=300 --> 610
print(add(d = 100 , a = 200 , b = 300)) # a=200, b=300, c=10, d=100 --> 610
print(add(c = 100 , d = 200 , 300 , 400)) # Error dur to Positional arguments after keyword
print(add(100 , 200 , c = 300 , x = 400))  # Error due to x is not a parameter
print(add()) # Error due to missing Arguments




#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))  # 10
print(f1()) # 25
print(f2(20)) # 20
print(f2()) # Error




# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6) # ------
disp('$')  # $$$$
disp() # ****
disp(n = 5) # *****
disp(5) # Error
disp(n = 7 , ch = '%') # %%%%%%%
disp(7 , '@') # Error 
disp(7 , n = 6)  # Error
disp(ch = '!' ,  5)  # Error





# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
# End  of the function
print(power(2 , 6)) # 64
print(power(5)) # 25
print(power(b = 3 , a = 4.5))  # 91.125
print(power(3 + 4j)) # (-7+24j)
print(power(True))  # 1
def   power(b = 2 , a): 
 	 pass




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
print(add(10 , 20 , 30 , 40)) # 4-argument  function <nextLine>100
print(add(50 , 60 , 70)) # 4-argument  function <nextLine>184
print(add(80 , 90)) # 4-argument  function <nextLine>177
print(add(100)) # 4-argument  function <nextLine> 109
print(add()) # 4-argument  function <nextLine> 10




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
def   add(a = 10 , b , c):
        pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))
print(add(b = 60 , c = 70))
print(add(c = 80 , b = 90 , a = 100))
print(add(c = 25 , a = 43))
print(add(1 , 2 , 3))
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):
		pass
        
        
        
        
        
# Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 . _defaults_)




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
	Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
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
	Write  code  to  return  join  of  all  the  strings  passed  to  the  function  (1  line)
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
f1(a = 10 , (20 , 30 , 40))
f1(25 , b = (10 , 20 , 30))
f1(25 , a = (10 , 20 , 30))
f1((10 , 20 , 30) , 10 , 20 , 30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30)







# Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)
f1(50 , b = 60)
f1(b = 70)
f1(b = 10 , a = (20 , 30 , 40))
f1(b = 10 , (20 , 30 , 40))
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
f1(a = 1 , 2 , c = 3)
f1(1 , 2 , 3)
f1(a = 1 , b = 2 , c = 3)
f1(a = 25 , 100 , 200 , 300 , c = 35)





# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):
        pass
def  f2(*a , b):
        pass
def  f3(a , *b):
        pass
def  f4(a , b):
        pass
def    f5(a , *b , c):
        pass
def   f6( * , a , *b , c):
       pass
def   f7(a , *b , c ,  /):
       pass





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
	print(type(a)) # <class 'tuple'>
	print(a) # (25, 10.8, 'Hyd', True)
def   f2(**a):
	print(type(a)) # <class 'dict'>
	print(a)   # {'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)
    
    
#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')  # Emp  Number  :  25  	  Emp  Name  :  Sita  	  Salary  : 10000.0

def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)  
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)
    
    
    
    
# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)
print()
f1('Hyd' , 10 , 20 , 30)
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)
'''
25

Hyd
(10, 20, 30)

10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}'''