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
def   prime(n): 
	for i in range(2,(n//2)+1):
		if n%i == 0:
			return False
	return  True 

l=[]
def  prime_numbers(n):
    for i in range(2,n):
        if prime(i):
            l.append(i)		
    return  list  #of  all  the  prime  numbers  between  2  and   n
n = int(input("enter a value:"))    #Read  'n'  value
x = prime_numbers(n)    #call  prime_numbers()  function  
print(l)    #print  the  list
print(len(l))    #print  number  of  prime  numbers