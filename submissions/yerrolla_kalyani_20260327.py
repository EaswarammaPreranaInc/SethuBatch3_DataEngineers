#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a)#a : <space> 11
	print('b : ' , b)#b : <space> 20
	print('c : ' , c)#c : <space> 21
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)# 50
	print('b : ' , b)# 22
	print('c : ' , c)# 32
# End  of  f2()  function
c = 30
print('a : ' , a)# 10
print('b : ' , b)# 20
print('c : ' , c)# 30
print()#noting is printed
a +=  1#11
b +=  1#21
c +=  1#31
f1()# 11 <next line>  20 <next line>   31
a +=  1#12
b +=  1#22
c +=  1#32
f2()#  50 <next line>  22 <next line>   32
print('Bye')#Bye



# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a)#10
a += 1
f1()#20
print(a)#11

# Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a)
	dict = globals()
	print(dict['a'])
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a)#10
# a += #error int value is missing after =
f1()#20<next line>10
print(a)#40

#Find  outputs (Home  work)
x = 10
def   f1():
	print(x)
	print(globals()['x'])
# end of the function
f1()#10<next line> 10


#Find  outputs (Home  work)
def  f1():
	x = 20
	print(x)#20
	print(globals()['x'])#error, because no GV x
# End  of  the  function
f1()#20<nextline> error, because no GV x

#Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)#40<space>50<space>60
	dict = globals()#{'a':10,'b':20,'c':30}
	print(dict['a'] , dict['b'] , dict['c'])#10 <space>20 <space>30
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c)#100<space>200<space>300
# End  of  f2  function
a = 10
b = 20
c = 30
f1()#40<space>50<space>60  <next line> 10 <space>20 <space>30
f2()#100<space>200<space>300



#global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x)#20
def   f2():
	global  x
	x = 30
	print(x)#30
	x += 1
def   f3():
	global  y
	y = 40
	print(y)#40
	y += 1
def   f4():
	x = 50
	# global   x #  no use of global keyword after creating the local x 
#  End  of  the  functions
x = 10
print(x)#10
x += 1
f1()#20
print(x)#11
f2()#30
print(x)#31
x += 1
f3()#40
print(y)#41
f4()
print(x)#32




#Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a)#20
	print(globals()['a'])#20
	a = 30
# End of the function
a = 10
print(a)#10
f1()#20<nextline> 20
print(a)#30



# Find  outputs(Home  work)
def  f1():
	global  a
	print(a)
	a = 10
	print(globals()['a'])#10
	a = 20
	print(a)#20
	a = 30
def  f2():
	print(a)#30
# End  of   f2   function
f1()#10<nxt line>20 
f2()#30
print(a)#30



#Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)#10
	a = 20
def  f2():
	global  a
	print(a)
	a = 30
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1()#10
f2()#20
f3()#30
print(a)#40



# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)#10
	a = 20
def  f2():
	print(a)#error as a is only for that funtion f1()  but not other functions cannot use them.
	a = 30
	print(a)#30
def  f3():
	print(a)#30
	globals()['a'] = 40
# End  of  the  function
f1()#10
f2()#30
f3()#30
print(a)#40



 #Find  outputs (Home  work)
def  f1():
        a = 10
        global  a#error keyword global after the a =10
        print(a)#10
        global  b
        b = 20
# End  of  f1()  function
f1()# 10 <next line> 20
print(a)#error 
print(b)#20


#Find outputs (Home  work)
def  f1():
        global  a
        print(a)#10 
        a += 1
def  f2():
        global  a
        print(a)#10
        a += 1
# End  of  the  function
a = 10
print(a)#10
a += 1
f1()#11
print(a)#12
a += 1
f2()#13
print(a)#13




#Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)#20
def  f2():
	print(a)#10
	a += 1
# End of the function
a = 10
print(a)#10
f1()#20
a += 1
f2()#10
print(a)#11


#Find outputs (Home  work)
def  f1():
	a = 20
	global   a #error
	print(a)
	print(globals()['a'])
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a)#10
a += 1
f1()#error
print(a)#11



 #Find   outputs
def   f1():
	x = x + 5
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)
# End of f2  function
x = 10
f1()#15
f2()#15
print(x)#10







