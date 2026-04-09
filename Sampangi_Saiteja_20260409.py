# Find  outputs
class Rat:
    def _init_(self , nr1 = 22, dr1 = 7):   # not recognized as constructor
        self.nr = nr1
        self.dr = dr1
    def _str_(self):                        # not recognized as string method
        return f'{self.nr} / {self.dr}'
# end of the class

a = Rat()                                   # object created
b = Rat(9)                                  #  error
c = Rat(5, 8)                               #  error
d = Rat(dr1 = 9)                            # error
e = Rat(dr1 = 3 , nr1 = 2)                  # error

x = eval(input('Enter numerator  :  '))     # input = 11
y = eval(input('Enter Denominator  :  '))   # input = 15
f = Rat(x , y)                              # has error

print('a  :  ' , a)                         # a  :  <__main__.Rat object at 0x...>
print('b  :  ' , b)                         # error
print('c  :  ' , c)                         # error
print('d  :  ' , d)                         # error
print('e  :  ' , e)                         # error
print('f  :  ' , f)                         #  error

c._init_()                                  #  error
print('c  :  ' , c)                         #  error

a._init_(3.8 , 4.6)                         # executed, sets nr=3.8, dr=4.6
print('a  :  ' , a)                         # a  :  <__main__.Rat object at 0x...>

g = Rat(nr1 = 9 , 5)                        #  error
h = Rat(nr = 9 , dr = 5)                    #  error


#find out put
class Date:
        def _init_(self , dd1 , mm1 , yy1):   # not recognized as constructor
                self.dd = dd1
                self.mm = mm1
                self.yy = yy1
# End of the class

a = Date(15 , 8 , 1947)                      # error
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)    # error
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)    # error

print('a  :  ' , a._dict_)                   # error
print('b  :  ' , b._dict_)                   # error
print('c  :  ' , c._dict_)                   # error

d = Date()                                   # error
e = Date(dd = 30 , mm = 4 , yy = 2022)       # error
f = Date(dd1 = 26 , mm1 = 8 , 2023)          # error

Object 'a' ---> error
Object 'b' ---> error
Object 'c' ---> error


class c1:
    def _init_(self):
        print('c1  class constructor')
        return 25

class c2:
    def _init_(self):
        print('c2  class  constructor')
        return None

class c3:
    def _init_(self):
        print('c3  class  constructor')
# End of class

a = c1()                     # error (constructor not recognized)
b = c2()                     # error (constructor not recognized)

print(b)                     # error (b not created)
print(b._init_())            # error (b not created)

c = c3()                     # error (constructor not recognized)
print(c._init_())            # c3  class  constructor
                             # None



#find out put
class c1:
    def _init_(self):
        print('Constructor')
        b = c1()
# End of class

a = c1()                     # error


#find output
class c1:
    def _init_(self):
        print('Constructor')
        self.x = 10
        self.y = 20

class c2:
    def init(self):
        print('Method')
        self.x = 30
        self.y = 40

a = c1()                     # error (constructor not recognized)
print(a._dict_)              # error (a not created)

b = c2()                     # object created
print(b._dict_)              # {}   (empty dictionary, no attributes yet)

b.init()                     # Method
print(b._dict_)              # {'x': 30, 'y': 40}

#find out put
class c1:
        def _init_(self):
                self.a = 10
        def m1(self):
                self.b = 20
# End of class c1

class c2:
        def m3(self):
                x.e = 50
# End of class c2

def f1():
        x.c = 30
# End of function f1

x = c1()                     # object created (constructor not recognized, so no attributes set)
print(x._dict_)              # {}   (empty dictionary)

x.m1()                       # adds b = 20
print(x._dict_)              # {'b': 20}

f1()                         # adds c = 30
print(x._dict_)              # {'b': 20, 'c': 30}

x.d = 40                     # adds d = 40
print(x._dict_)              # {'b': 20, 'c': 30, 'd': 40}

y = c2()                     # object created
y.m3()                       # adds e = 50 to x
print(x._dict_)              # {'b': 20, 'c': 30, 'd': 40, 'e': 50}

z = c1()                     # object created (constructor not recognized, so no attributes set)
print(z._dict_)              # {}
object 'x' ---> {'b': 20, 'c': 30, 'd': 40, 'e': 50}
object 'z' ---> {}
object 'y' ---> {}

#findoutput
class c1:
    def _init_(self):
        self.x = 10
        self.y = 20
        self.z = 30
# end of the class

a = c1()                     # object created (constructor not recognized, so no attributes set)
b = c1()                     # object created (constructor not recognized, so no attributes set)

print(a._dict_)              # {}   (empty dictionary)
print(b._dict_)              # {}   (empty dictionary)

del a.x                      # error (attribute x does not exist)
del b.y                      # error (attribute y does not exist)

print(a._dict_)              # {}   (still empty)
print(b._dict_)              # {}   (still empty)

print(a.x)                   # error (x not defined)
print(b.y)                   # error (y not defined)
Object 'a' ---> {}
Object 'b' ---> {}

#findoutput
class c1:
    def _init_(self):
        print('1st  constructor')
    def _init_(self):
        print('2nd  constructor')
    def _init_(self):
        print('3rd  constructor')
# End of the class

a = c1()                     # error (constructor not recognized)

#find output
class c1:
    def _init_(self):
        print('No  argument  constructor')
    def _init_(self , x):
        print('single  argument  constructor : ' , x)
    def _init_(self , x , y):
        print('Two  argument  constructor : ' , x , y)
# End of the class

a = c1(10 , 20)               # error (constructor not recognized)
b = c1(30)                    # error (constructor not recognized)
c = c1()                      # error (constructor not recognized)

#find out put

def f1():
    print('Function')
    return 25

class f1:
    def _init_(self):
        print('Constructor')
# End of the class

a = f1()                     # error (constructor not recognized)
print(a)                     # error (a not created)
#find out put
class c1:
    def _init_(self):
        print('Constructor')

def c1():
    print('Function')
# end of the class

a = c1()                     # Function
print(a)                     # None

#find output
class c1:
    def _init_(self):
        print('Constructor')

def c1(x):
    print('Function : ', x)
# End of class c1

a = c1()                     # error (function requires 1 argument, none given)
b = c1(25)                   # Function :  25
print(b)                     # None

#find output
# prog9a.py
class c1:
    def _init_(self):
        print('c1  class  of  prog9a')
#find out put
from prog9a import c1
class c1:
    def _init_(self):
        print('c1  class  of  prog9b')

a = c1()                     # error (constructor not recognized)

#find output
class c1:
    def _init_(self):
        print('c1  class  of  prog9c')

from prog9a import c1
a = c1()                     # error (constructor not recognized)


#find out put
from prog9a import c1 as c1_prog9a   # import prog9a’s class with alias
class c1:
    def __init__(self):              # corrected constructor
        print('c1  class  of  prog9d')

# create object of current module’s class
obj_current = c1()                   # prints: c1  class  of  prog9d

# create object of prog9a’s class
obj_prog9a = c1_prog9a()             # prints: c1  class  of  prog9a
  

#find output
# Import prog9a’s class with an alias
from prog9a import c1 as c1_prog9a

# Define another class c1 in the current module
class c1:
    def __init__(self):
        print('c1 class of prog9e')

# Create object of current module’s class
obj_current = c1()           # c1 class of prog9e

# Create object of prog9a’s class
obj_prog9a = c1_prog9a()     # c1 class of prog9a




