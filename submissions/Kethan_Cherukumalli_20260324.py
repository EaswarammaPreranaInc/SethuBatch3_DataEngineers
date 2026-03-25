
# Modify following program such that every function should be executed
'''
def f1():
    print('No-argument function')
def f1(x):
    print('Single argument function: ', x)
def f1(x , y):
    print('Two argument function: ', x , y)
def f1(x , y , z):
    print('Three argument function: ', x , y , z)
'''
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
  
-------------------------------------------------------------------

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