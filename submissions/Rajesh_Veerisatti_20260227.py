# Write  a  program  to  determine  bill  amount  and  input  is  units 
try:

    units = int(input("Enter units : "))
    if units < 0 :
        exit()
    else:
        match units//100:

            case 0:
                cost = units * 3.00

            case 1:
                cost = (100 * 3.00) + ((units - 100) * 3.50)

            case 2:
                cost = (100 * 3.00) +(100 * 3.50) + ((units - 200) * 4.00)
            
            case 3:
                cost = (100 * 3.00) +(100 * 3.50) +(200 * 4.00) + ((units - 400) * 4.50)

            case _:
                cost = (100 * 3.00) +(100 * 3.50) +(200 * 4.00) +(300 * 4.50) +((units - 700) * 5.00)

            
        print("Bill amount :", cost)

except  :

    print('Enter units should be +ve int')




 # Write  a  program  to  print  fibonacci  series  upto   x


try:
    x = int(input('Enter any integer: '))
    a=0
    b=1
    print('fibonacci series')
    while a <= x:
        print(a)
        c=a+b
        a=b
        b=c
except:
    print('Enter should be integer')


#  Write  a  program  to  print  full  pyramid       
try:    
        
    a = int(input("Enter number of lines: "))

    i = 1
    while i <= a:
        spaces = a - i
        stars = 2 * i - 1

        print(" " * spaces + "*" * stars)

        i += 1   

except:
    print('Enter +ve integer')


# Write  a  program  to  print  first  20  even  numbers 

a = 2
b = int(input('Enter no-of elements: '))
if b<1:
    print('Enter only +ve integer')
    exit()
else:
    i = 1
    print(f'first {b} even nembers')
    while i <=b:
        print(2*i)
        i+=1
print('Bye')


# Write  a  program  to  print  first  20  odd  numbers

a = 1
b = int(input('Enter no-of elements: '))
if b<0:
    print('Enter only +ve integer')
    exit()
else:
    i = 1
    print(f'first {b} odd nembers')
    while i <=b:
        print((2*i)-1)
        i+=1
print('Bye')


# Write  a  program  to  print  natural  numbers  1 , 2 , 3 .... n  and   ask  user  to  input  value  of  'n'


b = int(input('Enter no-of elements: '))
if b<0:
    print('Enter only +ve integer')
    exit()
else:
    i=1
    while i<=b:
        
        print(i)
        i+=1
print('Bye')

#  Write  a  program  to  print  10  ,  9  ,   8  ,  ..... 1

b = int(input('Enter no-of elements: '))

i=b
while i<=b:
        
    print(i)
    i-=1
    if i == 0:
        break

print('Bye')


# Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

a = eval(input('Enter 1st list : '))
b = eval(input('Enter 2nd list : '))

c = []

min_len = len(a) if len(a) < len(b) else len(b)

for i in range(min_len):
    c.append(a[i] + b[i])

print( c)