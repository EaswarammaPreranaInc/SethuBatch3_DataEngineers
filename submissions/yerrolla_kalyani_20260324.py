
# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(10)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(10,20)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10,20,30)
'''
Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a.py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime numbers : [2 , 3 , 5 , 7]
																		    Number  of   prime  numbers : 4
'''
# def  prime_numbers(n):
	
# 	return  list  of  all  the  prime  numbers  between  2  and   n
# Read  'n'  value
# call  prime_numbers()  function  
# print  the  list
# print  number  of  prime  numbers

from prime_number import prime
c=[]
n=int(input("Enter the value of n:"))
for  i in range(2,n):
    if prime(i):
       c.append(i)
print(c)
len(c)
print(len(c))




# '''
# Write  a  function  to  print  number  in  words

# Let  input  be  123456789
# What  is  the  output ?  --->  Tweleve  crores  thirty  four  lakhs  fifty  six  thousand  seven  hundred  eighty  nine

# 1) a = ["" , "One" , "Two" , "Three" , "Four" , "Five" , "Six" , "Seven" , "Eight" , "Nine" , "Ten" ,   "Eleven" , "Twelve" ,
#            "Thirteen" , "Fourteen" , "Fifteen" , "Sixteen" , "Seventeen" ,  "Eightteen" , "Nineteen"]

# 2) b = [""  , "" , "Twenty" , "Thirty" , "Forty" , "Fifty" , "Sixty" , "Seventy" , "Eighty" , "Ninety"]
#             0     1          2              3            4             5           6              7               8               9

# 3) How  to  print  92  in  words ?  --->  b[92 // 10]  and  a[92 % 10]  = b[9]  and  a[2]
#     How  to  print  50  in  words ?  --->   b[50 // 10]  and  a[50 % 10]  = b[5]  and  a[0]

# 4) How  to  print  14  in  words ?  --->  a[14]
#     How  to  print  4  in  words ?  --->  a[4]

# 5) How  to  obtain  crores  part  from  123456789 ?  --->  123456789 // 10000000 = 12
#     How  to  obtain  lakhs  part  from  123456789 ?  --->  123456789 // 100000 % 100 = 1234 % 100 = 34
#     How  to  obtain  thousands  part  from  123456789 ?  --->  123456789 // 1000 % 100 = 123456 % 100 = 56
#     How  to  obtain  hundreds  part  from  123456789 ?  ---> 123456789 // 100 % 10 = 1234567 % 10 = 7
#     How  to  obtain  last  two  digits  of  the  number ?  ---> 123456789 % 100 = 89
# '''
# def  words(n , units):
# 	 a = ["" , "One" , "Two" , "Three" , "Four" , "Five" , "Six" , "Seven" , "Eight" , "Nine" , "Ten" , "Eleven" , "Twelve" , 
# 	        "Thirteen" , "Fourteen" , "Fifteen" , "Sixteen" , "Seventeen" , "Eightteen" , "Nineteen"]
# 	 b = [""  , "" , "Twenty" , "Thirty" , "Forty" , "Fifty" , "Sixty" , "Seventy" , "Eighty" , "Ninety"]
#             0     1          2              3            4             5            6              7               8              9
# 	if n<20:
# 	    b[n//10]#Write  if  statement  to  print  two  digit  number  in  words
# 	a[n//10]#Write  if  statement  to  print  units
# '''
# 1) words(92 , "Crores")  --->  Ninety  two  crores

# 2) words(50 ,  "Lakhs")  --->  Fifty  Lakhs

# 3) words(14 , "Thousand")  --->  Fourteen  Thousand

# 4) words(7 , "Hundred")  ---> Seven  Hundred

# 5) words(0 , "Crores")   --->  Nothing  becoz  1st  argument  is  0
# '''
# n = int(input('Enter any number (max : 999999999)  : '))
# if  n == 0:
# 	printf('Zero')
# else:
#         How  to  obtain  crores  part  from  the  number  and  call  words()  function
#         How  to  obtain  lakhs  part  from  the  number  and  call  words()  function
#         How  to  obtain  thousands  part  from  the  number  and  call  words()  function
#         How  to  obtain  hundreds  part  from  the  number  and  call  words()  function
#         How  to  obtain  last  two  digits  of  the  number  and  call  words()  function
# 		printf("\n");


def words(n,units):
    a=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",
       "Eleven","Tweleve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    b=["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    if n==0:
        return
    if n<20:
        print(a[n],end=" ")
    else:
        print(b[n//10],a[n%10],end=" ")
    print(units,end=" ")
#function definition end
n=int(input("Enter any number: "))
if n==0:
    print("Zero")
else:
    words(n//10000000, "crores")
    words((n//100000)%100, "lakhs")
    words((n//1000)%100, "Thousand")
    words((n//100)%10, "Hundred")
    words((n%100), "")