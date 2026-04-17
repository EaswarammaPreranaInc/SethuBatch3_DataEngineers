# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)

def f1(*args):
    count = len(args)
    
    if count == 0:
        print('No-argument function')
    elif count == 1:
        print('Single argument function:', args[0])
    elif count == 2:
        print('Two argument function:', args[0], args[1])
    elif count == 3:
        print('Three argument function:', args[0], args[1], args[2])

f1()
f1(10)
f1(10, 20)
f1(10, 20, 30)


'''
Write a program to generate list of all prime numbers between 2 and n, also print how many prime numbers are existing

What are the outputs if input is 10? --> Prime numbers: [2 , 3 , 5 , 7]
                                         Number of prime numbers: 4
'''

def prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

val = int(input("Enter the value of n: "))

result = prime_numbers(val)

print(f"Prime numbers: {result}")
print(f"Number of prime numbers: {len(result)}")









