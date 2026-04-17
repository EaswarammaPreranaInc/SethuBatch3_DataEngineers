units = int(input('Enter units : '))
match units :
    case 0 : # 0 -99
        cost = units * 3.00
    case 1 : # 100 - 199
        cost = 100 * 3.00 + (units - 100) * 3.50
    case 2 : # 200 - 399
        cost = (100 * 3.00 + 100  * 3.50 + (units - 200) * 4.00)
    case 3: # 400 - 699
        cost = (100 * 3.00 + 100  * 3.50 + 200 * 4.00 +(units -300) * 4.50)
    case _: # 700 and above
        cost = (100 * 3.00 + 100  * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00) 
        print ('Bill amount:', cost)
            



x = int(input('Enter value of x :'))
a = 0
b = 1
print("fibonacci series upto", x , ':')
while a  <=10 :
    print(a, end = " ")
    c = a+b
    a = b
    b = c

list = [10,20,15,18]
for l in list:
    print(l)

string = 'Hyd'
for s in string:
    print(s)

    x = [0,1,2,3,4]
for i in x:
    print(i)

x = {10:20,30:40,50:60}.keys()
    for i in x:
    print(x)
   
    x = {10:20,30:40,50:60}.values()
    for i in x:
     print(x)

x = {10:20,30:40,50:60}.items()
for i in x:
    print(x)


    x = {10:20,30:40,50:60}
    for i in x:
    print(x)


a = {10:20,30:40,50:60}
for x,y in a:
 print(x,y ---> Error 

a = {10:20,30:40,50:60}:
for x,y in 
 print(x,y, sep='...') ---> Error  

 # Identify  error  (Home  work)
for  x  in   123:
        print(x)--> condition values are 123

        # Find  outputs  (Home  work)
for  x   in   ():
        print(x)---> Error empty tuple
for  x   in  []:
        print(x)---> Error empty list
for  x   in   {}:
        print(x)
for  x   in   set():---> Error empty set
        print(x)
for  x   in   '':---> Error empty string
        print(x)
for  x  in  range(10 , 10):
	print(x)---> Error index value begin and end are same
for  x  in   range():
	print(x)---> Error range
for  x  in   (25):
	print(x)---> 25

    r = range(25 , 10.8,'Hyd', True)
for i in range(len(a)):
  print(a[i])  

  x = [10,20,15,18]
y = [30,40,35,12,100,200,300]
x = eval(input('Enter  1st  list  :  '))
y = eval(input('Enter  2nd  list  :  '))
z = x+y
print('3rd listL:' , z)

x = [25,10.8,'Hyd', True , 3+4j]
print[2:4:1]

a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)---> (10 , 20 , 15 , 18 : 11 , 21 , 16 , 19)
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)--> 11 , 21 , 15 , 18

n = int(input("Enter number of lines: "))

for i in range(n):
    spaces = n - i - 1
    stars = 2 * i + 1
    print(" " * spaces + "*" * stars)

    i = 1
while i<= 20:
 print(2 * i)
 i = i + 1

 i = 1
while i<= 20:
  print(2 * i-1)
  i = i +1

i = 1
while i<= n :
  print(i)
  i = i + 1

  # Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')---> 'Hello'
                          'Outside loop'


# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec')---> error empty tuple

    # Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')---> 'Outside loop'

# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')---> list have values Error