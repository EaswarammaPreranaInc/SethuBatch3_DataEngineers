# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
##
def f1(*args):
    if len(args) == 0:
        print('No-argument function')
    elif len(args) == 1:
        print('Single argument function :', args[0])
    elif len(args) == 2:
        print('Two argument function :', args[0], args[1])
    elif len(args) == 3:
        print('Three argument function :', args[0], args[1], args[2])

# Calling all cases
f1()
f1(10)
f1(10, 20)
f1(10, 20, 30)
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
from prog3a import prime   # using given function

def prime_numbers(n):
    primes = []
    for i in range(2, n+1):
        if prime(i):   # using already defined function
            primes.append(i)
    return primes

# Read input
n = int(input("Enter n value: "))

# Function call
result = prime_numbers(n)

# Output
print("Prime numbers :", result)
print("Number of prime numbers :", len(result))