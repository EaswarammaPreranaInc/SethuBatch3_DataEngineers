Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop


a = int(input("Enter a value: "))
b=0
c=1
d=c+b
print("Fibonacci Series:")
print(b)
print(c)
while d <= a:
	print (f'{d}')
	b = c
	c = d
	d = b + c


**************************

How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()


#
lst = eval(input('enter a list:' )
for i in lst:
	 print(i)


How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()

#
lst = input('enter a str:' )          ###check
for i in lst:
	 print(lst(i))

How  to  print  each  element  of   range(5)  with  for  loop
#
n = int(input('enter range:')
for i in range(n):
	print(i)


**************************

for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)
print()  # 10
           30
           50
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)
print() #20
         40
         60
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)
print() #(10, 20)
         (30, 40)
         (50, 60)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)
#          10
           30
           50

**************************

a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')

#
10...20
30...40
50...60

for  x ,  y  in   a:
	print(x , y
#error

for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')

**************************

for  x  in   123:
        print(x)

#erroe int is not iterable

****************************

for  x   in   ():
        print(x)  #prints each element if given
for  x   in  []:
        print(x)  #prints each element in the list if given
for  x   in   {}:
        print(x)  #prints each element in the set if given
for  x   in   set():
        print(x)  #converts the input into set & prints each element in the set if given

for  x   in   '':
        print(x)
for  x  in  range(10 , 10):
	print(x)
for  x  in   range():
	print(x)      #error no range given
for  x  in   (25):
	print(x)      #error int obj is not iterable

****************************



i = 1
while i <= 20:
    print(2 * i)
    i += 1

****************
i = 1
while i <= 20:
    print(2 * i - 1)
    i += 1

***************

n = int(input('Enter n : '))
i = 1
while i <= n:
    print(i)
    i += 1

**************

n = int(input('Enter n : '))
i = 1
while i <= n:
    print(i)
    i += 1

******************


n = int(input('Enter n : '))
sum = 0

for i in range(1, n + 1):
    sum += 1.1 * i

print('Sum =', sum)

*****************

sum = 0

for i in range(1, 21):
    sum += 2 * i

print('Sum =', sum)

******************

sum = 0

for i in range(1, 21):
    sum += 2 * i - 1

print('Sum =', sum)

*******************

n = int(input('Enter n : '))
sum = 0

for i in range(1, n + 1):
    sum += i

print('Sum =', sum)

**************

for i in range(1, 8):
    print(i)
    if i % 3 == 0:
        continue
    else:
        print('Sec')
    print('Hello')
print('Outside loop')




	
