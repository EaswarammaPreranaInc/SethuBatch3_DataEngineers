1) outputs 
def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a)
a += 1
f1()
print(a)#10
	 20
	 11


2) outputs  
def   f1():
	a = 20
	print(a)
	dict = globals()
	print(dict['a'])
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a)
a += 1
f1()
print(a)#10
	 20
	 40
	 11

3) outputs 
x = 10
def   f1():
	print(x)
	print(globals()['x'])
# end of the function
f1()#10
     10

4) outputs
def  f1():
	x = 20
	print(x)#20
	print(globals()['x'])#Error because it is not permitted
# End  of  the  function
f1()

5) outputs 
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)#40 50 60
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c'])#100 200 300
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c)#10 20 30
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()

6) global  keyword  demo  program
def    f1():
	x = 20
	print(x)#20
def   f2():
	global  x
	x = 30
	print(x)#30
	x += 1#31
def   f3():
	global  y
	y = 40
	print(y)#40
	y += 1
def   f4():
	x = 50
	global   x#Error because it is not permitted
#  End  of  the  functions
x = 10
print(x)#10
x += 1
f1()
print(x)#11
f2()
print(x)#31
x += 1
f3()
print(y)#41
f4()
print(x)

7) outputs 
def  f1():
	global  a
	a = 20
	print(a)
	print(globals()['a'])
	a = 30
# End of the function
a = 10
print(a)#10
f1()
print(a)#20
         20
         30

8) outputs
def  f1():
	global  a 
	print(a)
	a = 10
	print(globals()['a'])
	a = 20
	print(a)
	a = 30
def  f2():
	print(a)
# End  of   f2   function
f1()
f2()
print(a)#Error because it is not valid

9) outputs 
def  f1():
	global   a
	a = 10
	print(a)
	a = 20
def  f2():
	global  a
	print(a)
	a = 30
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a)#10
	 20
	 30
	 40

10) outputs 
def  f1():
	global   a
	a = 10
	print(a)
	a = 20
def  f2():
	print(a)#Error because it is not valid
	a = 30
	print(a)
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a)#10

11) outputs 
def  f1():
        a = 10
        global  a #Error because it is not valid
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1()
print(a)
print(b)

12) outputs 
def  f1():
        global  a
        print(a)
        a += 1
def  f2():
        global  a
        print(a)
        a += 1
# End  of  the  function
a = 10
print(a)
a += 1
f1()
print(a)
a += 1
f2()
print(a)#10
	 11
	 12
	 13
	 14

13) outputs 
def   f1():
	a = 20
	print(a)#20
def  f2():
	print(a)
	a += 1
# End of the function
a = 10
print(a)#10
f1()
a += 1
f2()
print(a)#Error because it is not valid

14) outputs
def  f1():
	a = 20
	global   a #Error because it is not permitted 
	print(a)
	print(globals()['a'])
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a)#10
a += 1#11
f1()
print(a)#20
	 40

15)  outputs
def   f1():
	x = x + 5
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)
# End of f2  function
x = 10
f1()
f2()
print(x)#Error because it is not permitted

16) outputs
a = 10
def   f1():
	b = 40
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
# End  of  f2()  function
c = 30
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print()
a +=  1
b +=  1
c +=  1
f1()# a: 10
      b: 20
      c: 30

      a: 11
      b: 40
      c: 31
a +=  1
b +=  1
c +=  1
f2()
print('Bye')#a: 50
             b: 22
	     c: 32
             Bye
