#1
#  Find  outputs
print({10 , 20}  |  {30 , 20}) #{10, 20, 30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})  #{10: 'Hyd', 20: 'Vja', 30: 'Cyb'}
print(range(4) | range(5)) #Error as range object can't be concatenated 
print([10 , 20]  |  [30 , 20]) #Error lists can't be concatenated by '|' operated isntead one can use '+' operator



#2
#  //  operator  demo  program
print(9 // 2) #previous  integer(4.5) = 4
print(9.0 // 2) #previous  integer(4.5) = 4.0
print(9 // 2.0) #previous  integer(4.5) = 4.0
print(9.0 // 2.0) #previous  integer(4.5) = 4.0
print(10.5 // 2) #previous integer(5.25) = 5.0
print(10 // 3) #previous integer(3.34) = 3
print(10.0 // 3) #previous integer(3.34) = 3.0
print(8.5 // 3) #previous integer(2.84) = 2.0
print(18 // 4) #previous integer(4.5) = 4
print(-18 // 4) #Tricky - previous integer(-4.5) = -5.0 i.e. rounded off
print(-(18 // 4)) #Tricky - previous integer(-(4.5)) = -4



#3
# Find outputs
print(7 / 0) #Error as one can't divide an object by 0 i.e. Division by zero can't be performed hence quotient can't be retrieved 
print(7 // 0) #Error as one can't divide an object by 0 i.e. Division by zero can't be performed hence quotient can't be retrieved
print(7 % 0) #Error as one can't divide an object by 0 i.e. Division by zero can't be performed hence modulo or remainder can't be retrieved



#4
# ** operator demo program
print(3 ** 4) #3 ^ 4 = 81
print(10 ** -2) #10 ^ (-2) = 0.01
print(4 * 3 * 2) #24
print(3 + 4 * 5 - 32 / 2 ** 3) #3 + 4 * 5 - 32 / 8 => 3 + 20 - 32 / 8 => 3 + 20 - 4 = 19



#5
#  Relational  operators  demo  program (Home  work)
print(9 >= 5) #True  
print(9 >= 9) #True
print(9 >= 12) #False 
print(6 <= 8) #True
print(6 <= 6) #True
print(6 <= 4) #False
print(9 != 7) #True
print(6 == 8) #False
print(True  >  False) #True
print(3 + 4j == 3 + 4j) #True
print(3 + 4j == 5 + 6j) #False
print(3 + 4j != 5 + 6j) #True
print(10 == 10.0) #True
print(3 + 4j >  3 + 4j) #Error as '>' operator can't justify or compare two complex numbers



#6
#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh') #True: 'm' > 'j'
print('Rama'  <  'Sita') #True: 'R' < 'S'
print('Hyd'  ==  'Hyd') #True
print('Rama'  <=   'Ramana') #True
print('Rama  Rao'  >=  'Rama') #True
print('Hyd'  != 'Sec') #True
print('HYD'  <   'hyd') #True



#7
# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30) #True
print(10 >= 20 < 30) #False
print(10 < 20 > 30) #False
print(1 < 2 < 3 < 4) #True
print(1 < 2 > 3 > 1) #False
print(4 > 3 >= 3 > 2) #True



#8
print(True  or  False)  #True
print(False  or  True)  #True
print(True  or  True) #True
print(False  or   False) #False
print(10  or  20)  #10
print(0   or  20)  #20
print(-25  or  0) #-25
print(''  or  35) #35
print(6j  or  'Hyd') #6j
print(0.0  or  3 + 4j) #3+4j
print('Hyd'   or   10.8) #Hyd



#9
# not  operator  demo  program
print(not  True)  #False
print(not  False) #True
print(not  25) #False
print(not  0) #True
print(not  'Hyd') #False
print(not  '') #True
print(not  -10) #False
print(not  not  'Hyd') #True



#10
#  Find   outputs (Home work)
i = 10
i = not  i > 14 #i = 10 > 14 => False => not False = True
print(i) #False
print(not(6 < 4  or  9 >= 5  and  6 != 6)) #not(False or True and False) i.e. Priority: Relational operators before Logical Operatiors => not(False or False) i.e 'and' is top priority upon 'or' => not(False) = True



#11
#  Assignment  operators  demo  program  (Home  work)
a = 25
print(a) #25
b = a
print(b) #25
print(a  is  b) #True as both refernces are matched 
x = 4
y = 5
z = x + y * 6
print(z) #34
25 = a #Error as reference can't be an immuatble object
a + b = x + y #Error as sum of two objects can't be assigned to sum of two another objects



#12
# Find outputs (Home work)
a = b = c = 25
print(id(a)) #Some random address assigned to 'a' by the IDE or PVM
print(id(b)) #Same random address assigned to 'a' by the IDE or PVM
print(id(c)) #Same random address assigned to 'a' by the IDE or PVM
print(a , b , c) #25<space>25<space>25



#13
## Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x) #25
print(y) #10.8
print(z) #Hyd



#14
# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c # a = a * (b + c) i.e. a = 3 * (4 + 5) => a = 3 * (9) => a = 27   
print(a) #27



#15
# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4 # a =  a % (3 + 2 * 4) => a = 20 % (3 + 8) => a = 20 % (11) => a = 9
print(a) #9



#16
# Find outputs (Home work)
a = 3
a **= 4 # a = a ** (4) => a = 3 ** (4) => a = 81
print(a) #81



#17
# Identity operators demo program
a = 25
b = 25
print(a  is  b) #True
print(a  is  not  b) #False
print(a == b) #True



#18
# Find outputs (Home work)
a = 25
b = 25.0
print(a is b) #False as 25 and 25.0 fall under different class type
print(a is not b) #True
print(a == b) #True as both as object 25 and 25.0 are same i.e. value



#19
# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b) #True
print(a  is  not  b) #False
print(a == b) #True
print() #Nothing or Empty
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y) #False
print(x  is  not  y) #True
print(x == y) #True
print() #Nothing or Empty
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n) #True
print(m  is  not  n) #False
print(m == n) #True
print(x == m) #False



#20
# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) #False due to ordered nature of lists
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b) #False due to ordered nature of tuples
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q) #True due to unordered nature of sets
m = range(5)
n = range(5)
print(m == n) #True as the objects in both the range() object are the same i.e 0, 1, 2, 3 and 4



#21
# Find outputs (Home work)
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b) #False as both 'a' and 'b' do belong to different class types i.e. list and tuple respectively
print(a  ==  b) #False as both 'a' and 'b' do belong to different class types i.e. list and tuple respectively



#22
# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list) #True
print(19 in list) #False
print(14 not in list) #True
print(15 not in list) #False
s = 'Hyd is green city'
print('is' in s) #True
print('was' in s) #False
print('g' in s) #True
print('z' in s) #False
print(' ' in s) #True
print('gre' in s) #True
print('yd i' in s) #True
print('' in s) #True
print('' not in s) #False



#23
#  ++  and  --  operators  demo  program
a = 25
print(++a) # +(+a) = +a = +25 = 25
print(a++) # (a+)+ = a+ = 25+ => Error
print(a++1) # a + (+1) = 25 + 1 = 26
print(--a) # -(-a) = +a = +25 = 25
print(a--) # (a-)- = a+ = 25+ => Error
print(a--1) # (a-)-1 = a + 1 = 25 + 1 = 26 
print(-a) # -(a) = -a = -25
print(+-a) # +(-a) = -a = -25
print(-+a) # -(+a) = -a = -25



#24
#  Semicolon  demo  program
print('One'); #One - ';' is optional in python as by using print() by default it goes to the next line
print('Two'); #Two - ';' is optional in python as by using print() by default it goes to the next line
print('Three'); #Three - ';' is optional in python as by using print() by default it goes to the next line
print('Hyd')  ;   print('Sec')  ;  print('Cyb') #Hyd<next line>Sec<next line>Cyb -';' is optional in python as by using print() by default it goes to the next line



#25
#pow()  function  demo  program
import math
print(math.pow(2 , 3))  # 2 ^ 3 = 8
print(math.pow(-2 , -3)) # -2 ^ -3 = -0.125
print(math.pow(10 , -2)) # 10 ^ (-2) = 0.01
print(math.pow(4 , math . pow(3 , 2))) # 4 ^ (3 ^ 2) = 262144



#26
# sqrt()  function  demo  program
import math
print(math.sqrt(25)) #5
print(math.sqrt(10)) #3.16
print(math.sqrt(6.25)) #2.5
print(math.sqrt(True)) #1
print(math.sqrt(3+4j)) #Error as there would be no square roots for complex numbers or objects
print(math.sqrt(math.sqrt(256))) #math.sqrt(256) = 16 => math.sqrt(16) = 4
print(math.sqrt(math.pow(3 , 4))) #math.sqrt(3 ^ 4) => math.sqrt(81) = 9
print(math.sqrt(-16)) #Error as no square roots are present or permitted in python but in mathematics it turns out to be '4i'
print(sqrt(49)) #Error because sqrt() function is not defined earlier



#27
# fabs()  function  demo   program
import math
print(math.fabs(-10)) #10.0
print(math.fabs(-25.6)) #25.6
print(math.fabs(20)) #20.0
print(math.fabs(35.8)) #35.8
print(fabs(-25)) #Error because sqrt() function is not defined earlier



#28
#  floor()  and  ceil()  functions  demo  program
import math
print(math.floor(10.8)) #10
print(math.ceil(10.8)) #11
print(math.floor(25.0)) #25
print(math.ceil(25.0)) #25
print(math.floor(-3.5)) #-4
print(math.ceil(-3.5)) #-3
print(math.floor(-9.0)) #-9
print(math.ceil(-9.0)) #-9
print(math.floor(25.1)) #25
print(math.ceil(25.1)) #26
print(floor(3.5)) #Error because floor() function is not defined earlier
print(ceil(3.5)) #Error because ceil() function is not defined earlier