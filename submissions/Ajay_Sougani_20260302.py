print("UpperCase alphbet Letters: ")
for i in range(65, 91):
    print(chr(i), sep=" ", end=' ');
print();
print("LowerCase Letters: "); 
for i in range(97, 123):
    print(chr(i), sep=" ", end=" ");

# fibonacci series

n = int(input("enter the no. of series to be printed: "));
if n==0:
    print("0");
else:
    a = 0;
    b = 1;
    c = a+b;
    for i  in range(n):
        print(a, sep=" ", end=" ");
        a = b;
        b=c;
        c = a+b;

# finding 'x' in fibonacci series 
n = int(input("enter the no. of series to be printed: "));
x = int(input("enter the x value: "));
if n==0:
    print("0");
else:
    a = 0;
    b = 1;
    c = a+b;
    for i  in range(n):
        if a==x:
            print(x, "found");
            break;
        a = b;
        b=c;
        c = a+b;
    else:
        print("not found")

# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)  # 1, 2, 3, 4, 5, 6, 7
	if   i % 3 == 0:
		continue
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside  loop')
# outputs:
# for iterations 1, 2, 4, 5, 7 output will be :
# 	Sec
#     Hello
#    Outside loop
# for 3,6 will be:
#    Outside loop


# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i) #1, 2, 3, 4, 5, 6, 7
	if  i == 8:
		break;
	else:
		print('Sec') # Sec Sec Sec Sec Sec
	print('Hello') # Hello Hello Hello Hello Hello
else:
	print('else  suite') # else suite
# End  of  the  loop
print('Outside loop') # outside loop

# find x in list
lst = [10, 20, 15, 12, 18]

x = int(input("Enter element to search: "))

for i in range(len(lst)):
    if lst[i] == x:
        print("Found at index", i)
        break
else:
    print("Not found")

# printing count and found or not found

lst = [10, 20, 15, 12, 18]

x = int(input("Enter element to search: "))
count=0;
found=False
for i in range(len(lst)):
    if lst[i] == x:
        print("Found at index", i)
        count+=1
        found = True
if found == False:
    print("not found")


# printing x found count times

lst = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]

x = 15
count = 0

for i in range(len(lst)):
    if lst[i] == x:
        print(x, "is found at index", i)
        count += 1

print(x, "is found", count, "times")



# Walrus operator (:=) demo program

print(a := 25)        # 25
print(a = 25)         # Error
print(a)
print(a := 6 + 7)
print(a)
print((a := 6) + 7)
print(a)
# print((a = 6) + 7 )



# Find outputs (Home work)

a = 0
if a == 0:
    print('Hyd')          # Hyd
else:
    print('Sec')

if b := 0:
    print('Hyd')
else:
    print('Sec : ', b)    # Sec :  0

# if c = 0:                 # Error
#     print('Hyd')
# else:
#     print('Sec')


# Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
#(without  walrus  operator)
sum = 0
ctr = 0

try:
    while True:
        data = input("Enter value: ")
        value = eval(data)   # converts 25, 10.8, True correctly
        sum = sum + value
        ctr = ctr + 1

except EOFError:
    pass   # end of inputs

if ctr > 0:
    avg = sum / ctr
    print("Average =", avg)
else:
    print("No inputs given")


# Program to find average of inputs terminated by Ctrl + Z

total = 0
count = 0

try:
    while True:
        x = eval(input("Enter value: "))
        total = total + x
        count = count + 1
except EOFError:
    pass

if count > 0:
    print("Average =", total / count)
else:
    print("No inputs given")



# del operator demo program

a = 25
print(a)   # 25
del a
print(a)   # Error



# Find outputs (Home work)

a = b = c = 25   # All three variables point to 25
print(a, b, c)   # 25 25 25

del a            # a is deleted
print(b, c)      # 25 25
print(a)         # Error: a is not defined

del b            # b is deleted
print(c)         # 25
print(b)         # Error: b is not defined

del c            # c is deleted
print(c)         # Error: c is not defined




# Can multiple objects be deleted with same del operator?

a, b, c = 25, 10.8, 'Hyd'  
print(a, b, c)        # 25 10.8 Hyd

del a, b, c           # Deletes all three variables

print(a)              # Error: name 'a' is not defined
print(b)              # Error: name 'b' is not defined
print(c)              # Error: name 'c' is not defined



# Find outputs (Home work)

a = [10, 20, 15, 18]  
print(a)             # [10, 20, 15, 18]

del a[2]             # Deletes element at index 2 (15)
print(a)             # [10, 20, 18]

del a                # Deletes the whole list variable
print(a)             # Error: name 'a' is not defined
print(a[0])          # Error: name 'a' is not defined



# Find outputs (Home work)

a = (10, 20, 15, 18)  
print(a)           # (10, 20, 15, 18)
print(a[0])        # 10

del a[2]           # Error: 'tuple' object doesn't support item deletion

del a              # This line will not execute because program already stops at previous error
print(a)           # Error (would happen if previous line succeeded)
print(a[0])        # Error