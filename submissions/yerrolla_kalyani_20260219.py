
# #  Find  outputs
print({10 , 20}  |  {30 , 20})					#{10,20,30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})	#{10 : 'Hyd' , 20 : 'Vja' , 30 : 'Cyb' }
print(range(4) | range(5))					#error range not support |concatenation 
print([10 , 20]  |  [30 , 20])					#error list  is concatenate though the + operator not through|
__________________________________

 #  //  operator  demo  program
print(9 // 2)   #  prev  integer(4.5)   = 4
print(9.0 // 2)  #    prev  integer(4.5)   = 4.0
print(9 // 2.0)   #   prev  integer(4.5)   = 4.0
print(9.0 // 2.0)   #   prev  integer(4.5)   = 4.0
print(10.5 // 2)  #   prev  integer(5.25)=5.0
nt(10 // 3) #   prev  integer(3.3)=3
print(10.0 // 3) #   prev  integer(3.3)=3.0
print(8.5 // 3) #   prev  integer(2.83)=2.0
print(18 // 4) #   prev  integer(4.5)=4
print(-18 // 4)  ####  Tricky  prev  integer(-4.5)=-5
print(-(18 // 4))  #  Tricky   prev  integer(4.5)=-4.0



____________________________________________
 # ** operator demo program
print(3 ** 4)  #   3 ^ 4 = 81
print(10 ** -2)#0.01
print(4 **3 **2)#262144
print(3 + 4 * 5 - 32 / 2 ** 3)#19.0

___________________________

 #  Relational  operators  demo  program (Home  work)
print(9 >= 5) 		 #   True  
print(9 >= 9) 		 #   True
print(9 >= 12)  	#  False 
print(6 <= 8)		#True
print(6 <= 6)		#True
print(6 <= 4)		#False
print(9 != 7)		#True
print(6 == 8)		#False
print(True  >  False)	#True
print(3 + 4j == 3 + 4j)	#True
print(3 + 4j == 5 + 6j)	#False
print(3 + 4j != 5 + 6j)	#True
print(10 == 10.0)	#False#True
print(3 + 4j >  3 + 4j)	#Complex numbers cannot be compared with <, >, <=, >=

____________________________________________

#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  	#  True :  'm' > 'j'
print('Rama'  <  'Sita')  	 #   True :   'R' < 'S'
print('Hyd'  ==  'Hyd')  	#  True
print('Rama'  <=   'Ramana')	#True
print('Rama  Rao'  >=  'Rama')	#True
print('Hyd'  != 'Sec')		#True
print('HYD'  <   'hyd')		#True

___________________________________________________

# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30) 		 #   True
print(10 >= 20 < 30) 		 #  False
print(10 < 20 > 30)		# False
print(1 < 2 < 3 < 4)		#True
print(1 < 2 > 3 > 1)		#False
print(4 > 3 >= 3 > 2)		#True
_________________________________________________
 #  or  operator  demo program
print(True  or  False)  	#   True
print(False  or  True) 		 #   True
print(True  or  True)		 #  True
print(False  or   False) 	#  False
print(10  or  20)  		#   10
print(0   or  20) 		 #  20
print(-25  or  0)		#-25
print(''  or  35)		#35
print(6j  or  'Hyd')		#6j
print(0.0  or  3 + 4j)		#3 + 4j
print('Hyd'   or   10.8)	#'Hyd'

_______________________________________________

# not  operator  demo  program
print(not  True) 	 #   False
print(not  False) 	#   True
print(not  25) 		#   False
print(not  0)		#True
print(not  'Hyd')	#   False
print(not  '')		#   True
print(not -10)		#   False
print(not  not  'Hyd')  #   True
 
____________________________________________________



 #Find   outputs (Home work)
i = 10
i = not  i > 14
print(i)					#True
print(not(6 < 4  or  9 >= 5  and  6 != 6))	#  True

#  Assignment  operators  demo  program  (Home  work)
a = 25
print(a)					#25
b =  a
print(b)					#25
print(a  is  b)					#True
x = 4
y = 5
z = x + y * 6
print(z)					#34
25 = a						#error the reference should be left to the assignment operator and value to right side assignment operator(syntax error)
a + b = x + y					#error the reference should be one operand but not 2(syntax error)
________________________________________________________

# Find outputs (Home work)
a = b = c = 25
print(id(a))			#address of the of the int object 25
print(id(b))			#address of the of the int object 25(same address)
print(id(c))			#address of the of the int object 25(same address)
print(a , b , c)		#25<space>25<space>25

___________________________________________
# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x)		#25
print(y)		#10.8
print(z)		#Hyd

# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c  
print(a)#27
# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4 
print(a)#9
# Find outputs (Home work)
a = 3
a **= 4 
print(a)#81
___________________________

# Identity operators demo program
a = 25
b = 25
print(a  is  b)		#True
print(a  is  not  b)	#False
print(a == b)		#True
# Find outputs (Home work)
a = 25
b = 25.0
print(a is b)		#False
print(a is not b)	#True
print(a == b)		#True
____________________________

# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b)		#True
print(a  is  not  b)	#False
print(a == b)		#True
print()			#does not print anything
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y)		#False
print(x  is  not  y)	#True
print(x == y)		#False
print()			#does not print anything
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n)		#True
print(m  is  not  n)	#False
print(m == n)		#True
print(x == m)		#False
___________________________
# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) 		#False
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)	 	 #False
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q)  		#True
m = range(5)
n = range(5)
print(m == n)		#True
# Find outputs (Home work)
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b)		 #False
print(a  ==  b)		#False
___________________________

# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)	#True
print(19 in list)	#False
print(14 not in list)	#True
print(15 not in list)	#False
s = 'Hyd is green city'
print( 'is' in s)	#True
print('was' in s)	#False
print('g' in s)		#True
print('z' in s)		#False
print(' ' in s)		#True
print('gre' in s)	#True
print('yd i' in s)	#True
print('' in s)		#True
print('' not in s)	#False
__________________________________________

#  ++  and  --  operators  demo  program
a = 25
print(++a) 	 #   +(+a) = +a = +25 = 25
print(a++)   	#  (a+)+  = a+ = 25+   --->  Error
print(a++1) 	 #  a + (+1)  =  25 + 1 = 26
print(--a)	#25
print(a--)	# error becoz 25-
print(a--1)	#26
print(-a)	#-25
print(+-a)	#-25
print(-+a)	#-25
_____________________________

#  Semicolon  demo  program
print('One');		#One
print('Two');		#Two
print('Three');		#Three
print('Hyd')  ; 	#Hyd 
 print('Sec')  ; 	 #Sec
print('Cyb')#Cyb
---------------------------

#pow()  function  demo  program
import  math
print(math . pow(2 , 3))  		#  2 ^ 3 = 8
print(math . pow(-2 , -3))		#-0.125
print(math . pow(10 , -2))		#0.01
print(math . pow(4 , math . pow(3 , 2)))#4^9=262144

_______________________________________________

# sqrt()  function  demo  program
import  math
print(math . sqrt(25))			#5.0
print(math . sqrt(10))			#3.1622776601683795
print(math . sqrt(6.25))		#2.5
print(math . sqrt(True))		#1.0
print(math . sqrt(3+4j))		#math.sqrt() works only for real numbers not complex numbers.
print(math . sqrt(math . sqrt(256)))	#4.0
print(math . sqrt(math . pow(3 , 4)))	#9.0
print(math . sqrt(-16))			#-4
print(sqrt(49))				#7.0

________________

# fabs()  function  demo   program
import  math
print(math . fabs(-10))		#-10.0
print(math . fabs(-25.6))	#25.6
print(math . fabs(20))		#20.0
print(math . fabs(35.8))	#35.8
print(fabs(-25))		#error becoz python not recognize it belong math module 


___________________________________________
import  math
print(math . floor(10.8))	  #  10
print(math . ceil(10.8))  	#   11
print(math . floor(25.0))	#25
print(math . ceil(25.0))	#25
print(math . floor(-3.5))	#-4
print(math . ceil(-3.5))	#-3
print(math . floor(-9.0))	#-9
print(math . ceil(-9.0))	#-9
print(math . floor(25.1))	#25
print(math . ceil(25.1))	#26
print(floor(3.5))		#error because  doesn’t know what floor and ceil are belong module
print(ceil(3.5))		#error because  doesn’t know what floor and ceil are belong module


