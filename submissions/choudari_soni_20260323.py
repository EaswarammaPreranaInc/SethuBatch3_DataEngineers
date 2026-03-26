#  Find  outputs
def  f1():
		print('f1  Function')#fl function <\n>None
		f2()
def  f2():
		print('f2  function')#f2 function <\n>None
f1()

#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))  #  print(30)
print(add('Hyder' , 'abad'))#Hyderabad
print(add(10.8 , 20.6))#31.4
print(add(True , False))#1
print(add(3 + 4j , 5 + 6j))#8+10j
print(add(25 , 10.8))#35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))#25,10.8,'Hyd',True,None,3+4j,'Sec'
print(add(10 , '20'))#error

# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')#No-argument  function<\n>None
def  f1(x):
	print('Single  argument  function  : ' , x)#Single  argument  function  :60
def  f1(x , y):
	print('Two  argument  function : ' , x , y)#Two  argument  function : 40,50
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)#Three  argument  function :10,20,30
f1(10 , 20 , 30)
f1(40 , 50)  
f1(60)  
f1()

# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')#Emp Number : 25  Emp Name  :Rama Rao   Salary  : 10000.0 
# End  of  the  function                                                                #Emp Number : sita  Emp Name  :20000.0   Salary  : 35 
disp(25 , 'Rama  Rao' , 10000.0)                                                        #None
disp('Sita' , 20000.0 , 35)

# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')#a:10   b:20    c:30
# End  of  the  function                                    #a:25   b:10.8  c:'Hyd'
f1(a = 10 , b = 20 , c = 30)                                #a:50.2 b:40.7  c:60.5
f1(25 , 10.8 , 'Hyd')                                       #a = 'Cyb' b = 'Sec'  c = 'Hyd'   
f1(b = 40.7 , a = 50.2 , c = 60.5)                          #a = True   b = None   c = 3 + 4j     
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')                       #a:25   b:10.8  c:'Hyd'
f1(c = 3 + 4j , a = True , b = None)                        #a:25   b = 'Hyd' c = 10.8
f1(25 , c = 10.8 , b = 'Hyd')                               #a:True   b : 'Hyd' c: None 
f1(a = 100 , 200 , 300)  #   Error
f1(True , None , b = 'Hyd')
f1(10 , 20 , x = 30)                                        #error
f1(10 , 20)                                                 #None

# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')#Emp  Number :   25  	  Emp  Name : Rama Rao       	  Salary : 10000.0
# End  of  the  function     #Emp  Number :   35  	  Emp  Name : Sita           	  Salary : 20000.0
disp(25 , 'Rama Rao' , 10000.0)#Emp  Number : Rama  Rao  	  Emp  Name : 30000.0       	  Salary : 20
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)#None
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)

#  Tricky  program
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))#23
print(f1(*[6 , 7 , 8]))#62
print(f1([6 , 7 , 8]))#error
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))#16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6}))#14
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))#error
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})#'c' : 2 , 'b' :  4 , 'a' : 6
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))#error

# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a))#error because reverse is used after a
print(sorted(a , rev = True))#error because a is used after the rev
print(25 , 10.8 , 'Hyd' , separator = '\t')#error because didn't use separator
print(25 , 10.8 , 'Hyd' , endofline = '\t')#error because don't use endofline
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')