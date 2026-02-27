'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,   1 ,  2 ,  3 ,  5 , 8 , 13

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  ---> (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop
'''
def fib():
    n=int(input("enter value of x"))
    a=0
    b=1
    print("fibnocci series :")
    
    while(a<=n):
       
        print(a)
        a,b=b,a+b
#fib()
        
'''a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)
'''
    
a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)):
    print(f'index : {i}  value :  {a[i]}')
for i in a:
    print(f'value = {i}')
for i in range(-1,-len(a)-1,-1):
    print(f'value={a[i]}')
    '''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  --->  [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method

a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)'''
def addlist():
    a = eval(input('Enter  1st  list  :  '))
    b = eval(input('Enter  2nd  list  :  '))
    c = []
    for i in range(min(len(a),len(b))):
        c.append(a[i]+b[i]);
    print(c)

#addlist()
b = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
count=0;
for i in b:
    if 2<=count<=4:
        print(i)
    count+=1

a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)           # a :[11 , 21 , 16 , 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)           # b :[10 , 20 , 15 , 18]


def patteren():
     a=int(input('number of rows'))
     for i in range(1,a+1):
          for j in range(a-i):
               print(" ",end="")
          for k in range(2*i-1):
                 print('*',end='')
          print()
         
#patteren()



'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers 

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
def evennumber():
     a =int(input("Enter of even numbers you want"))
     count=1
     while(count<=a):
          print(2*count)
          count+=1
#evennumber()

def oddnumber():
     a =int(input("Enter  numbers of odd numbers you want"))
     count=1
     while(count<=a):
          print(2*count-1)
          count+=1
#oddnumber()

def naturalnumber():
     a =int(input("Enter of upto numbers you want"))
     count=1
     while(count<=a):
          print(count)
          count+=1
#naturalnumber()

def reversenumber():
     a =int(input("Enter of upto numbers you want"))
     count=a
     while(count>=1):
          print(count)
          count-=1
#reversenumber()

def addnumber():
     a =int(input("Enter of upto numbers you want"))
     count=1
     sum=0
     while(count<=a):
          sum+=1.1*count
          count+=1
     print(sum)
#addnumber()
def EvenAddnumber():
     a =int(input("Enter of sum of even numbers you want :"))
     count=1
     sum=0
     while(count<=a):
          sum+=count*2
          count+=1
     print(sum)
#EvenAddnumber()
def oddAddnumber():
     a =int(input("Enter of sum of odd numbers you want :"))
     count=1
     sum=0
     while(count<=a):
          sum+=count*2-1
          count+=1
     print(sum)
#oddAddnumber()



def naturaladdnumber():
     a =int(input("Enter of upto numbers you want"))
     count=1
     sum=0
     while(count<=a):
           sum+=count
     print(count)  
#naturaladdnumber()
