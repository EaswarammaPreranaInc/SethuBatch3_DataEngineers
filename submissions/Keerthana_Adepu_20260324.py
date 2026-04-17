# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(1)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(1 , 2)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(1 , 2 , 3)


#1
'''
Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
Number  of   prime  numbers : 4
'''
def prime(n):
    if n < 2:
        return False
    
    for i in range(2 , n // 2 + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(n):
    p = []

    for i in range(2, n + 1):
        if prime(i):
            p.append(i)
    return p

n = int(input('Prime numbers upto which number?'))

res = prime_numbers(n)

print('Prime Numbers:', res)

print('Number of Prime Numbers:',len(res))
