# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function') #No-argument function
def  f1(x):
	print('Single  argument  function  : ' , x) #Single argument function: 10
def  f1(x , y):
	print('Two  argument  function : ' , x , y) #Two argument function: 10 20
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z) #Three argument function: 10 20 30

#Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
#also  print  how  many  prime  numbers  are  existing

# assume this function is already defined in prog3a.py
def prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
def prime_numbers(n):
    primes = []
    for i in range(2, n + 1):
        if prime(i):
            primes.append(i)
    return primes
n = int(input("Enter n: "))
result = prime_numbers(n)
print("Prime numbers:", result)
print("Number of prime numbers:", len(result))