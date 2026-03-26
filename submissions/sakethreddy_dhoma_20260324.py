
#
def f1(*args):
    if len(args) == 0:
        print('No-argument function')
    elif len(args) == 1:
        print('Single argument function:', args[0])
    elif len(args) == 2:
        print('Two argument function:', args[0], args[1])
    elif len(args) == 3:
        print('Three argument function:', args[0], args[1], args[2])

# Test the function
f1()
f1(5)
f1(5, 10)
f1(5, 10, 15)


#Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
#also  print  how  many  prime  numbers  are  existing

def  prime_numbers(n):
	return  list  of  all  the  prime  numbers  between  2  and   n
Read  'n'  value
call  prime_numbers()  function  
print  the  list
print  number  of  prime  numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(n):
    return [num for num in range(2, n + 1) if is_prime(num)]

n = int(input("Enter a number: "))
primes = prime_numbers(n)
print("Prime numbers:", primes)
print("Number of prime numbers:", len(primes))