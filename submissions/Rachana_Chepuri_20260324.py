'''Modify  following  program  such  that  every  function  should  be  executed'''
def  f1():
	print('No-argument  function')#Discard
def  f1(x):
	print('Single  argument  function  : ' , x)#Discard
def  f1(x , y):
	print('Two  argument  function : ' , x , y)#Discard
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)#Three argument function : 1 2 3
	
'''
Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
																		    Number  of   prime  numbers : 4
'''
def prime_numbers(n):
    primes = []
    for i in range(2, n+1):
        if prime(i):
            primes.append(i)
    return primes  

n = int(input("Enter n: "))
prime_list = prime_numbers(n)
print("Prime numbers:", prime_list)
print("Number of prime numbers:", len(prime_list))
