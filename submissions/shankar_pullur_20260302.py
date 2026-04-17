'''Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series'''

def fib():
     try:
        n=int(input("enter postive number"))
        if(n<0):
            print("error print nagative number")
        flag=True
        a=0
        b=1
        while(flag):
            if(a==n):
                print(f"{n} is found")
                flag=False
            elif(a>n):
                print(f'{a} is not found')
                flag=False
            a,b=b,a+b
     except:
       print("give integer value only")





for  i  in  range(1 , 8):
	print(i)
	if   i % 3 == 0:
		continue
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside  loop')
'''1
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
else  suite
Outside  loop'''


for  i  in  range(1 , 8):
	print(i)
	if  i == 8:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside loop')

'''''1
Sec
Hello
2
Sec
Hello
3
sec 
hello
4
Sec
Hello
5
Sec
Hello
6
sec
hello
7
Sec
Hello
outside the loop'''



'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

Let  list  be   [10 , 20 , 15 , 12 , 18]
1) What  is  the  output  if  15  is  seacrhed ?  ---> Found  at  index  2

2) What  is  the  output  if  19  is  seacrhed ?  --->  Not  found

3) What  action  to  be  made  when  'x'  does  not  match  with  the  current  element  of  list ?  --->
																												Compare  'x'  with  next  element  of  list

4) What  action  to  be  made  when  'x'  matches   with  list  element ?  ---> Print  found   message  along  with  index  and
																														do  not  search  for  'x'  in  rest  of  the  list
'''

def search():
	l=eval(input("enter list"))
	n=eval(input("enter number you want to find"))
	for i in range(len(l)):
		if(l[i]==n):
			print(f"element fount at index {i}")
			break
	else:
		print("element not found")
#search()
	
def search2():
	l=eval(input("enter list"))
	n=eval(input("enter number you want to find"))
	count=0
	for i in range(len(l)):
		if(l[i]==n):
			print(f"element {n} fount at index {i}")
			count+=1
	print(f'element {n} is repeated {count}')
#search2()


a = 25
print(a)   # 25  
del   a 
print(a)   # error


a = b = c = 25
print(a , b , c)
del   a
print(b , c)     # 25 25
print(a)         # error
del   b
print(c)         # 25
print(b)         # error
del   c 
print(c)         #error



#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)             # 25 10.8 hyd
del   a , b ,c
print(a)                     # error
print(b)                     # error
print(c)                     #error



a = [10 , 20 , 15 , 18]
print(a)                 # [10 , 20 , 15 , 18]
del  a[2]  
print(a)                  # [10 , 20 ,18]
del  a       
print(a)                   #error
print(a[0])                #error