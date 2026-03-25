# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(1)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(1,2)
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

from ajithkumar_medisetti_20260323  import prime
def  prime_numbers(n):
	global li
	li=[]
	global count
	count=0
	for i in range(2,n+1):
		if prime(i):
			li.append(i)
			count+=1
n=int(input('Enter n value : ')) #Read  'n'  value
prime_numbers(n)#call  prime_numbers()  function  
print(li)#print  the  list
print(f'Number of prime numbers are {count}')#print  number  of  prime  numbers