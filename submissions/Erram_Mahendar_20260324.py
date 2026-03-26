# Modify  following  program  such  that  every  function  should  be  executed

def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)


######

x,y,z=10,20,30
f1()
f2(x)
f3(x,y)
f4(x,y,z)

************************

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

#############

def prime(i):
    for j in range(2,(i//2)+1):
        if i%j==0:
            return False
    return(True)
a=int(input())
c=[]
for i in range(2,a):
    if prime(i) == True:
        c.append(i)
print("list of prime nos upto" , a, "is :", c)
print("No of Prime nos:" , len(c))