Write  a  program  to  print  fibonacci  series  upto   x

n=int(input('Enter value of x : '))
a=0
b=1
while(a<=n):
    print(a)
    c=a+b
    a=b
    b=c 

output:

Enter value of x : 10
0
1
1
2
3
5
8

Enter value of x : 1
0
1
1

Enter value of x : 0
0


# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop

for x in list:
   Print(x)

How  to  print  each  character  of   string  'Hyd'  with  for  loop

for x in ‘Hyd’:
    print(x)
How  to  print  each  element  of   range(5)  with  for  loop

for i range(5):
    print(i)


# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)   # 10
                     30
                     50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)   # 20 
                     40
                     60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)   # (10,20) 
                     (30,40)
                     (50,60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)  # 10
                    30
                    50


# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')  # 10...20
                                      30...40
                                      50...60
for  x ,  y  in   a:
	print(x , y) # error
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') # error

# Identify  error  (Home  work)
for  x  in   123: # error it cannot be non sequence 
        print(x)


# Find  outputs  (Home  work)
for  x   in   ():
        print(x) # ()
for  x   in  []:
        print(x) # []
for  x   in   {}:
        print(x) # {}
for  x   in   set():
        print(x) # set()
for  x   in   '':
        print(x)  # ''
for  x  in  range(10 , 10):
	print(x) # empty
for  x  in   range():
	print(x) # error atleast one arg should be there
for  x  in   (25):
	print(x) # error we cannot iterate non-sequence

#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')

Output:
1 1
1 2
1 3
1 4
Hello
2 1
2 2
2 3
2 4
Hello
3 1
3 2
3 3
3 4
Hello
Bye

# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
for i in range(len(a)):
    print(a[i],i)
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
for x in a:
    print(x)
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
for i in range(len(a)):
    print(a[i], i)


#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
for i in range(len(a)-1,-1,-1):
    print(a[i])
How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop
for i in range(len(a)-1,-1,-1):
    print(a[i])
How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)



#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)   # [11,21,16,19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)   # [11,21,16,19]


a=eval(input('Enter 1st list : '))
b=eval(input('Enter 2nd list : '))
c=[]
for i in range(min(len(a),len(b))):
        c.append(a[i]+b[i])
print(c)


a=eval(input('Enter 1st list : '))
b=eval(input('Enter 2nd list : '))
c=[]
i=0
for x in a:
    if i<len(b):
        c.append(x+b[i])
    i=i+1
print(c)


output:

Enter 1st list : [10 , 20 , 15 , 18]
Enter 2nd list : [30 , 40 , 35 , 12 , 100 , 200 , 300]
[40, 60, 50, 30]


#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
for i in range(2,5):
    print(a[i])
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop
for i in range(2,5):
    print(a[i])
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice
i=0
for x in a:
    if i>=2 and i<=4:
        print(x)
    i=i+1


#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) # [11,21,16,19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1 
print('b :  ' ,  b) # [10,20,15,18]


n=int(input('How many lines? '))
for i in range(1,n):
    print(' '*(n-i)+'*'*(2*i-1))

output:

How many lines? 7
      *
     ***
    *****
   *******
  *********
 ***********


n=int(input())
i=1
print(f'First {n} even numbers')
while(i<=n):
    print(2*i)
    i=i+1


output:
First 20 even numbers
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40




n=int(input())
i=1
print(f'First {n} odd numbers')
while(i<n):
    print(2*i-1)
    i=i+1

output:
First 20 odd numbers
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39



n=int(input('Natural numbers: '))
i=1
while(i<=n):
  print(i)
  i=i+1;

output:
Natural numbers: 5
1
2
3
4
5



n=int(input('Numbers from 10 down to 1 in steps of -1 :'))
i=10
while(i>=1){
   print(i)
   i=i-1
}

output:
Numbers from 10 down to 1 in steps of -1: 10
10
9
8
7
6
5
4
3
2
1



n=int(input('How many terms woud you like to add: '))
sum=0
for i in range(1,n+1):
    sum=sum+(1.1*i)
   
print('sum: ',sum)

output:
How many terms woud you like to add: 5
sum: 16.5


n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+(2*i)
print('sum of first 20 even numbers: ',sum)

output:
sum of first 20 even numbers: 420


n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+(2*i-1)
print('sum of first 20 odd numbers:')

output:
sum of first 20 odd numbers: 400

n=int(input('how many terms would you like to add: '))
sum=0
for i in range(1,n+1):
    sum=sum+i 
print('sum: ',sum)

output:
how many terms would you like to add: 10
sum:55


# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')

output:

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
Outside loop


# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue  # cannot be used in if, it can be only used in loops
	print('Sec')


# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

output:
1
Sec
Hello
2
Sec
Hello
3
Outside loop


# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break   # cannot be used in if, it can be only used in loops
	print('Sec')



Write  a  program  to  determine  bill  amount  and  input  is  units


units = int(input('Enter  units :   '))   #   175
cost=0
match  units // 100:

	case  0:   
		cost = units * 3.00
	case  1:  
		cost =  100 * 3.00 + (units - 100) * 3.50
	case  2:
		cost = 100 * 3.00 + 100 * 3.50 + (units-200)*4.0
	case  3:
		cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.0 +(units-400)*4.50
	case  4:				
		cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.0 + 300*4.5 + (units-700)*5.00 
print('Bill  amount  :  ' , cost)

output:

Enter  units :   175
Bill  amount  :   562.5









