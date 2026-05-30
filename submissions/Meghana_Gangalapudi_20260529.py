'''
Producer-Consumer problem with synchronization
'''

from threading import *
import time


class buffer:
    def __init__(self):
        self.x = None
        self.write = True          # Producer can write initially
        self.cond = Condition()

    def store(self, value):
        self.cond.acquire()

        while self.write == False:
            self.cond.wait()

        # Producer stores value
        self.x = value
        print('Producer produced :', self.x)

        # Producer cannot write again immediately
        self.write = False

        # Notify consumer
        self.cond.notify()

        # Release lock
        self.cond.release()

    def ret(self):
        self.cond.acquire()

        while self.write == True:
            self.cond.wait()

        # Consumer reads value
        print('Consumer consumed :', self.x)

        # Consumer allows producer to write again
        self.write = True

        # Notify producer
        self.cond.notify()

        # Release lock
        self.cond.release()


# Producer thread
def f1():
    for i in range(1, 6):
        buf.store(i)
        time.sleep(1)


# Consumer thread
def f2():
    for i in range(1, 6):
        buf.ret()
        time.sleep(1)


# Main program
buf = buffer()

p = Thread(target=f1)
c = Thread(target=f2)

p.start()
c.start()

p.join()
c.join()

print('End of main thread')



'''
Write  a  function  to  print  number  of  500's , 200's , 100's , 50's , 20's , 10's , 5's ,  2's ,  1's   in  a  number

Let  input  be  2628
What  are  the  results ?  --->  500 - 5
			         100 - 1
				  20 - 1
				   5 - 1
				   2 - 1
				   1 - 1


		                       
1) List  b    --->   [5 , 0 , 1 , 0]     
		              	     
2) Let  input  be  2628
    2628 // 500 =  5
    2628 % 500 =  128
    128 // 200 =  0
    128 % 200 =  128
    128 // 100 =  1
    128 % 100 = 28
    28 // 50 = 0
    28 % 50 =  28
    and  so  on
'''
def  denom(n):
	How  create  a  list
	How  to  store  9  results  in  list  with  for  loop
	How  to  return  list
# denom(2878)
a = [500 , 200 , 100 , 50 , 20 , 10 , 5 , 2 , 1]
n = int(input('Enter  any   number:  '))
How  to  call  denom()  function
How  to  print  non-zero  elements  of  list  and  also  elements  of  list  'a'




def denom(n):
    b = []   # Empty list to store results

    for d in a:
        b.append(n // d)   # Store quotient in list
        n = n % d          # Update remainder

    return b


a = [500, 200, 100, 50, 20, 10, 5, 2, 1]

n = int(input('Enter any number: '))

# Function call
b = denom(n)

# Print non-zero denominations
for i in range(len(a)):
    if b[i] != 0:
        print(a[i], '-', b[i])




'''
Write  a  program  to  convert  arabic   number  to   roman  number

1000 -  M
900 - CM
500 - D
400 - CD
100 - C
90 - XC
50 - L
40 - XL
10 - X
9 - IX
5 - V
4 - IV
1 - I

Arabic  number : 3878
Roman  number :   '' + 'MMM' + '' + 'D' + '' + 
3878 // 1000 = 3
3878 % 1000 =  878
878 // 900 = 0
878 % 900 =  878
878 // 500 =  1
878 % 500 =   378
378 // 400 = 0
378 % 400 =  378
and  so  on
'''
def   arabic_roman(n):
	Create  an  empty   string
	Concatenate  each  result  to  the  string 
	return  the  string
n = int(input('Enter  arabic  number  :   ')	
How  to  call  arbic_roman()  function
How  to   print  roman  number


def arabic_roman(n):

    # Arabic values
    a = [1000, 900, 500, 400, 100, 90,
         50, 40, 10, 9, 5, 4, 1]

    # Roman symbols
    r = ['M', 'CM', 'D', 'CD', 'C', 'XC',
         'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    s = ''   # Empty string

    for i in range(len(a)):

        q = n // a[i]      # Quotient

        s = s + (r[i] * q) # Concatenate roman symbols

        n = n % a[i]       # Remaining number

    return s


n = int(input('Enter arabic number : '))

# Function call
roman = arabic_roman(n)

# Print roman number
print('Roman number :', roman)