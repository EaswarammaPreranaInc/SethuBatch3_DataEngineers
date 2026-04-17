import math
print(9 // 2)   #  prev  integer(4.5)   = 4
print(9.0 // 2)  #    prev  integer(4.5)   = 4.0
print(9 // 2.0)   #   prev  integer(4.5)   = 4.0
print(9.0 // 2.0)   #   prev  integer(4.5)   = 4.0
print(10.5 // 2)       # 5.0
print(10 // 3)         # 3
print(10.0 // 3)       # 3.0
print(8.5 // 3)        # 2.0
print(18 // 4)         # 4
print(-18 // 4)     # -5
print(-(18 // 4))  #  -4



print(3 ** 4)                      #  81
print(10 ** -2)                    #  0.01
print(4 * 3 * 2)                   #  24
print(3 + 4 * 5 - 32 / 2 ** 3)     # 19.0


print(9 >= 5)                      #   True  
print(9 >= 9)                      #   True
print(9 >= 12)                     #  False 
print(6 <= 8)                      # True
print(6 <= 6)                       # True
print(6 <= 4)                       #False
print(9 != 7)                       #true
print(6 == 8)                       # False
print(True  >  False)               # True
print(3 + 4j == 3 + 4j)              #True
print(3 + 4j == 5 + 6j)             # false
print(3 + 4j != 5 + 6j)             #true
print(10 == 10.0)                   # true
#print(3 + 4j >  3 + 4j)             # error


print('Rama'   >  'Rajesh')           #  True :  'm' > 'j'
print('Rama'  <  'Sita')              #   True :   'R' < 'S'
print('Hyd'  ==  'Hyd')               #  True
print('Rama'  <=   'Ramana')          #   True
print('Rama  Rao'  >=  'Rama')         #true
print('Hyd'  != 'Sec')                # True
print('HYD'  <   'hyd')               # True

print(" Chaining relation Operator")

print(10 < 20 < 30)                  #   True
print(10 >= 20 < 30)                 #  False
print(10 < 20 > 30)                  # False
print(1 < 2 < 3 < 4)                 # True
print(1 < 2 > 3 > 1)                 # False
print(4 > 3 >= 3 > 2)                # True

 
print("OR Operator")

print(True  or  False)             #   True
print(False  or  True)             #   True
print(True  or  True)              #  True
print(False  or   False)           #  False
print(10  or  20)                  #   10
print(0   or  20)                  #  20
print(-25  or  0)                  # -25
print(''  or  35)                  # 35
print(6j  or  'Hyd')               #6j
print(0.0  or  3 + 4j)             # 3+4j
print('Hyd'   or   10.8)           # Hyd

 
print("Not Operator")
 
i = 10
i = not  i > 14 
print(i)                             # True
print(not(6 < 4  or  9 >= 5  and  6 != 6))  # True



print("not Operator")
print(not  True)          #   False
print(not  False)         #   True
print(not  25)            #   False
print(not  0)             #  False
print(not  'Hyd')         # false
print(not  '')             # True
print(not  -10)            # False
print(not  not  'Hyd')     #True



a = 25                 
print(a)                # 25
b =  a                  
print(b)                # 25
print(a  is  b)         # True
x = 4 
y = 5
z = x + y * 6 
print(z)               # 34
#25 = a                # error
#a + b = x + y         # error

print("nextline")
 
a = b = c = 25 
print(id(a))           # address of object       
print(id(b))           # same address of object
print(id(c))           # same address of object
print(a , b , c)       # 25 25 25

print("nextLine")

x , y , z = 25 , 10.8 , 'Hyd'
print(x)                 # 25
print(y)                 # 10.8
print(z)                 # Hyd


a , b , c = 3 , 4 , 5
a *= b + c                 
print(a)                # 27




a = 'Hyd'
b = 'Hyd'
print(a  is  b)               # True
print(a  is  not  b)          # False
print(a == b)                 # True
print()                       #
x = [1 , 2 , 3 , 4]         
y = [1 , 2 , 3 , 4]
print(x is y)                 # false
print(x  is  not  y)          # true
print(x == y)                 # True
print()                       #
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n)               # true
print(m  is  not  n)          # False
print(m == n)                  #True
print(x == m)                 #false

print()
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b)         #False
print(a  ==  b)         # False

print("hello worls")

list = [10 , 20 , 15 , 12 , 18]
print(15 in list)                  # True
print(19 in list)                  # False
print(14 not in list)              # True
print(15 not in list)              # false
s = 'Hyd is green city'
print( 'is' in s)                  # True
print('was' in s)                  # False
print('g' in s)                    # True
print('z' in s)                    # False
print(' ' in s)                    # True
print('gre' in s)                  # True
print('yd i' in s)                 # True
print('' in s)                     # True
print('' not in s)                 #False



print(math . pow(2 , 3))        #  2 ^ 3 = 8
print(math . pow(-2 , -3))      # -0.125
print(math . pow(10 , -2))      # 0.01
print(math . pow(4 , math . pow(3 , 2))) #262144.0

 
print(" ")

# sqrt()  function  demo  program
import  math
print(math . sqrt(25))                  #5.0
print(math . sqrt(10))                  #3.162
print(math . sqrt(6.25))                #2.5
print(math . sqrt(True))                # 1.0
#print(math . sqrt(3+4j))                # Error
print(math . sqrt(math . sqrt(256)))     #4.0
print(math . sqrt(math . pow(3 , 4)))   # 9.0
#print(math . sqrt(-16))                # error
#print(sqrt(49))                       # error


print(math . fabs(-10))            #10.0
print(math . fabs(-25.6))          #26.6
print(math . fabs(20))             #20.0
print(math . fabs(35.8))           # 35.8
#print(fabs(-25))                  Error



print(math . floor(10.8))               #  10
print(math . ceil(10.8))                #   11
print(math . floor(25.0))               #25        
print(math . ceil(25.0))                #25
print(math . floor(-3.5))               # -4
print(math . ceil(-3.5))                #-3
print(math . floor(-9.0))               #-9
print(math . ceil(-9.0))                #-9
print(math . floor(25.1))              #25
print(math . ceil(25.1))               # 26
#print(floor(3.5))
#print(ceil(3.5))