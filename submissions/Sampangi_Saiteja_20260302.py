'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
""
#OUt put

for i in range(65,90):
	chr(i+)=1
	print(i end="")



for i in range(64,90):
    i+=1
    print(chr(i), end=" ")
print("\n")


for i in range(96,122):
    i+=1
    print(chr(i),  end=" ")
print("\n")



# Program to print first n terms of Fibonacci series

n = int(input("Enter number of terms: "))

# First two terms
a, b = 0, 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b




    
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

#out put
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

Sec
Hello
else  suite
Outside  loop


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


#Output
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




# Program to search for an element in the list and count occurrences

numbers = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]
x = int(input("Enter element to search: "))

count = 0   # to count occurrences

for i in range(len(numbers)):
    if numbers[i] == x:
        print(x, "is found at index", i)
        count += 1

if count > 0:
    print(x, "is found", count, "times")
else:
    print("Not found")


 #  Walrus   operator (:=)  demo  program
print(a := 25)
print(a = 25)
print(a)#25
print(a := 6 + 7)#13
print(a)#13
print((a := 6) + 7)#
print(a)#25
print((a = 6) + 7)#13

 # Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')#Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd')#hyd
else:
	print('Sec : ' , b)
if  c = 0:
	print('Hyd')
else:
	print('Sec')#sec

#  del  operator  demo program  (Home  work)
a = 25
print(a)#25  
del   a 
print(a)#Nohing 
# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)#25 25 25
del   a
print(b , c)#25 25
print(a)  #nothing
del   b
print(c)#25
print(b)#nothing
del   c
print(c)#nothing

#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)#25 10.8 Hyd
del   a , b , c
print(a) #25
print(b) #10.8
print(c)#Hyd


# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a) #10 20 15 18 
del  a[2]  
print(a)#nothing 
del  a
print(a)#nothing 
print(a[0])#nothing


# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)#10 20 15 18  
print(a[0])#10 
del  a[2] 
del  a 
print(a) #nothing  
print(a[0])#nothing 

