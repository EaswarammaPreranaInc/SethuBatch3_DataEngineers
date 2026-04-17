# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1()#call f1() before f1(x),f1(x,y),f1(x,y,z)
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(4)#call f1(x) before f1(x,y),f1(x,y,z)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(4,16)#call f1(x,y) before f1(x,y,z)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(4,16,40)##call f1(x,y,z)




'''
Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing
Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite
What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
Number  of   prime  numbers : 4
'''

from prime import prime
def prime_numbers(n):
    primes_list = []
    for i in range(2, n + 1):
        if prime(i):# this prime function is saved in prime.py you can see in the below of the this program
            primes_list.append(i)         
    return primes_list
n = int(input('Enter any integer number: '))
result = prime_numbers(n)
print(f"Prime numbers : {result}")
print(f"Number of prime numbers : {len(result)}")


'''
output
Enter any integer number: 10
Prime numbers : [2, 3, 5, 7]
Number of prime numbers : 4
Enter any integer number: 20
Prime numbers : [2, 3, 5, 7, 11, 13, 17, 19]
Number of prime numbers : 8
'''


'''
#prime.py
def prime(n):
    if n < 2:
        return False
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False 
    return True 
'''