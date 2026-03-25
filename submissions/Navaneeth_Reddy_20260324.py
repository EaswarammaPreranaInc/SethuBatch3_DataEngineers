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
# '''
# Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
# also  print  how  many  prime  numbers  are  existing

# Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite

# What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
# 																		    Number  of   prime  numbers : 4
# def  prime_numbers(n):
# 	return  list  of  all  the  prime  numbers  between  2  and   n
# Read  'n'  value
# call  prime_numbers()  function  
# print  the  list
# print  number  of  prime  numbers
# '''

def Prime(n):
    
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True

def prime_numbers(n):
    b=[]
    for i in range(2,n+1):
        if Prime(i):
            b.append(i)
    return b

inp = int(input("Enter the value :" ))
if inp < 0:
    print("Only Postive Numbers")
else:
	if inp == 1:
		print("It is neither prime nor composite")
	elif inp >= 2:
		print(prime_numbers(inp))
  
'''
Output :
Enter the value :89
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
'''
