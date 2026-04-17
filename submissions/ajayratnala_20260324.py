'''
1) # Modify  following  program  such  that  every  function  should  be  executed
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
f1()
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1()
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1()

'''
2) Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
Number  of   prime  numbers : 4
'''

def prime(n):
    if n < 2:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True
def prime_numbers(n):
    a = []
    for i in range(2, n+1):
        if prime(i):
            a.append(i)
    return a
n = int(input('Enter number : '))
res = prime_numbers(n)
print('Prime numbers :', res)
print('Number of prime numbers :', len(res))