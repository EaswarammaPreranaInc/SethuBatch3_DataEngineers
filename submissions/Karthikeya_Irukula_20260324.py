# Modify  following  program  such  that  every  function  should  be  executed
# def  f1():
# 	print('No-argument  function')
# def  f1(x):
# 	print('Single  argument  function  : ' , x)
# def  f1(x , y):
# 	print('Two  argument  function : ' , x , y)
# def  f1(x , y , z):
# 	print('Three  argument  function : ' , x , y , z)


'''
def f1(x=None, y=None, z=None):
    if x is None and y is None and z is None:
        print("No-argument function")
    elif y is None and z is None:
        print("Single argument function:", x)
    elif z is None:
        print("Two argument function:", x, y)
    else:
        print("Three argument function:", x, y, z)


f1()
f1(10)
f1(10, 20)
f1(10, 20, 30)'''



#2. Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
# also  print  how  many  prime  numbers  are  existing

# Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite

# What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
# 												 Number  of   prime  numbers : 4
# '''
# def  prime_numbers(n):
# 	return  list  of  all  the  prime  numbers  between  2  and   n
# Read  'n'  value
# call  prime_numbers()  function  
# print  the  list
# print  number  of  prime  numbers
'''

def prime_numbers(n):
    primes = []

    for i in range(2, n + 1):
        is_prime = True

        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
            
        if is_prime:
            primes.append(i)

    return primes

n = int(input("Enter n value: "))
result = prime_numbers(n)
print("Prime numbers :", result)
print("Number of prime numbers :", len(result))'''