'''
Write  a  program  to  generate  all   prime  divisors  of  a  number  also  print  how  many  prime  divisors  are  existing

Hint:  Reuse  the  prime()  function  defined  in   prog3a   but  do  not  rewrite

1) What  are  the  outputs  if  input  is  30 ?  --->  Prime divisors : [2, 3, 5]
                                                                               Number  of  prime  divisors :  3

2) What  are  the  outputs  if  input  is  84 ?  --->  Prime divisors : [2, 3, 7]
                                                                               Number  of  prime  divisors :  3

3) What  are  the  outputs  if  input  is  49 ?  --->  Prime divisors : [7]
                                                                               Number  of  prime  divisors :  1
																			   
'''
n = int(input('Enter a Value : '))
def prime(n):
	for i in range(2, n//2+1):
		if n % i == 0:
			return False
	return True
a = []
def prime_divisors(n):
    for i in range(2, n+1):
        if prime(i) and n%i == 0:
            a.append(i)
    return a
		   
print(prime_divisors(n))
