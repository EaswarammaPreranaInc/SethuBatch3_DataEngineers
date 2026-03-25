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
a=[]
def prime(n):
    for i in range(2, n):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count == 2:
            a.append(i)
    return a

n = int(input("Enter n: "))
print(prime(n))
