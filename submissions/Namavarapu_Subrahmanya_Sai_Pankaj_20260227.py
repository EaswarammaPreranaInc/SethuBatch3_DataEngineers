''' 
Write  a  program  to  determine  bill  amount  and  input  is  units
Units                                                      Cost
------------------------------------------------------------
First  100  units(0 - 99)                    Rs. 3.00 / unit
Next  100  units(100 - 199)                 Rs. 3.50 / unit
Next  200  units(200 - 399)                 Rs. 4.00 / unit
Next  300  units(400 - 699)                 Rs. 4.50 / unit
Above  700  units(units >= 700)             Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ?
--->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + 500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''

units = int(input('Enter  units :   '))   #   175

match  units // 100:

    case  0:   #   units  between  0  and  99
        cost = units * 3.00

    case 1:   # 100–199
        cost = 100 * 3.00 + (units - 100) * 3.50

    case 2:   # 200–299
        cost = (
            100 * 3.00 +
            100 * 3.50 +
            (units - 200) * 4.00
        )

    case 3:   # 300–399
        cost = (
            100 * 3.00 +
            100 * 3.50 +
            100 * 4.00 +
            (units - 300) * 4.50
        )

    case _ :   # 400 and above
        cost = (
            100 * 3.00 +
            100 * 3.50 +
            100 * 4.00 +
            100 * 4.50 +
            (units - 400) * 5.00
        )

print("Total bill =", cost)



x = int(input('Enter value of x :'))

a = 0
b = 1
c = a + b

print('Fibanocci series')
print(f'{a}')
print(f'{b}')

while c < x:
    print(f'{c}')
    a = b
    b = c
    c = a + b

print('This program is over')



a = eval(input('Enter any sequence with quotes on : '))
i = 0

while i <= len(a):
    print(a[i])
    i += 1
    if i == len(a):
        break



for  x  in  {10 : 20 , 30 : 40 , 50 : 60}.keys():
    print(x)

print()

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}.values():
    print(x)

print()

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}.items():
    print(x)

print()

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
    print(x)



a = {10 : 20 , 30 : 40 , 50 : 60}

for  x , y  in   a.items():
    print(x , y , sep = '...')



for  x  in   123:
    print(x)



for  x   in   ():
    print(x)

for  x   in  []:
    print(x)

for  x   in   {}:
    print(x)

for  x   in   set():
    print(x)

for  x   in   '':
    print(x)

for  x  in  range(10 , 10):
    print(x)



for  i  in  range(1 , 4):
    for  j  in  range(1 , 5):
        print(i ,  j)
    print('Hello')

print('Bye')



a = eval(input('Enter a Sequence :'))

b = []

for x in a:
    print(x, end = ' ')
    b.append(x)
    print(len(b)-1)



for i in range(len(a)):
    print(i)
    print(a[i])



for x in enumerate(a):
    print(x)



a = eval(input('Enter a Sequence : '))

for i in range(-1,-len(a)-1, -1):
    print(a[i])

for x in reversed(a):
    print(x)



a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []

for x,y in zip(a,b):
    c.append(x+y)
    print('3rd  list : ' , c)



a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']

print('Indexed for loop')

for i in range(len(a)):
    if i >=2 and i < 5:
        print(a[i])



for x in a:
    if 2 <= a.index(x) <= 4:
        print(x)



a = [10 , 20 , 15 , 18]

for  i  in  range(len(a)):
    a[i] +=  1

print('a :  ' , a)



b = [10 , 20 , 15 , 18]

for  x  in   b:
    x += 1
    print(x)

print('b :  ' ,  b)



a = eval(input('Enter number of lines :  '))

for i in range(a*2):

    if i%2 == 0:
        continue

    b = ' '*a
    a -=1
    c = '*'*i

    print(f'{b}{c}')



a = eval(input('Enter number of even numbers :  '))

i = 0

while i<=a:
    print(2*i)
    i+=1

print('Bye')



a = eval(input('Enter number of odd numbers :  '))

i = 1

while i<=a:
    print(2*i-1)
    i+=1

print('Bye')



a = eval(input('Enter number of natural numbers :  '))

i = 0

while i<= a:
    print(i)
    i+=1



a = eval(input('Enter number of natural numbers to be reversed :  '))

i = a

while i > 0:
    print(i)
    i-=1

print('Bye')



a = int(input('How many terms would you like to add :  '))

sum = 0

for i in range(1,a+1):
    x = 1.1*i
    sum+=x

print(f'{sum:.1f}')



a = int(input('enter a integer :  '))

sum = 0

for i in range(0,a+1):
    x = 2*i
    sum = sum+x

print('Sum of first 20 even numbers :', sum)



a = int(input('enter a integer :  '))

sum = 0

for i in range(1,a+1):
    x = 2*i-1
    sum = sum+x

print('Sum of first 20 odd numbers :', sum)



a = int(input('enter a integer :  '))

sum = 0

for i in range(1,a+1):
    x = i
    sum = sum+x

print('Sum of first numbers :', sum)



for  i   in   range(1 , 8):

    print(i)

    if  i % 3  == 0:
        continue
    #prints Sec 
# # 1
# # Sec
# # Hello
# # 2
# # Sec
# # Hello
# # 3
# # 4
# # Sec
# # Hello
# # 5
# # Sec
# # Hello
# # 6
# # 7
# # Sec
# # Hello
# # Outside loop

    else:
        print('Sec')

    print('Hello')

print('Outside loop')



if ():
    print('Hyd')
    #continue
    print('Sec')



for  i   in   range(1 , 8):

    print(i)# 1
# # Sec
# # Hello
# # 2
# # Sec
# # Hello
# # 3
# # Outside loop

    if   i % 3 == 0:
        break

    else:
        print('Sec')

    print('Hello')

print('Outside loop')



if(10 , 20 , 30):
    print('Hyd')
    #break
    print('Sec')