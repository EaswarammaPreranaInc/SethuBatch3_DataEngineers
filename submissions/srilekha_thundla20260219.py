#  Find  outputs
print({10 , 20}  |  {30 , 20})#{10,20,30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})#{10:'Hyd',20:'Sec',30:'Cyb'}
print(range(4) | range(5))#error
print([10 , 20]  |  [30 , 20])#error



#  //  operator  demo  program
print(9 // 2)   #  prev  integer(4.5)   = 4
print(9.0 // 2)  #    prev  integer(4.5)   = 4.0
print(9 // 2.0)   #   prev  integer(4.5)   = 4.0
print(9.0 // 2.0)   #   prev  integer(4.5)   = 4.0
print(10.5 // 2)#6
print(10 // 3)#3
print(10.0 // 3)#3.0
print(8.5 // 3)#2.0
print(18 // 4)#4
print(-18 // 4)  #  Tricky   4
print(-(18 // 4))  #  Tricky 4


'''
//  operator
--------------
1) What  is  the  result  of  integer // integer ?  ---> Integer  quotient
    What  is  the  result  of  integer // float ?  --->  Float  quotient  with  .0
    What  is  the  result  of  float // integer ?  --->	Float  quotient  with  .0
    What  is  the  result  of  float // float ?  ---> Float  quotient  with  .0
'''


# Find outputs
print(7 / 0)# error
print(7 // 0)# error
print(7 % 0)# error


# ** operator demo program
print(3 ** 4)  #   3 ^ 4 = 81
print(10 ** -2)#100
print(4 * 3 * 2)#24
print(3 + 4 * 5 - 32 / 2 ** 3)#9/8 = 1




'''

**  operator
---------------
1) What  is  **  operator  called ?  --->  Exponential  operator

2) What  is  the  result  of  a ** b ?  ---> a ^ b

3) What  is  the  result  of  a * b  * c ?   --->  a ^ b ^ c

4) What  is  the  associativity  of  **  operator ?  ---> Right  to  left
    What  is  the  associativity  of  remaining  arithmetic  operators ?  --->  Left  to  right
'''

#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True  
print(9 >= 9)  #   True
print(9 >= 12)  #  False 
print(6 <= 8)#True
print(6 <= 6)#True
print(6 <= 4)#False
print(9 != 7)#True
print(6 == 8)#False
print(True  >  False)#True
print(3 + 4j == 3 + 4j)#True
print(3 + 4j == 5 + 6j)#False
print(3 + 4j != 5 + 6j)#False
print(10 == 10.0)#True
print(3 + 4j >  3 + 4j)#False



#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #  True :  'm' > 'j'
print('Rama'  <  'Sita')   #   True :   'R' < 'S'
print('Hyd'  ==  'Hyd')  #  True
print('Rama'  <=   'Ramana')#True
print('Rama  Rao'  >=  'Rama')#True
print('Hyd'  != 'Sec')#True
print('HYD'  <   'hyd')#False



'''
1) Can  strings  be  compared  with  > ,  < , == ,  >= , <=  and  != ?  --->   Yes  only  in  python  but  not  in  other  languages

2) What  are  compared  internally  when  strings  are  compared ? --->  1st  non-matching  characters

3) Are  characters  compared  (or)  their  unicode  values ?  --->  Unicode  values

4) How  many  unicode  values  exist ?  --->  512

5) What  is  the  range  of  unicode  values ?  --->  0  to  511

6) What  are  the  unicode  values  of  'A'  to  '…

'''



# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #  False
print(10 < 20 > 30)#False
print(1 < 2 < 3 < 4)#True
print(1 < 2 > 3 > 1)#False
print(4 > 3 >= 3 > 2)#True


#  or  operator  demo program
print(True  or  False)  #   True
print(False  or  True)  #   True
print(True  or  True) #  True
print(False  or   False) #  False
print(10  or  20)  #   10
print(0   or  20)  #  20
print(-25  or  0)# 0
print(''  or  35)#35
print(6j  or  'Hyd')#6j
print(0.0  or  3 + 4j)#3+4j
print('Hyd'   or   10.8)#'Hyd'





'''
or  operator
--------------
1) When  is  the  result  of  or  operator  True ?  --->  When  at  least  one  operand  is  True
    When  is  the  result  of  or  operator  False ?  ---> When  both  the  operands  are  False

2) What  is  the  result  of  op1  or  op2  when  op1  is  False ?  ---> op2
    What  is  the  result  of  op1  or  op2  when  op1  is  True ?  ---> op1

3) and ,  or  operators  are  quite  opposite
'''



# not  operator  demo  program
print(not  True)  #   False
print(not  False) #   True
print(not  25) #   False
print(not  0)# True
print(not  'Hyd')# False
print(not  '')#False
print(not  -10)#False
print(not  not  'Hyd')#True



'''
not  operator
----------------
1) What  does  not  operator  do ?  --->  Complement  operation

2) Is  not  a  unary  operator  ?  --->  Yes  due  to  single  operand
    What  about  and ,  or ? ---> Binary  operators  due  to  two  operands

3) What  is  the  associativity  of  unary  operators ?  ---> Right  to  Left
    What  is  the  associativity  of  binary  operators ?  ---> Left  to  Right  except  for  **
'''


#  Find   outputs (Home work)
i = 10
i = not  i > 14
print(i) # True
print(not(6 < 4  or  9 >= 5  and  6 != 6))#True


Assignment  operators  demo  program  (Home  work)
a = 25
print(a)#25
b =  a
print(b)#25
print(a  is  b)#True
x = 4
y = 5
z = x + y * 6
print(z)#34
25 = a
a + b = x + y


# Find outputs (Home work)
a = b = c = 25
print(id(a))#address of a will be printed 
print(id(b))#address of b will be printed
print(id(c))#address of c will be printed
print(a , b , c)#(25,25,25)



# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x)#25
print(y)#10.8
print(z)#'Hyd'




# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c   
print(a)#9




# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4 
print(a)#9


# Find outputs (Home work)
a = 3
a **= 4 
print(a)#81


# Identity operators demo program
a = 25
b = 25
print(a  is  b)#True
print(a  is  not  b)#False
print(a == b)#True


# Find outputs (Home work)
a = 25
b = 25.0
print(a is b)#False
print(a is not b)#True
print(a == b)#True