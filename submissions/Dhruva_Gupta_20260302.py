Name-Dhruva Gupta
Roll Number-D238

1)
ch=65
for i in range(0,26):
    print(chr(ch),end=" ")
    ch=ch+1
print()
ch=97
for i in range(0,26):
    print(chr(ch),end=" ")
    ch=ch+1


2)
n=int(input("Enter the number of terms you need: "))
a=0
b=1
print(a,end=" ")
print(b,end=" ")
c=a+b
#print(c)
for i in range(0,n-2):
    print(c,end=" ")
    a=b
    b=c
    c=a+b


3)
a=[10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
b=15
cnt=0
for i in range(0,len(a)):
    if(b==a[i]):
        print(f"15 is found at index {i}")
        cnt=cnt+1
print(f"15 is found at {cnt}")

4)
sum = 0
count = 0
try:
    while True:
        value = input("Enter a value: ")
        num = eval(value)  
        sum += num
        count += 1

except EOFError:
    pass   
if count != 0:
    average = sum / count
    print("Average =", average)
else:
    print("No inputs were given.”)

5)
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
print('Outside  loop’)

Output:-
1
Sec 
Hello
2 
Sec 
hello
3
4
Sec
hello 
5
sec
hello
6
7
Sec
Hello
Else suite
outside loop

6)
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
print('Outside loop’)

Output-
1
Sec
Hello
2
Sec
Hello
.
.
.
Else suite
Outside loop

7)
#  Walrus   operator (:=)  demo  program
print(a := 25) #25
print(a = 25) #Error, can’t use assignment in print() statement and execution stops
print(a) #25
print(a := 6 + 7) #13
print(a) #13
print((a := 6) + 7)#13
print(a) 13
print((a = 6) + 7) #Error

8)

# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)
if  c = 0:
	print('Hyd')
else:
	print('Sec')

Output:-
Hyd
Sec: 0
Error

9)
#  del  operator  demo program  (Home  work)
a = 25
print(a)  #25
del   a 
print(a) #Error

10)
# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) #25,25,25
del   a
print(b , c) #25,25
print(a)  #error
del   b
print(c) #25
print(b) #error
del   c
print(c) #error
11)
#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) #25 , 10.8 , 'Hyd'
del   a , b , c 
print(a) #Error
print(b) #Error
print(c) #Error

12)
# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  #List printed 
del  a[2]  
print(a) #[10,20,18]
del  a
print(a) #Error
print(a[0]) #Error

13)
# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a) #Tuple printed
print(a[0]) #10
del  a[2] #Tuple immutable
del  a 
print(a)  #error
print(a[0]) #Error

