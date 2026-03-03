#1
'''
Write a program to print upper and lower case alphabets

Hint:
chr(65) = 'A'
chr(90) = 'Z'
chr(97) = 'a'
chr(122) = 'z'
'''
for i in range(65, 91):
    print(chr(i), end=" ")
print()
for i in range(97, 123):
    print(chr(i), end=" ")


#2
'''
Write a program to print first 'n' terms of fibonacci series

Let input be 6
What is the output? ---> First 6 terms i.e. 0 , 1 , 1 , 2 , 3 , 5
'''
n = int(input("Enter the number of terms: "))

a = 0
b = 1

print(f"First {n} terms:", end=" ")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


#3
'''
Write a program to search for 'x' in fibonacci series

1)  Let input be 10
    What is the output? ---> Not found

2)  Let input be 21
    What is the output? ---> Found

3) Do not generate fibonacci series
'''
x = int(input("Enter value to be searched: "))

a = 0
b = 1

while a < x:
    temp = a + b
    a = b
    b = temp

if a == x:
    print("Found")
else:
    print("Not Found")


#4
# Find outputs (Homework)
for i in range(1 , 8):
    print(i)
    if i % 3 == 0:
        continue
    else:
        print('Sec')
    print('Hello')
else:
    print('else suite')
# End of the loop
print('Outside loop')

#Output:
'''
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
Outside loop'''


#5
# Find outputs (Homework)
for  i  in  range(1 , 8):
    print(i)
    if  i == 8:
        break
    else:
        print('Sec')
    print('Hello')
else:
    print('else  suite')
# End of the loop
print('Outside loop')

#Output:
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
else suite
Outside loop'''


#6
'''
Write a program to search for an element in the list without using in operator and print 'Found' or 'Not Found' message (Assume that there are no duplicates)

Let  list  be   [10 , 20 , 15 , 12 , 18]
1) What is the output if 15 is seacrhed? ---> Found at index 2

2) What is the output if 19 is seacrhed?  ---> Not found

3) What action to be made when 'x' does not match with the current element of list? ---> Compare 'x' with next element of list

4) What action to be made when 'x' matches with list element? ---> Print found message along with index and do not search for 'x' in rest of the list

5) What action to be made when 'x' does not match with all the elements of list? ---> Print not found message

6) Hint: Use for loop
'''
l = eval(input("Enter any list: "))

x = int(input("Enter the element to be searched : "))

found = False

for i in range(len(l)):
    
    if l[i] == x:
        print("Found at index : ", i)
        found = True
        break

if not found:
    print("Not Found")


#7
'''
Write a program to search for an element in the list and print index of each element and also number of times it is found

List: [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search for 15

What are the outputs ? ---> 15 is found at index 2
                            15 is found at index 5
                            15 is found at index 8
                            15 is found 3 times
'''
l = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]

x = int(input("Search for: "))

count = 0

for i in range(len(l)):
    
    if l[i] == x:
        print(f"{x} is found at index {i}")
        count = count + 1

if count > 0:
    print(f"{x} is found {count} times")
else:
    print("Not Found")


#8
#Walrus operator (:=) demo program
print(a := 25) #25
print(a = 25) #Error as assignment operator alone can't be use inside a print() function
print(a) #25
print(a := 6 + 7) #13
print(a) #13
print((a := 6) + 7) #13
print(a) #6
print((a = 6) + 7) #Error as assignment operator can't be use inside a print() function



#9
#Find outputs (Homework)
a = 0
if a == 0:
    print('Hyd') #Hyd
else:
    print('Sec')
if b := 0:
    print('Hyd') 
else:
    print('Sec: ',b) #Sec: 0
if c = 0: #Error as assignment operator i.e. '=' can't be used to compare or check some specific condition instead use comparision operator i.e. '=='
    print('Hyd') 
else:
    print('Sec')



#10
'''
(Homework)
Write a program to determine average of inputs which are terminated with ctrl + z
(without walrus operator)

Let inputs be 25 , 10.8 , True , ctrl + z

sum = 0 + 25 + 10.8 + True 
ctr = 0 + 1 + 1 + 1

1) What is ctrl + z ? --->  End of inputs i.e. No more inputs

2) What does input() function do when input is ctrl + z ? --->  Raises EOFError

3) How is end of inputs denoted in unix? --->  ctrl + d
'''
total = 0
count = 0

print("Enter your values (Press Ctrl+Z then Enter to finish):")

while True:
    try:
        s = input()
        
        val = eval(s)
        
        total = total + val
        count = count + 1
        
    except EOFError:
        break

if count > 0:
    avg = total / count
    print("Sum:", total)
    print("Count:", count)
    print("Average:", avg)
else:
    print("No values were entered.")



#11
# del operator demo program (Homework)
a = 25
print(a) #25
del a 
print(a) #Error as 'a' is not defined earlier i.e. both reference 'a' and object '25' are deleted upon execution of 'del a' statement



#12
# Find outputs (Homework)
a = b = c = 25
print(a , b , c) #25<space>25<space>25
del a
print(b , c) #25<space>25
print(a) #Error as 'a' is not defined earlier i.e. reference 'a' is deleted upon execution of 'del a' statement
del b
print(c) #25
print(b) #Error as 'b' is not defined earlier i.e. reference 'b' is deleted upon execution of 'del b' statement
del c
print(c) #Error as 'c' is not defined earlier i.e. both reference 'c' and object '25' are deleted upon execution of 'del c' statement



#13
# Can multiple objects be deleted with same del operator?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) #25<space>10.8<space>Hyd
del a , b , c
print(a) #Error as 'a' is not defined earlier i.e. reference 'a' and object '25' are deleted upon execution of 'del a, b, c' statement
print(b) #Error as 'b' is not defined earlier i.e. reference 'b' and object '10.8' are deleted upon execution of 'del a, b, c' statement
print(c) #Error as 'c' is not defined earlier i.e. reference 'c' and object ''Hyd'' are deleted upon execution of 'del a, b, c' statement



#14
# Find outputs (Homework)
a = [10 , 20 , 15 , 18]
print(a) #[10 , 20 , 15 , 18]
del a[2]  
print(a) #[10 , 20 , 18]
del a
print(a) #Error as 'a' is not defined earlier i.e. reference 'a' and object '[10 , 20 , 15 , 18]' are deleted upon execution of 'del a' statement
print(a[0]) #Error as 'a' is not defined earlier i.e. reference 'a' and object '[10 , 20 , 15 , 18]' are deleted upon execution of 'del a' statement



#15
# Find outputs (Homework)
a = (10 , 20 , 15 , 18)
print(a) #(10 , 20 , 15 , 18)
print(a[0]) #10
del a[2] #Error as a tuple is an immutable object, which doesn't support item deletion
del a 
print(a) #Error as 'a' is not defined earlier i.e. reference 'a' and object '(10 , 20 , 15 , 18)' are deleted upon execution of 'del a' statement 
print(a[0]) #Error as 'a' is not defined earlier i.e. reference 'a' and object '(10 , 20 , 15 , 18)' are deleted upon execution of 'del a' statement 