for CH in range(65,91):
    print(chr(CH), end=' ')
print()
for ch in range(97,123):
    print(chr(ch),end=' ')


'''
output
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
a b c d e f g h i j k l m n o p q r s t u v w x y z
'''

x = int(input("Enter input: "))
a, b = 0, 1
print(f"First {x} terms : ",end='')
for i in range(x):
    print(a, end=" ") 
    a, b = b, a + b   

'''
output
Enter input: 6
First 6 terms : 0 1 1 2 3 5
'''

   
x=int(input("Enter Value to be searched : "))
a,b=0,1
while(a<x):
    a,b=b,a+b
if a==x:
    print("found")
else:
    print("not found")
	
'''
output
Enter Value to be searched : 10
not found
Enter Value to be searched : 21
found
'''

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
output
1
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
Outside  loop
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
Sec
Hello
2
Sec
Hello
3
Sec
Hello
4
Sec
Hello
5
Sec
Hello
6
Sec
Hello
7
Sec
Hello
else  suite
Outside loop
'''

l=eval(input("Enter any list : "))
x=int(input("Enter element to search in list : "))
for i in range(len(l)):
    if x==l[i]:
        print("found at : ",i)
        break
else:
    print("not found")
   
'''
output
Enter any list : [4,12,16,8,67,95]
Enter element to search in list : 16
found at :  2
Enter any list : [8,84,95,4]
Enter element to search in list : 44
not found
'''

l=eval(input("Enter any list : "))
x=int(input("Enter element to search in list : "))
count=0
for i in range(len(l)):
    if x==l[i]:
        count+=1
        print("found at index : ",i)
if count>0:
    print(F'{x} found {count} times')
else:
    print("not found")

'''
output
Enter any list : [4,8,4,8,4,8,4,8]
Enter element to search in list : 4
found at index :  0
found at index :  2
found at index :  4
found at index :  6
4 found 4 times
Enter any list : [4,8,4,8,4,8,4,8]
Enter element to search in list : 16
not found
'''




#  Walrus   operator (:=)  demo  program
print(a := 25)#25
print(a = 25)#error
print(a)#25
print(a := 6 + 7)#13
print(a)#13
print((a := 6) + 7)#13
print(a)#6
print((a = 6) + 7)#error




# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')#Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)#Sec : 0
if  c = 0:
	print('Hyd')#error because c object does not exist
else:
	print('Sec')#error beacuse if give error then else will not run if we remove if statement then else will give error beacuse of already else is there in the program




----
#  del  operator  demo program  (Home  work)
a = 25
print(a)#25  
del   a #object a with 25 deleted 
print(a)#error no object exist




# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)#25 25 25
del   a
print(b , c)#25,25
print(a)#error  
del   b
print(c#25)
print(b)#error
del   c
print(c)#error




#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)#25,10,8,'Hyd'
del   a , b , c
print(a) #error
print(b) #error
print(c)#error




# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  #[10, 20, 15, 18]
del  a[2] 
print(a) #[10, 20, 18]
del  a#error
print(a) #error
print(a[0])#error




a = (10 , 20 , 15 , 18)
print(a)  
print(a[0]) 
#del  a[2] 
del  a 
print(a)  
print(a[0])

'''
output
(10, 20, 15, 18)
10
error
delete tuple 'a'
error
'''

