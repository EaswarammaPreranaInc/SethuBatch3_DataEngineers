# Find  outputs
def  f1():
		print('f1  Function')
		f2()
def  f2():
		print('f2  function')
f1()
 # Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)
f1(40 , 50)  
f1(60)  
f1()
 #  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))  #  print(30)
print(add('Hyder' , 'abad'))
print(add(10.8 , 20.6))
print(add(True , False))
print(add(3 + 4j , 5 + 6j))
print(add(25 , 10.8))
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))
print(add(10 , '20'))



'''
1) What  are  the  three  events  in  execution  of  add(10 , 20) ?  --->
	a) Executes  add()  function  and  passes  10  and  20  to  the  function
	b) Copies  10  and  20  to  formal  parameters  'a'  and   'b'
	c) Function  returns  30  which  is  returned  to  the  function  call  add(10 , 20)

2) Finally  add(10 , 20)  is  30

3) int  add(int  a , int  b)
     {
     		return  a +  b;
     }
	 add("Hyder"  ,  "a…
[12:39 pm, 23/3/2026] +91 99482 50500: '''

def   prime(n):   
	return  True  when 'n'  is  pr…
[12:39 pm, 23/3/2026] +91 99482 50500: # Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)
disp('Sita' , 20000.0 , 35)
[1:12 pm, 23/3/2026] +91 99482 50500: '''
Write  a  function  to  print  number  in  words

Let  input  be  123456789
What  is  the  output ?  --->  Tweleve  crores  thirty  four  lakhs  fifty  six  thousand  seven  hundred  eighty  nine

1) a = ["" , "One" , "Two" , "Three" , "Four" , "Five" , "Six" , "Seven" , "Eight" , "Nine" , "Ten" ,   "Eleven" , "Twelve" ,
           "Thirteen" , "Fourteen" , "Fifteen" , "Sixteen" , "Seventeen" ,  "Eightteen" , "Nineteen"]

2) b = [""  , "" , "Twenty" , "Thirty" , "Forty" , "Fifty" , "Sixty" , "Seventy" , "Eighty" , "Ninety"]
            0     1          2              3            4             5           6              7               8               9

3) How  to  print  92  in  words ?  --->  b[92 // 10]  and  a[92 % 10]  = b[9]  and  a[2]
    How  to…
[1:19 pm, 23/3/2026] +91 99482 50500: # Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)
f1(25 , 10.8 , 'Hyd')
f1(b = 40.7 , a = 50.2 , c = 60.5)
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')
f1(c = 3 + 4j , a = True , b = None)
f1(25 , c = 10.8 , b = 'Hyd')
f1(a = 100 , 200 , 300)  #   Error
f1(True , None , b = 'Hyd')
f1(10 , 20 , x = 30)
f1(10 , 20)
[1:30 pm, 23/3/2026] +91 99482 50500: # Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)
[1:30 pm, 23/3/2026] +91 99482 50500: #  Tricky  program
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))
print(f1(*[6 , 7 , 8]))
print(f1([6 , 7 , 8]))
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6}))
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))
[1:30 pm, 23/3/2026] +91 99482 50500: # Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a))
print(sorted(a , rev = True))
print(25 , 10.8 , 'Hyd' , separator = '\t')
print(25 , 10.8 , 'Hyd' , endofline = '\t')
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')


[11:31 am, 24/3/2026] +91 99482 50500: # Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
[12:04 pm, 24/3/2026] +91 99482 50500: '''
												    
'''
def  prime_numbers(n):
	return  list  of  all  the  prime  numbers  between  2  and   n
Read  'n'  value
call  prime_numbers()  function  
print  the  list
print  number  of  prime  numbers