for i in range(65,91):
    print(chr(i), end = '  ' )
for i in range(97,123):
    print(chr(i), end  = '   ')



n = int(input('Enter the number of terms:  '))
a , b = 0, 1 
for i in range(n):
    print(a , end = ' ')
    a , b = b , a + b



import math


def is_perfect_square(num):
    root = int(math.sqrt(num))
    return num == root * root
x = int(input('Enter the number to search:  '))
if is_perfect_square(5 * x * x + 4) or  is_perfect_square(5 * x * x - 4):
    print('Found')
else:
    print('Not found')



L = eval(input("Enter any list:   "))
x = int(input("Enter the element to be searched:   "))
for i in range(len(L)):
    if L[i] == x:
        print(f'Found at index {i}')
        found = True
        break
if not found:
    print('Not found')




lst = [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
x = int(input('Enter the element to search:   '))
count = 0
for i, val in enumerate(lst):
    if val == x:
        print(f'{x} is found at index {i}')
        count += 1
if count > 0:
    print(f'{x} is found {count} times')
else:
    print(f'{x} is not found')




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
#outputs
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
else suite
Outside loop






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
#outputs
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
else suite
Outside loop




#  Walrus   operator (:=)  demo  program
print(a := 25) #25
print(a = 25) #Syntax Error
print(a) #25
print(a := 6 + 7) #13
print(a)#13
print((a := 6) + 7)#13
print(a) #6
print((a = 6) + 7) #Syntax error



# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd') #Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b) #Sec : 0
if  c = 0:
	print('Hyd')
else:
	print('Sec') #Sec





#  del  operator  demo program  (Home  work)
a = 25
print(a) #25  
del   a 
print(a) #Error


# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  #[10 , 20 , 15 , 18]
del  a[2] #Deletes the element at index 2 
print(a) #[10 , 20 , 18]
del  a #It deletes the entire list a
print(a) #a is deleted
print(a[0]) #we can't access it.


# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)#25 25 25
del   a#it deletes the reference a
print(b , c) #25 25
print(a)  #a is deleted
del   b  #it deletes the reference b
print(c) #25
print(b) # b is deleted
del   c #it deletes the reference c
print(c) #c is deleted



#  Can  multiple  objects  be  deleted  with  same  del  operator ? Yes,multiple objects can be deleted with the same del operator, separated by commas.
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) #25 10.8 Hyd
del   a , b , c #a , b , c gets deleted.
print(a)  # a is deleted
print(b)  # b is deleted
print(c)  # c is deleted



# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a) #(10 , 20 , 15 , 18) 
print(a[0]) #(10)
del  a[2] #The element gets deleted at index 2.
del  a  #Entire tuple gets deleted.
print(a)  #Tuple a is deleted.  
print(a[0]) #We can't access.




    
    







