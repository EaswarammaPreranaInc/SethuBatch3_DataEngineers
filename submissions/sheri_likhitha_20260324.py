# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(1)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(10,20)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(20,30,40)




from lists import prime   # importing the given prime() function

def prime_numbers(n):
    primes = []
    for i in range(2, n + 1):
        if prime(i):   # use the existing function
            primes.append(i)
    return primes

# Read input
n = int(input("Enter n value: "))

# Call function
result=prime_numbers(n)

# Print results
print("Prime numbers:", result)
print("Number of prime numbers:", len(result))