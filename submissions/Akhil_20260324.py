# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')#
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(10)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(10,20)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10,20,30)
 
 
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