print({10,20} | {30,20}) # we cannot concatenate because of no duplicates are allowed.
print({10:'hyd',20:'sec'} | {30:'cyb',20:'Vja'}) #we cannot concatenate because no duplicate key are allowed.
print(range(4) | (range(5)) #we cannot concatenate because no duplicate are allowed.
print([10,20] | [30,20]) # we can concatenate list we get a new list object.


print(9//2) #4 
integer(4.5) #4
print(9//2) #3
integer(4.5) = 4.0 #4
print(9 // 2.0) #3.0
integer(4.5) =4.0 #4
print(10.5//2) # 5.0
print(10//3) # 3
print(10.0 // 3) #3.0
print(8.5//3) #2.0
print(18//4) #4
print(-18//4) # -4
print(-(18//4) -4

print(7/0) # zero division error we cannot divide any with 0.
print(7 // 0) #we cannot divide with 0.
print(7%0) # we cannot divide with 0.

print(3**4) # 81
print(10**2) #100
print(4*3*2) #24
print(3+4*5-32/2**3) #19


print( 9 >= 5) # True 
print( 9 >= 9) # True
print( 6 <= 8) #true
print( 6 <= 6) #True
print( 9!= 7) #True
print( 6 == 8) #False
print( True >False)  #True
print(3+4j == 3+4j) #True
print(3+4j != 5+6j) #True
print(10 ==10.0) #False
print( 3+4j > 3+4j) #False

print('Rama' > 'Rajesh') # True
print('Rama' < 'Sita') # True
print('Hyd' == 'Hyd') # True
print('Rama Rao' >= 'Rama') #True
print('Hyd' != 'Sec') # True
print('HYD' < 'hyd') # False

print(10 < 20 < 30) # True
print( 10 >= 20 > 30) #False
print(10 < 20 > 30) #False
print( 1 < 2 < 3 < 4)  # True
print(1 < 2 > 3 > 1) # False
print(4 > 3 >= 3 >2) # True

print( True or False) #True
print(False or True) #True
print(False or False) #False
print(10 or 20) #10
print(0 or 20) #20
print(-25 or 0) #0
print('' or 35) ''
print(6j or 'hyd') #6j
print(0.0 or 3+4j) #3+4j
print('hyd' or 10.8) #hyd

print(not True) #False
print(not False) #True
print( not 25) # False
print(not '') False
print(not -10) #True
print(not not 'hyd')

i = 10
i = not i >14 # Error
print(i) # 10 
print(not (6 <4 or 9 >= 5 and 6!=6)) #True

a = 25
print(a) # 25 is printed 

b = a
print(b) # referece is copied from a to b reusable object.

print(a is b) #True

x=4 
y=5
z=x+y*6 #reference of 54 is stored
print(z) 

25 = a #ERROR we cannot have reference with int 
a+b = x+y # Error


a = b = c = 25 
print(id(a)) # id of an object 25.
print(id(b)) #same address
print(id(c)) # same address.
print(a,b,c)

x,y,z = 25,10.8,'hyd'
print(x) #25
print(y) #10.8
print(z) #hyd

a,b,c = 3,4,5
a*=b+c   # a= a*b+c
print(a) #12

a = 3 
a**=4 #a = a**4
print(a)  #81

a =20 
a %= 3+2*4 #a= a % 3 + 2*4
print(a) #14.0

a = 3
a ** =4 # a = a ** 4 
print(a) # 81

 a = 25
 b = 25
 
 print(a is b) # object of reference is compared
 print(a is not b) # False
 print(a == b) # object value is compared therefor True.
 
 a=25
 b=25.0
 print( a is b) # False
 print(a is not b)#True
 print(a == b) #True
 
 
 a ='Hyd'
 b ='Hyd'
 print(a is b) #True
 print(a is not b) #False
 print(a == b) #True
 print()
 
 x = [1,2,3,4]
 y = [1,2,3,4]
 print(x is y) #False
 print(x is not y) #True
 print( x == y) #True
 print()
 m = (1,2,3,4)
 n = (1,2,3,4)
 print(m is n) # False
 print(m == n) #True
 print(m is not n) #True
 print(x == m) #False
 
 
 x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y)  #False
a = (4 , 1 , 3 , 2) 
b = (4 , 2 , 3 , 1)
print(a == b)  #False
p = {1 , 2 , 3 , 4} 
q = {4 , 1 , 3 , 2}
print(p == q)   #True
m = range(5)
n = range(5)
print(m == n) #True


 a = [10,20,30] #object list                        
 b = (10,20,30) #object tuple                     
 print(a is b) # Flase
 print(a ==b) # True
 
list = [10,20,15,12,18]
print(15 in list) #True
print(19 in list) #False
print(14 not in list) #true
print(15 not in list) #False

s = 'Hyd is green city'
print('is' in s) #True
print('was' in s) #False
print('g' in s) #true
print('z' in s) #False
print(' ' in s) #True
print('gre' in s) #True
print('yd' in s) #True
print('' in s) #True
print('' not in s) #False

a = 25
print(++a) #+(+a) = +a = +25 = 25
print(a++) # (a+)+ = a+ = 25+ Error
print(a++1)  #  a + (+1)  =  25 + 1 = 26
print(--a) # -(-a) = -a = 25+ Error
print(a--) #(a-)- = a- = -25
print(a--1) #(a-)-1 = a- -1 = 26
print(-a) #-(a) = -a = -25
print(+-a) #+(-a) -a = -25
print(-+a) # -(+a) =-a = -25



print('One') #one
print('Two') #two
print('three)# three
print('Hyd'),print('Sec'),print('Cyb)
#Hyd
#Sec
#Cyb

#import math

print(math.pow(2,3)) #2^3 = 8
print(math.pow(-2,-3)) #-0.125
print(math.pow(10^-2)) #0.01
print(math.pow(4,math.pow(3,2))) #6561

#import math
print(math.sqrt(25)) #120
print(math.sqrt(10)) # 100
print(math.sqrt(6.25)) #2.5
print(math . sqrt(True)) #1.0
print(math . sqrt(3+4j)) #Error complex number will not square root
print(math . sqrt(math . sqrt(256))) #4.0
print(math . sqrt(math . pow(3 , 4))) #9.0
print(math . sqrt(-16)) #Error no negative square roots.
print(sqrt(49)) #no module in present sqrt in here.



import  math
print(math . fabs(-10)) #10.0
print(math . fabs(-25.6)) #25.0
print(math . fabs(20)) #20.0
print(math . fabs(35.8)) #35.8
print(fabs(-25)) #Error because not fabs module in here.



import  math
print(math . floor(10.8))  #  10
print(math . ceil(10.8))  #   11
print(math . floor(25.0)) #25
print(math . ceil(25.0)) #25
print(math . floor(-3.5)) #-4
print(math . ceil(-3.5)) #3
print(math . floor(-9.0)) -9
print(math . ceil(-9.0)) #-9
print(math . floor(25.1)) #25
print(math . ceil(25.1)) #26
print(floor(3.5)) #Error no module 
print(ceil(3.5)) #Error no module.



















