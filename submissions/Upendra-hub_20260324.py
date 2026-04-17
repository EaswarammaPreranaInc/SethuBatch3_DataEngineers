

def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(60)  
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(40 , 50)  
def  f1(x , y , z):
     print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_numbers(n):
    primes = []
    for i in range(2, n + 1):
        if prime(i):
            primes.append(i)
    return primes

n = int(input("Enter n value: "))
plist = prime_numbers(n)
print("Prime numbers :", plist)
print("Number of prime numbers :", len(plist))
