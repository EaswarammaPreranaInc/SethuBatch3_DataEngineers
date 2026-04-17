
# Modify  following  program  such  that  every  function  should  be  executed:
def f1(x=None, y=None, z=None):
    count = 0
    if x is not None: count += 1
    if y is not None: count += 1
    if z is not None: count += 1
    if count == 0:
        print("No argument function")
    elif count == 1:
        print("One argument function",f'x : {x}')
    elif count == 2:
        print("Two argument function",f'x : {x}, y : {y}')
    else:
        print("Three argument function",f'x : {x}, y : {y}, z : {z}')
f1(10 , 20 , 30)
f1(40 , 50)  
f1(60)  
f1()
#--------------------------------------------
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
def isPrime(n):
    flag=True
    for i in range(2,(n//2)+1):
        if n%i==0:
            flag=False
    return flag
def generate_prime_numbers(n):
    b=[]
    for i in range(2,n+1):
        if isPrime(i):
            b.append(i)
    return b
a=int(input("enter the value :" ))
if a<0:
    print("invalid input:prime number is only defined for positive integers")
else:
	if a==1:
		print("neither prime nor composite")
	elif a>=2:
		print(generate_prime_numbers(a))


            
    
        
    

