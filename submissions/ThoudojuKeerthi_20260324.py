 # Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
 '''
def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(10)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(10, 'keerthi')
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10, 'keerthi', 10.8)

Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
																		    Number  of   prime  numbers : 4
'''
def  prime_numbers(n):
	return  list  of  all  the  prime  numbers  between  2  and   n
Read  'n'  value
call  prime_numbers()  function  
print  the  list
print  number  of  prime  numbers


def prime_numbers(n):
	l=[]
	for i in range(2, n+1):
		isPrime(i):
			l.append(i)
	if len(l)>0:
		return (l, len(l))
	return ('No prime number in range of n, 0)

def isPrime(i):
	if i == 2 or i == 3:
		return True
	if i%2 == 0
		return False
	for j in range(3, int(i**0.5), 2):
		if i%j ==0:
			return False
	return True
n=int(input('Enter a number'))
prime_numbers(n)

	