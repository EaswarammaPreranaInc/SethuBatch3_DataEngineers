# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(4)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(3,2)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(1,2,3)

	


'''
Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
																		    Number  of   prime  numbers : 4
'''
'''def  prime_numbers(n):
	return  list  of  all  the  prime  numbers  between  2  and   n
Read  'n'  value
call  prime_numbers()  function  
print  the  list
print  number  of  prime  numbers'''
def primelist(n):
    a=[]
    for i in range(2,n):
        if i==2:
            a.append(i)
        elif isprime(i):
            a.append(i)
    return a
def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input())
x=primelist(n)
print(x)
print(len(x))