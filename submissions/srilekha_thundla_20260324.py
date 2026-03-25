# Modify  following  program  such  that  every  function  should  be  executed
# def  f1():
# 	print('No-argument  function')
# f1()
# def  f1(x):
# 	print('Single  argument  function  : ' , x)
# f1(x = 1)
# def  f1(x , y):
# 	print('Two  argument  function : ' , x , y)
# f1(x = 1,y = 0)
# def  f1(x , y , z):
# 	print('Three  argument  function : ' , x , y , z)
# f1(z=3,x=1,y=2)

'''
Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
																		    Number  of   prime  numbers : 4
'''
n = int(input('Enter any number : '))


x = 2
divisor = 2
prime = []
is_prime = True

while x <= n:
    if divisor <= x // 2:
        if x % divisor == 0:
            is_prime = False
        divisor += 1
    else:
        if is_prime:
            prime.append(x)
        x += 1
        divisor = 2
        is_prime = True

print("Prime numbers :", prime)
print("Number of prime numbers :", len(prime))

    
 
    	
	
				
