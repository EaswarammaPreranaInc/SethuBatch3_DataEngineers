#Topic-1
"""
# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1()    
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(10)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(10, 20)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10, 20, 30)
"""

'''
Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
																		    Number  of   prime  numbers : 4
'''

"""
from Yeetheendra_Govardhanam_20260323 import prime

p = []
def  prime_numbers(n):
    for i in range(2,n+1):
        j = prime(i)
        print(prime(i), i)
        if j == True:
            p.append(i)
    return  p
    #list  of  all  the  prime  numbers  between  2  and   n
n = int(input("Enter integer : ")) #Read  'n'  value
m = prime_numbers(n)#call  prime_numbers()  function  

print("Prime numbers :", m)
print("Number  of   prime  numbers : ", len(m))
"""