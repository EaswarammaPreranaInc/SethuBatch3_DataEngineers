# Modify  following  program  such  that  every  function  should  be  executed
def f1(a=None, b=None, c=None):
    if a is None and b is None and c is None:
        print("No-argument function")
    elif b is None and c is None:
        print("Single argument function :", a)
    elif c is None:
        print("Two argument function :", a, b)
    else:
        print("Three argument function :", a, b, c)

# Function calls
f1()
f1(10)
f1(10, 20)
f1(10, 20, 30)
	

def prime_numbers(n):
    primes = []
    
    for num in range(2, n + 1):
        is_prime = True
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(num)
    
    return primes


# Read input
n = int(input("Enter n value: "))

# Function call
result = prime_numbers(n)

# Output
print("Prime numbers:", result)
print("Number of prime numbers:", len(result))