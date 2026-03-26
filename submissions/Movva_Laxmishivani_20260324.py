
'''
# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)


# Modified code
def f1():
    print('No-argument function')
f1()
def f1(x):
    print('Single argument function :', x)
f1(10)
def f1(x, y):
    print('Two argument function :', x, y)
f1(10, 20)
def f1(x, y, z):
    print('Three argument function :', x, y, z)
f1(10, 20, 30)


Output:
No-argument function
Single argument function : 10
Two argument function : 10 20
Three argument function : 10 20 30
'''

'''
Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
																		    Number  of   prime  numbers : 4

def  prime_numbers(n):
	return  list  of  all  the  prime  numbers  between  2  and   n
Read  'n'  value
call  prime_numbers()  function  
print  the  list
print  number  of  prime  numbers
'''

from primefunc import prime  

def prime_numbers(n):
    res = []
    for i in range(2, n+1):
        if prime(i):     
            res.append(i)
    return res

n = int(input("Enter n: "))
lst = prime_numbers(n)
print("Prime numbers :", lst)
print("Number of prime numbers :", len(lst))