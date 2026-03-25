# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(x=1)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(1,2)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(1,2,3)

'''
Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
																		    Number  of   prime  numbers : 4

def  prime_numbers(n):
	return  list  of  all  the  prime  numbers  between  2  and   n
Read  'n'  value
call  prime_numbers()  function  
print  the  list
print  number  of  prime  numbers

'''
def prime(a):
    s=[]
    for i in range(2,a+1):
        for j in range(2,i-1):
            if i%j==0:
                break
        else:
              s.append(i)
    return (s)
a=int(input("Enter a number:"))
if a<2:
    print("Invalid Input")
b=prime(a)
print("Prime numbers till",a,"=",b)
print("Number of prime number =",len(b))
