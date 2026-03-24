 #1. Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)

def f1(*args):
    if len(args) == 0:
        print('No-argument function')
    elif len(args) == 1:
        print('Single argument function :', args[0])
    elif len(args) == 2:
        print('Two argument function :', args[0], args[1])
    elif len(args) == 3:
        print('Three argument function :', args[0], args[1], args[2])
f1()#No-argument function
f1(40)#Single argument function :40
f1(40,50)#Two argument function :40 50 
f1(40,50,60)#Three argument function :40 50 60

#----------------------------------------------------------------------------------------------------------
[19:28, 24/03/2026] A.Pooja: '''
Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
					            Number  of   prime  numbers : 4
'''
def  prime_numbers(n):
	l = []
	for i in range(2,n+1):
	    count = 0
	    for j in range(2,(i//2)+1):
	        if i%j==0:
	            count+=1
	    if count==0:
	        l.append(i)
	return l
n = int(input("Enter the number : "))
res = prime_numbers(n)
print("Prime numbers : ",res)
print("Number of prime numbers : ",len(res))






