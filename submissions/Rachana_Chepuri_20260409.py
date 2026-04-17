# # mod1 . py
# print('Hyd') # Hyd
# print('Sec') # Sec
# print('Cyb') # Cyb
# x = 25
# def  f1():
# 	print('Function') #  Function
# class   c1:
# 	def   m1(self):
# 			print('Method') #Method
'''How  to  reuse  mod1  ?  (Home  work)'''
#  How  to  reuse  mod1  ?  (Home  work)
# print('Hello')
# How  to  import  mod1
# print(How  to  print   variable  'x'   of  mod1)
# How  to  call  function  f1()  of  mod1
# How  to  call  method  m1()  of  class  c1  in  mod1
# print('Bye')
# import  mod4
# print(x)
# f1()
'''Find  outputs  (Home  work)'''
#  Find  outputs  (Home  work)
# print('Before')
# How  to  run  mod1
# print(mod1 . x)
# mod1 . f1()
# a = mod1 . c1()
# print('After')
# run_module('mod1')
# runpy . run_module(mod1)
'''How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)'''
# print('Begin')  #  Begin
# import cal_1
# print(cal_1.x)  # 100
# print(cal_1.y)   # 200
# print(cal_1 . x)  # 100
# print(cal_1.add(10, 7) )  # 17
# print(cal_1.sub(10, 7))  # 3
# print(cal_1.mul(10, 7))  # 70 
# print(cal_1.div(10, 7))   #  1.42
# #print(cal_1 . add(x , y))
# b = cal_1 . c1()
# b.m1()
'''How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)'''
# print('Begin')
# from cal_1 import x, add, mul, c1
# print(x)# 100
# #print(y) #Error --y is not imported
# print(x)# 100
# print(add(10,7)) #17
# print(sub(10 , 7)) # Error---sub is not imported
# print(mul(10,7))# 70
# print(div(10 , 7)) # Error---div is not imported
# p=c1()
'''Module  alias'''
# print('Begin') # Begin
# import cal_1 as ball 
# print(ball.x) # 100
# print(ball.y) # 200
# print(ball.add(10,7)) # 17
# print(ball.sub(10,7)) # 3
# print(ball.mul(10,7)) # 70
# print(ball.div(10,7))  # 1.42
# obj = ball.c1()
# obj.m1() # m1 method
# print(ball . x) #100

'''Member  alias''' 
# from cal_1 import x as val, add as addition, mul as multiply, c1 as clclass #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
# print("Variable 'x' of cal module:", val) #100
# print("add(10, 7) of cal module:", addition(10, 7)) # 17
# print("mul(10, 7) of cal module:", multiply(10, 7)) # 70

# obj = clClass()
# obj.m1()
'''How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)'''
print('Begin')
import cal_1
print(cal_1.x)
print(cal_1.y)
#print(cal . x)# Error
print(cal_1.add(10,7))
print(cal_1.sub(10,7))
print(cal_1.mul(10,7))
print(cal_1.div(10,7))
#print(cal . add(x , y)) # Error
obj=cal_1.c1()
obj.m1()
#b = cal . c1() # Error





'''Find  outputs'''
# class  Rat:
# 	def   __init__(self , nr1 = 22, dr1 = 7):
# 		self . nr = nr1
# 		self . dr = dr1
# 	def   __str__(self):
# 		return  F'{self . nr}  /  {self . dr}'
# #end  of  the  class
# a = Rat()
# b = Rat(9)
# c = Rat(5,  8)
# d = Rat(dr1 = 9)
# e = Rat(dr1 = 3 , nr1 = 2)
# x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
# y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
# f = Rat(x , y) 
# print('a  :  ' , a)# 22/7
# print('b  :  ' , b)# 9/7
# print('c  :  ' , c)# 5/8
# print('d  :  ' , d)# 22/9
# print('e  :  ' , e)# 2/3
# print('f  :  ' , f)# 11/15
# c . __init__()
# print('c  :  ' , c)# 22/7
# a . __init__(3.8  , 4.6) 
# print('a  :  ' , a)# 3.8/4.6
# g = Rat(nr1 = 9 , 5) # error--after KA , PA not come
# h = Rat(nr = 9 , dr = 5) #Error--arguments are nr1 , dr1
'''Find  outputs (Home  work)'''
# class  Date:
#         def   _init_(self , dd1 , mm1  , yy1):
#                 self . dd = dd1
#                 self . mm = mm1
#                 self . yy = yy1
# # End  of  the  class
# a = Date(15 , 8 , 1947)
# b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
# c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
# print('a  :  ' , a . __dict__) 
# print('b  :  ' , b . __dict__)  
# print('c  :  ' , c . __dict__) 
# d = Date()
# e = Date(dd = 30 , mm = 4 , yy = 2022)
# f = Date(dd1 = 26 , mm1 = 8 , 2023) # Error--after KA,PA not come
'''Find  outputs (Home  work)'''
# class  c1:
# 	def  __init__(self):
# 		print('c1  class constructor')
# 		return  25
# class  c2:
# 	def  __init__(self):
# 		print('c2  class  constructor')
# 		return  None
# class  c3:
# 	def  __init__(self):
# 		print('c3  class  constructor')
# # End  of  class
# a = c1() #Error--it cannot return other than None 
# b = c2()  # c2  class  constructor
# print(b) # Type and address
# print(b . __init__())# c2  class  constructor  <nxtline>  None
# c = c3() # c3  class  constructor
# print(c . __init__()) # c3  class  constructor  <nxtline>  None
'''Find  outputs (Home  work)'''
# class  c1:
# 	def  __init__(self):
# 		print('Constructor')
# 		b = c1() # infinite Constructor
# # End  of  class
# a = c1() #Constructor
'''Difference  between  init()    and  _init_()   methods (Home  work)'''
# class c1:
#     def  __init__(self):
#         print('Constructor')
#         self . x = 10
#         self . y = 20
# class c2:
#     def  init(self):
#         print('Method')
#         self . x = 30
#         self . y = 40
# a = c1()
# print(a . __dict__) #Constructor <nxtline> {'x':10,'y':20}
# b = c2()
# print(b . __dict__) #{}
# b . init()
# print(b . __dict__)# Method <nextline> {'x':30,'y':40}
'''Find  outputs (Home  work)'''
# class   c1:
#         def   __init__(self):
#                 self . a = 10
#         def   m1(self):
#                 self . b = 20
# #End  of  class  c1
# class   c2:
#         def  m3(self):
#                 x . e = 50
# # End  of  class  c2
# def   f1():
#         x . c = 30
# #  End  of  function  f1
# x = c1() 
# print(x . __dict__)#{'a':10}
# x . m1()
# print(x . __dict__)# {'a': 10, 'b': 20}
# f1()
# print(x . __dict__)# {'a': 10, 'b': 20, 'c': 30}
# x . d = 40
# print(x . __dict__)# {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# y = c2()
# y . m3()
# print(x . __dict__) #{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
# z = c1()
# print(z . __dict__)# {'a': 10}
''''Find  outputs  (Home  work)'''
# class   c1:
# 	def   __init__(self):
# 		self . x = 10
# 		self . y = 20
# 		self . z = 30
# #end  of  the  class
# a = c1()
# b = c1()
# print(a . __dict__) # {'x' : 10 ,'y' :20 , 'z' : 30 }
# print(b . __dict__) # {'x' : 10 ,'y' :20 , 'z' : 30 }
# del  a . x
# del  b . y
# print(a . __dict__)# {'y' :20 , 'z' : 30 }
# print(b . __dict__)# {'x' : 10 ,'y' :20 , 'z' : 30 }
# print(a . x) #Errror---already we delete
# print(b . y) #Error---already we delete
'''Find  outputs (Home  work)'''
# class   c1:
# 	def  __init__(self):
# 		print('1st  constructor') #Discarded
# 	def  __init__(self):
# 		print('2nd  constructor') #discarded
# 	def  __init__(self):
# 		print('3rd  constructor') # 3rd  constructor
# # End  of  the  class
# a = c1()
'''Find  outputs  (Home  work)'''
# class   c1:
# 	def  __init__(self): 
# 		print('No  argument  constructor') # Discarded
# 	def  __init__(self , x):
# 		print('single  argument  constructor : ' , x) # Discarded
# 	def  __init__(self , x , y):
# 		print('Two  argument  constructor : ' , x , y) # recognized
# # End  of  the  class
# a = c1(10 , 20) #Two  argument  constructor : 10 20
# b = c1(30) #Error--missing 1 argument
# c = c1() # Error--missing 2 
'''Find  outputs'''
# class   c1:
# 	def  __init__(self):
# 		print('No  argument  constructor') # Discarded
# 	def  __init__(self , x):
# 		print('single  argument  constructor : ' , x) # Discarded
# 	def  __init__(self , x = 100 , y = 200):
# 		print('Two  argument  constructor : ' , x , y) # Recognized
# # End  of  the  class
# a = c1(10 , 20) # Two  argument  constructor : 10  20
# b = c1(30) # Two  argument  constructor : 30  200
# c = c1() # Two  argument  constructor : 100  200
'''What  happens  when  function  and  class  have  same  name ?'''
# def   f1(): # Discarded
# 	print('Function')
# 	return  25
# class   f1:
# 	def  __init__(self): #Recognizes
# 		print('Constructor')
# # End  of  the  class
# a = f1()
# print(a) #Constructor
'''Find  outputs (Home  work)'''
# class    c1: # Discarded
# 	def   __init__(self):
# 		print('Constructor')
# def  c1(): #Recognized
# 	print('Function')
# #end of the  class
# a = c1()
# print(a)  # Function <nextline> None
'''Find outputs  (Home  work)'''
# class    c1: # Discarded
#         def  __init__(self):
#                 print('Constructor')
# def    c1(x): # Recognized
#         print('Function : ' , x)
# # End  of  class  c1
# a = c1()#Error---missing 1 argument
# b = c1(25)
# print(b) #Function :  25  <nextline> None






# #  Save  the  program  in  prog9a.py  file
# class   c1:
# 	def  _init_(self):
# 		print('c1  class  of  prog9a')
# #  Find  outputs (Home  work)
# from  prog9a  import  c1
# class   c1:
# 	def  _init_(self):
# 		print('c1  class  of  prog9b')
# a = c1()
# #  Find  outputs (Home  work)
# class   c1:
# 	def  _init_(self):
# 		print('c1  class  of  prog9c')
# from  prog9a  import  c1
# a = c1()
# #  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
# How  to  import  class  c1  from  prog9a
# class   c1:
# 	def  _init_(self):
# 		print('c1  class  of  prog9d')
# How  to  create  c1  class  object  of  current  module
# How  to  create  c1  class  object  of  prog9a
# '''
# How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
# '''
# How  to  import  prog9a
# class   c1:
# 	def  _init_(self):
# 		print('c1  class  of  prog9e')
# How  to  create  c1  class  object  of  current  module
# How  to  create  c1  class  object  of  prog9a





 


