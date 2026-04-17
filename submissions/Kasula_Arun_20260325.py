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
f1(a = 10 , b = 20)  # a  :  10  \t  b : 20
f1(b = 30 , a = 40)  #a  :  30  \t  b :  40
f1(50 , 60)       # error no positional args 
f1(70 , b = 80)    #error no positional agrs
f1(a = 15 , 25)    # after KA there should not be PA




 #Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)       #a  :  10  \t  b :  20  \t  c  :  30
f1(a = 40 , b = 50 , c = 60)   #a  :  40  \t  b :  50  \t  c  :  80
f1(c = 100 , b = 90 , a = 80)  #a  :  80  \t  b :  90  \t  c  :  100
f1(70 , 80 , c = 90)           # error 'a' can be any arg not b
f1(70 , 80 , 90)               # error 'a' can be any arg not b and c
f1(c = 15 , b = 25 , 35)       # error no P args after K agrs



# Identify error (Home  work)
def   f1(a  , b , *):
        pass
# after * there should be atleast one arg


 #  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)          # a  :  10  \t  b  :  20
f1(a = 30 ,  b = 40)  #error no k args
f1(50 , b = 60)      # no K args
f1(a = 70 , 80)      # there should be no P args after K args




# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)     #a  :  10  \t  b :  20  \t  c  :30  
f1(40 , 50 , c = 60) #a  :  40  \t  b :  50  \t  c  :60  
f1(a = 70 , b = 80 , c = 90) # #error a and b should only be PA
f1(a = 100 , b = 110 , 120)  # no P args after K args
f1(a = 130 , 140 , c = 150)  # 'a' should be only P arg
f1(160 , b = 170 , 180)      #  'b' should be only P arg
f1(190 , b = 200 , c = 210)  #  'b' should be only P arg



# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)
    #a  :  10  	  b  :  20  	  c  :  30  	  d  :  40  	  e  :  50  	  f  :  60
f1(1 , 2 , 3 , 4 , 5 , f = 6) #error
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)  #error
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)
    #a  :  10  	  b  :  20  	  c  :  30  	  d  :  40  	  e  :  50  	  f  :  60


# Identify error (Home  work)
def  f1(/ , a , b ,  c):  #error there should be atleast one arg before /
        pass
def   f2(a , b , c , *):  #error there should be atleast one arg after *
        pass



# Identify  error  (Home  work)
def  f4(* , a , b , c , /):        # error there can be either / or * but not both
	        pass                 
                                



# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)           #discarded
def  f1(y):
	print('2nd  function : ' , y)           #discarded
def  f1(z):
	print('3rd  function : ' , z)          #10
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
print(add(100 , c = 200))       #  320
print(add(c = 100 , b = 200 , a = 300))   #600
print(add(c = 100 , a = 200))      #320
print(add()) #error
print(add(a = 100 , 200))  #no P args after K args
print(add(100 ,  , 300))   #error in syntax
print(add(100 ,  b , 300)) #   error
 
 
 
 
 
 # Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d):   #no non - default after default
	pass
def   f2(b , d , a = 10 , c = 20):      # no ERROR
	pass
 
 
 
 
 
 
 #  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)   # 20
f1()         # 10
f1(a = 30)    #30





# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))   #330
print(add(100 , 200 , 300))     #620
print(add(100 , 200 , 300 , 400))   #1000
print(add(b = 100 , a = 200))    #330
print(add(100 , 200 , d = 300))   #610
print(add(d = 100 , a = 200 , b = 300))  #610
print(add(c = 100 , d = 200 , 300 , 400))  # no non- default after default
print(add(100 , 200 , c = 300 , x = 400))  #x is not defined
print(add())  #error



#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))    #10
print(f1())      #25
print(f2(20))    #20
print(f2())      #error




# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)   # '------'
disp('$')       #'$$$$'
disp()          #'****'
disp(n = 5)     #'*****'
disp(5)         # 20
disp(n = 7 , ch = '%')   #'%%%%%%%'
disp(7 , '@')       #'@@@@@@@'
disp(7 , n = 6)      #42
disp(ch = '!' ,  5)    # no P args after K args



# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
# End  of the function
print(power(2 , 6))    #64
print(power(5))        #25
print(power(b = 3 , a = 4.5))  #  error
print(power(3 + 4j))      #error
print(power(True))            #1
def   power(b = 2 , a):      # no non- default after default
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
print(add(10 , 20 , 30 , 40))  
'''
4-argument  function
100

'''
print(add(50 , 60 , 70))
'''
4-argument  function
184

'''
print(add(80 , 90))
'''
4-argument  function
177

'''
print(add(100))
'''
4-argument  function
109
'''
print(add())

'''
4-argument  function
100

'''



# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)         #3-argument  function  :  10 20 30
disp(40 , 50 , 60 , 70)    #error
disp(80 , 90)              #3-argument  function  :  80 90 25



# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))   #70
print(add())                  #30
print(add(a = 50))            #70
print(add(b = 60 , a = 70))    #130
print(add(80 , 90))             #only K args




# Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 . __defaults__)     #([],)




# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1._defaults_)
f1(3)
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
[12:31 PM, 3/25/2026] +91 99482 50500: # Find  outputs(Home  work)
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
[12:31 PM, 3/25/2026] +91 99482 50500: # Find  outputs
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
    return " ".join(a)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  #  Sankar<space>Dayal<space>Sarma
print(concat('Hyd', 'Is', 'Green', 'City')) #Hyd<space>Is<space>Green<space>City
print(concat('Python', 'Is', 'A', 'Great', 'Language')) #Python<space>IS<space>A<space>Great<space>Language
print(concat()) # nothing
print(concat('Python')) #Python
print(concat(1, 2, 3)) #error






#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)  #a : 10  \t   b  : (20, 30, 40) 
f1(50 , 60)   #a : 50  \t   b  :  (60,)
f1(70)   # a : 70  \t   b  :  ()
f1(a = 80)   #a : 80  \t   b  :  ()
f1(b = (10 , 20 , 30) , a = 40)   #error
f1() #a : 25  \t   b  : () 
f1(a = 10 , (20 , 30 , 40))   # Error
f1(25 , b = (10 , 20 , 30)) #error
f1(25 , a = (10 , 20 , 30))  #error
f1((10 , 20 , 30) , 10 , 20 , 30)  #a : (10, 20, 30)  \t   b  :  (10, 20, 30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30)   # error no P args after K args





 # Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)                        #a : (10, 20, 30)  \t   b  :  40
f1(50 , b = 60)                                  #a : (50) \t   b  :      60
f1(b = 70)                                       #a : () \t   b  :  70
f1(b = 10 , a = (20 , 30 , 40))                  # a canoot be Ka arg  
f1(b = 10 , (20 , 30 , 40))                      # no P args after K args
f1()                                             # error 
f1(10 , 20 , 30 , (10 , 20 , 30))                # error
f1(10 , 20 , 30 , 40)                            # error
f1(25)                                           # error
f1(10 , 20 , 30 , b = (10 , 20 , 30))            #a : (10, 20, 30)  \t   b  :  (10, 20, 30)





 #Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)   #a  :  10  \t  b  :  (20, 30, 40)  \t  c  : 50 
f1(60 , 70 , c = 80)           # a  :  60   \t  b  :  (70,)  \t  c  :  80
f1(90 , c = 100)               # a  :  90  \t  b  :  ()  \t  c  :   100
f1(a = 1 , 2 , c = 3)           #error
f1(1 , 2 , 3)               #error 
f1(a = 1 , b = 2 , c = 3)        #error
f1(a = 25 , 100 , 200 , 300 , c = 35)   #error







 # Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):              #error
        pass                 
def  f2(*a , b):                 #valid
        pass
def  f3(a , *b):                 #valid
        pass
def  f4(a , b):                 #valid
        pass
def    f5(a , *b , c):          # valid
        pass
def   f6( * , a , *b , c):       # invalid
       pass
def   f7(a , *b , c ,  /):         #invalid
       
       pass





# Find  outputs  (Home  work)
def   f1(*a):
	print(a)               #([10 , 20] , {30 , 40} , (50 , 60))
	print(type(a))           #<class 'tuple'>
	for  x  in  a:
		print(x)               
		print(type(x))
                
'''
[10 , 20]
<class 'list'>
{30, 40}
<class 'set'>
(50, 60)
<class 'tuple'>



'''
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
'''
Results
<class 'dict'>
{2 elements}

Results
<class 'dict'>
{3 elements}

Results
<class 'dict'>
{4 elements}

Results
<class 'dict'>
{}


'''


# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()
'''
Results
Empno...25 
Empname...'Rama  Rao' 
Salary...10000.0 
Gender...'m'

Results
'''


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

'''
<class 'tuple'>
(25 , 10.8 , 'Hyd' , True)

<class 'dict'>
{EmpNum : 25 , EmpName :  'Sita' , Salary : 10000.0}

'''


 #  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)   #'Emp  Number  :  25  \t  Emp  Name  :  'Sita'  \t  Salary  :	10000.0
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)     #error
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)           #{empno : 25 , ename : 'Sita' , sal : 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)       # {eno : 25 , empname : 'Sita' , salary : 10000.0}
