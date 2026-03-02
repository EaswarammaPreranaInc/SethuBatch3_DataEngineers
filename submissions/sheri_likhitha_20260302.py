for i in range(65,91):
 print(chr(i),end=" ")
print()
for i in range(97,123):
    print(chr(i),end=" ")
print()    


a=0
b=1
n=int(input("Enter the number of terms: "))
for i in range(1,n+1):
    print(a)
    c=a+b
    a=b
    b=c




a=0
b=1
x=int(input("Enter a number to search: "))
if x==0:
    found=True
else:
 while b<x:    
    c=a+b
    a=b
    b=c
if b==x:
        print("Found")
else:
        print("Not Found")



# Find  outputs  (Home  work)
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
'''
1
sec
Hello
2
sec
Hello
3
4
sec
Hello
5
sec
Hello
6
sec
Hello
7
sec
Hello
else suite
'''

# Find  outputs  (Home  work)
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
'''
1
se
Hello
2
sec
Hello
3
se
Hello
4
sec
Hello
5
sec
Hello
6
sec
Hello
7
sec
Hello
else suite
Outside loop
'''



n=int(input("Enter the element to search: "))
list=[10,20,15,12,18]
found=False
for i in range(len(list)):
    if list[i]==n:
        print(f"found at index {i}")
        found=True
        break
if not found:
        print("Not found")



n=int(input("Enter the element to search: "))
list=[10,20,15,12,18,15,19,14,15,14]
count=0
for i in range(len(list)):
    if list[i]==n:
        print(f"{n} is found at index {i}")
        count=count+1
print(f"{n} is found {count} times")



#  Walrus   operator (:=)  demo  program
print(a := 25)		#25
print(a = 25)		#error invalid syntax
print(a)		#25
print(a := 6 + 7)	#13
print(a)		#13
print((a := 6) + 7)	#13
print(a)		#6
print((a = 6) + 7)	#error because invalid syntax




# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')		#Hyd
else:
	print('Sec')		
if  b := 0:
	print('Hyd')		
else:
	print('Sec : ' , b)	#sec : 0
if  c = 0:
	print('Hyd')		#error
else:
	print('Sec')



#  del  operator  demo program  (Home  work)
a = 25
print(a)	#25  
del   a 
print(a) 	#error not defined


# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)
del   a
print(b , c)
print(a)  
del   b
print(c)
print(b)
del   c
print(c)


	
#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)     #25 10.8 Hyd
del   a , b , c
print(a)		#error not defined 
print(b)		#error not defined 
print(c)		#error not defined


# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)		#10,20,15,18  
del  a[2]  
print(a)		#10,20,18 
del  a
print(a)		#error not defined 
print(a[0])


# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a) 		#10,20,15,18 
print(a[0])		#10 
del  a[2] 
del  a 
print(a)		#error not defined  
print(a[0])        


n=(input("Enter the list: "))
while True:
    try:
        val=eval(input("> "))
        total_sum+=val
        count+=1
    except EOFError:
        break
if count>0:
    print(f"Average: {total_sum/count}")
else:
    print("No input provided")            
    





