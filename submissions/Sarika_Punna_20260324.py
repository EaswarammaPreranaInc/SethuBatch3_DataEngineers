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
    b=[]
    for i in range(2,n):
        k=0
        for j in range(2,i//2+1):
            if(i%j==0):
                k=1
                break
        if(k==0):
            b.append(i)
    return b
a=int(input("Enter number:"))
if(a<2):
    print("No primes")
else:
    b=prime_numbers(a)
    print(len(b),b)
        
