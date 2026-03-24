# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)


#
f1()
f1(x)
f1(x, y)
f1(x, y, z)


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


Program:
a=[]
def prime_num(n):
    global a
    for i in range(2,n+1):
       for j in range(2,i):
            if i%j==0:
               break
       else:
             a.append(i)
       
        
n=int(input("Enter range of prime numbers : "))
prime_num(n)
print(a)
print(len(a))