
# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
def  f2(x):
	print('Single  argument  function  : ' , x)
def  f3(x , y):
	print('Two  argument  function : ' , x , y)
def  f4(x , y , z):
	print('Three  argument  function : ' , x , y , z)


f1()                # No-argument  function
f2(10)              # Single  argument  function  :  10
f3(10 , 20)         # Two  argument  function :  10 20
f4(10 , 20 , 30)    # Three  argument  function :  10 20 30

# change the functions names. it will run without any errors. 
# python doesn't allow overloading



'''
Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
																		    
Number  of   prime  numbers : 4
'''

def prime_numbers(n):
    a = []
    count = 0

    for i in range(2,n+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            a.append(i)
    return a

n = int(input('Enter an integer : '))
print(prime_numbers(n))




   




























   