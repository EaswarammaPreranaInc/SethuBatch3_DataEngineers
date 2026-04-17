# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
def  f2(x):
	print('Single  argument  function  : ' , x)
def  f3(x , y):
	print('Two  argument  function : ' , x , y)
def  f4(x , y , z):
	print('Three  argument  function : ' , x , y , z)

'''
Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
																		                            Number  of   prime  numbers : 4
'''
def  prime_numbers(n):
	return  list  of  all  the  prime  numbers  between  2  and   n
Read  'n'  value
call  prime_numbers()  function  
print  the  list
print  number  of  prime  numbers

def prime(n):
    a=[]
    for i in range(2,n):
        k = 0
        for j in range(2,i//2+1):
            if i % j == 0:
                k = 1 
                break
        if k ==0:
            a.append(i)
    return a

        
n = int(input("Enter n: "))

if(n<2):
    print("No primes")
else:
    a=prime(n)
    print(a)























