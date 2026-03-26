def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)  # a: 10    b: 20
f1(b = 30 , a = 40)  # a: 40    b: 30
f1(50 , 60)  # Error
f1(70 , b = 80) # Error
f1(a = 15 , 25)  # Error

def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)     # a:20     b:20    c:30
f1(a = 40 , b = 50 , c = 60) # a:40     b:50    c:60
f1(c = 100 , b = 90 , a = 80)# a:80     b:90    c:100
f1(70 , 80 , c = 90)    # Error
f1(70 , 80 , 90)        # Error
f1(c = 15 , b = 25 , 35) #Error

def   f1(a  , b , *):  # atleast one argument after the *
        pass

def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)          # a:10     b:20
f1(a = 30 ,  b = 40) # Error
f1(50 , b = 60)      # Error
f1(a = 70 , 80)      #Error

def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)    # a:10    b:20    c:30
f1(40 , 50 , c = 60)# a:40    b:50    c:60
f1(a = 70 , b = 80 , c = 90) # Error
f1(a = 100 , b = 110 , 120)  # Error
f1(a = 130 , 140 , c = 150) #  Error
f1(160 , b = 170 , 180) #Error
f1(190 , b = 200 , c = 210)  #Error


def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)# a:10   b:20    c:30    d:40    e:50    f:60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) # Error
f1(1 , 2 , 3 , 4 , 5 , f = 6) # Error
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) # Error
f1(10 , 20 , 30 , 40 , e = 50 , f = 60) #a:10   b:20    c:30    d:40    e:50    f:60


'''def  f1(/ , a , b ,  c):
        pass   error  because there atleast one arg before "/"
def   f2(a , b , c , *):
        pass error  because there atleast one arg after "*"'''


def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10)
f1(y = 20) Error
f1(x = 30) Error


def   add(a , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100))   #  150
print(add(100 , 200))  #  330
print(add(100 , 200 , 300))  #   600
print(add(100 , c = 200))   #320
print(add(c = 100 , b = 200 , a = 300)) #600
print(add(c = 100 , a = 200)) #320
print(add()) #  Error
print(add(a = 100 , 200))  ##print(add(100 ,  , 300)) # Error
print(add(100 ,  b , 300)) # Error

 # Identify  Error
'''def   f1(a = 10 ,  b ,  c = 20 ,  d):
	pass Error because there shouldn't be a argument after default argument'''
def   f2(b , d , a = 10 , c = 20):
	pass
 Find  ou

def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20) # 20
f1()    #10 
f1(a = 30) #30


def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))             #330
print(add(100 , 200 , 300))       #620
print(add(100 , 200 , 300 , 400)) #1020
print(add(b = 100 , a = 200))     # 330
print(add(100 , 200 , d = 300))   #610
print(add(d = 100 , a = 200 , b = 300)) #610
print(add(c = 100 , d = 200 , 300 , 400)) #Error
print(add(100 , 200 , c = 300 , x = 400)) # Error
print(add()) Error


def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10)) #10
print(f1())   #25
print(f2(20)) #20
print(f2())  #Error


def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6) #------
disp('$')     #$$$$
disp()        #****
disp(n = 5)   #*****
disp(5)       #20
disp(n = 7 , ch = '%') #%%%%%%%
disp(7 , '@')          #@@@@@@@
disp(7 , n = 6)        #42
disp(ch = '!' ,  5)   # Error


def  power(a , b  =  2):
        return  a ** b
# End  of the function
print(power(2 , 6))#64
print(power(5))  # 25
print(power(b = 3 , a = 4.5)) #91.125
print(power(3 + 4j))          #(-7+24j)
print(power(True)) #1


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
print(add(10 , 20 , 30 , 40)) # 4-argument function 100
print(add(50 , 60 , 70))      # 4-argument function 184
print(add(80 , 90))           # 4-argument function 177
print(add(100))               # 4-argument function 109
print(add())                  # 4-argument function 10


def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)  #3-argument  function :10,20,30  
disp(40 , 50 , 60 , 70) #Error
disp(80 , 90)      #3-argument  function  80 90 25

'''def   add(a = 10 , b , c):
        pass error because the non-default-arguments follows default arguments '''
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))  #120
print(add(b = 60 , c = 70))           #140
print(add(c = 80 , b = 90 , a = 100)) #170
print(add(c = 25 , a = 43)) # Error
print(add(1 , 2 , 3)) #Error
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__)
f1(3)                                         #[3]
print('_defaults_  :  ' , f1.__defaults__)    #([3],)
f1(4 , [1 , 2 , 3])                           #[1,2,3.4]
print('_defaults_  :  ' , f1.__defaults__)    #([3,9],)
f1(9)                                         #[3,9]
print('_defaults_  :  ' , f1.__defaults__)  
f1(40 , [10 , 20 , 30])                       #[10,20,30,40]
print('_defaults_  :  ' , f1.__defaults__)
f1(5)                                         #[3,9,5]
print('_defaults_  :  ' , f1.__defaults__)    #([3,9,5],)
f1([6 , 7 , 8])                               #[3,9,5,[6,7,8]]
print('_defaults_  :  ' , f1.__defaults__)    #([3,9,5,[6,7,8]],)



def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . __defaults__)    #(hyd,[])
f1()   #a: 'hydsec' b : [1,2,3]
print('Default Values  :  ' , f1 . __defaults__)    #(hyd,[1,2,3])

f1() #a:'hydsec' b:[1,2,3,1,2,3]
print('Default Values  :  ' , f1 . __defaults__)    #(hyd,[1,2,3,1,2,3])

f1() #HydSec b:[1,2,3,1,2,3,1,2,3]


def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18) #(10 , 20 , 15 , 18) <class 'tuple' > 4
f1() #()  <class 'tuple'> 0
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})#([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90}) <class 'tuple'> 3
f1('Hyd') #('Hyd',) <class 'tuple'> 1
tpl = (100 , 200 , 150)
f1(tpl) #((100 , 200 , 150)) <class 'tuple'> 1
f1(t = (10 , 20 , 30)) #   Error

def  avg(*a):
	return sum(a)/len(a)
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #   Average  of  10 , 20 , 15 , 18
print(avg(25 , 10.8 , True))  #   Average  of  25 , 10.8 , True
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg()) # Error divide by zero error
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
tpl = (10 , 20 , 15 , 18)
print(avg(tpl)) # Error

def  concat(*a):
	return " ".join(a)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  #  Sankar<space>Dayal<space>Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat(1, 2, 3)) # Error


def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40) # a:10  b:( 20 , 30 , 40)
f1(50 , 60)           # a:50 b:(60,)
f1(70)                # a:70 b:()
f1(a = 80 )           # a:80 b:()
f1(b = (10 , 20 , 30) , a = 40) #a:40 b:((10 , 20 , 30)) #Error
f1()
f1(a = 10 , (20 , 30 , 40))
f1(25 , b = (10 , 20 , 30))
f1(25 , a = (10 , 20 , 30)) # Error
f1((10 , 20 , 30) , 10 , 20 , 30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30)


def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
# End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')
                 # <class 'dict'> {RollNo : 10 , StudName : 'Rama  Rao'} 
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
                 #{EmpNo : 25 , EmpName : 'Sita' , Salary : 10000.0}
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
                 #{AcNo :30 , CustName : 'Kiran' , Balance : 20000.0 , Gender:'m'}
disp()
                #<class 'dict'> {}

def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)       #<class 'tuple'> (25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)
                                   #<class 'dict'> {EmpNum : 25 , EmpName :  'Sita' , Salary : 10000.0}


def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
                                             #Emp  Number  :  25  \t  Emp  Name  :  Sita    Salary  :	10000.0
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)   #Error

f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
                            #{empno:25 , ename:'Sita' , sal:10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)
                            #{eno:25 , empname:'Sita' , salary:10000.0}

def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25) # 25
print()
f1('Hyd' , 10 , 20 , 30)
#hyd
#(10 , 20 , 30)
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)
#10.8
#( 25 , 'Hyd' , True )
#{EmpNo:12 , EmpName:'Rama  Rao' , Salary:10000.0}