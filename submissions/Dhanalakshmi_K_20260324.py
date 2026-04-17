
# Modify  following  program  such  that  every  function  should  be  executed
def  f1(): 
	print('No-argument  function')
f1()
def  f1(x):  
	print('Single  argument  function  : ' , x)
f1(10)
def  f1(x , y): 
	print('Two  argument  function : ' , x , y)
f1(10, 20)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10, 20, 30)



'''
Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
																		    Number  of   prime  numbers : 4
'''
'''
def  prime_numbers(n):
	return  list  of  all  the  prime  numbers  between  2  and   n
Read  'n'  value
call  prime_numbers()  function  
print  the  list
print  number  of  prime  numbers
'''
'''
def prime_numbers(n):
	primes = []
	for num in range(2, n+1):
		is_prime = True 
		
		for i in range(2, num):
			if num % i == 0 :
				is_prime = False
				break

		if is_prime:
			primes.append(num)
	return primes
	
n = int(input('Enter any number : '))
result = prime_numbers(n)

print('Prime Numbers : ',(result))
print('Count : ',len(result))
'''