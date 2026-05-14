# Save the program in prog9a.py file
class  c1:
	def  _init_(self):
		print('c1  class  of  prog9a')



#1
class  Rat:
	def   _init_(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   _str_(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat()
b = Rat(9)
c = Rat(5,  8)
d = Rat(dr1 = 9)
e = Rat(dr1 = 3 , nr1 = 2)
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y)
print('a  :  ' , a)   # a  :   22 / 7
print('b  :  ' , b)   # b  :   9 / 7
print('c  :  ' , c)   # c  :   5 / 8
print('d  :  ' , d)   # d  :   22 / 9
print('e  :  ' , e)   # e  :   2 / 3
print('f  :  ' , f)   # f  :   11 / 15
c . _init_()
print('c  :  ' , c)   # c  :   /   (uses default 22/7, but still valid call)
a . _init_(3.8  , 4.6)
print('a  :  ' , a)   # a  :   3.8 / 4.6
# g = Rat(nr1 = 9 , 5) # Error as positional argument follows keyword argument
# h = Rat(nr = 9 , dr = 5) # Error as Rat.__init__() got an unexpected keyword argument 'nr'



#2
class  Date:
        def   _init_(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a . _dict_)  # a  :   {'dd': 15, 'mm': 8, 'yy': 1947}
print('b  :  ' , b . _dict_)  # b  :   {'dd': 26, 'mm': 1, 'yy': 1950}
print('c  :  ' , c . _dict_)  # c  :   {'dd': 19, 'mm': 7, 'yy': 1985}
# d = Date() # Error as Date.__init__() missing 3 required positional arguments: 'dd1', 'mm1', 'yy1'
# e = Date(dd = 30 , mm = 4 , yy = 2022) # Error as Date.__init__() got an unexpected keyword arguments 'dd', 'mm', 'yy'
# f = Date(dd1 = 26 , mm1 = 8 , 2023) # Error as positional argument follows keyword argument