Name-Dhruva Gupta
Roll Number-D238

1)
def prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
def prime_numbers(n):
    res = []
    for i in range(2, n + 1):
        if prime(i):
            res.append(i)
    return res
n = int(input("Enter n: "))
result = prime_numbers(n)
print("Prime numbers : ", result)
print("Number of prime numbers : ", len(result))