
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(20)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(20, 30)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10,20,30)

	
from Ajay_Sougani_20260323 import prime

def  prime_numbers(n):
	primes=[]
	for i in range(2, n+1):
		if prime(i):
			primes.append(i)
	
	print("Number of prime numbers: ", len(primes))
	return primes #list  of  all  the  prime  numbers  between  2  and   n
#Read  'n'  value
#call  prime_numbers()  function  
#print  the  list
#print  number  of  prime  numbers
n = int(input("Enter the number: "))
res = prime_numbers(n)
print(F'list  of  all  the  prime  numbers  between  2  and   {n}: {res}')