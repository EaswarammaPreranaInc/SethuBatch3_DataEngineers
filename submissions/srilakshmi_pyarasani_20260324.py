1) Modify  following  program  such  that  every  function  should  be  executed
def  f1(x = None, y=None, z=None):
    if x is None and y is None and z is None:
	print('No-argument  function')
    elif  y is None and z is None:
	print('Single  argument  function  : ' , x)
    elif z is None:
	print('Two  argument  function : ' , x , y)
    else:
	print('Three  argument  function : ' , x , y , z)

f1()
f1(10)
f1(10, 20)
f1(10,20, 30)


2) Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
Number  of   prime  numbers : 4
'''
from prog3a import prime

def  prime_numbers(n):
	prime = []
	for i range(2, n+1):
            if prime(i):
                  prime.append(i)
        return primes

n = int(input("Enter a number:"))
res = prime_numbers(n)
print("Prime numbers:", result)










