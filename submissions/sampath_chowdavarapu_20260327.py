#Find  outputs (Home  work)
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
a +=  1             #a:10
b +=  1             #b:20
c +=  1             #c:30
f1()                #a:11
a +=  1             #b:40
b +=  1             #c:31
c +=  1             #a:50
f2()                #b:22
print('Bye')        #c:32
                    #Bye
-----------------------------------------------------
# Find  outputs (Home  work)
def   f1():                  #10
	a = 20             
	print(a)             #20
	a += 1               #11
#End  of  the  function
a = 10
print(a)
a += 1
f1()
print(a)
-------------------------------------------------------
# Find  outputs  (Home  work)
def   f1():                      #10
	a = 20                   #20
	print(a)                 #11
	dict = globals()         #40
	print(dict['a'])
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a)
a += 1
f1()
print(a)
----------------------------------------------------------
# Find  outputs (Home  work)           #10
x = 10                                 #10
def   f1():                            
	print(x)                     
	print(globals()['x'])
# end of the function
f1()
-----------------------------------------------------------
# Find  outputs (Home  work)         #20
def  f1():                           #error
	x = 20
	print(x)
	print(globals()['x'])
# End  of  the  function
f1()
-----------------------------------------------------------
# Find outputs (Home  work)        #40 50 60
def  f1():                         #10 20 30
	a = 40                     #100 200 300
	b = 50
	c = 60
	print(a , b , c)
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c'])
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c)
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()
----------------------------------------------------
# global  keyword  demo  program (Home  work)
def    f1():                #10
	x = 20              #20
	print(x)            #11
def   f2():                 #30
	global  x           #31
	x = 30              #40
	print(x)            #41
	x += 1              #error
def   f3():                 
	global  y
	y = 40
	print(y)
	y += 1
def   f4():
	x = 50
	global   x
#  End  of  the  functions
x = 10
print(x)
x += 1
f1()
print(x)
f2()
print(x)
x += 1
f3()
print(y)
f4()
print(x)
---------------------------------------------------
# Find outputs (Home  work)
def  f1():                  #10
	global  a           #20
	a = 20              #20
	print(a)            #30
	print(globals()['a'])  #error
	a = 30               
# End of the function
a = 10
print(a)
f1()
print(a)
# Find  outputs(Home  work)
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
print(a)
----------------------------------------------------------
# Find outputs (Home  work)
def  f1():                    #10
	global   a            #20
	a = 10                #30
	print(a)              #40
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
print(a)
-------------------------------------------------------------
# Find outputs (Home  work)
def  f1():                        #10
	global   a                #20
	a = 10                    #30
	print(a)                  #30           
	a = 20                    #40
def  f2():
	print(a)
	a = 30
	print(a)
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a)
----------------------------------------------
#  Find  outputs (Home  work)
def  f1():                   #error
        a = 10               
        global  a            #20
        print(a)
        global  b
        b = 20
# End  of  f1()  function
f1()
print(a)
print(b)
----------------------------------------------
# Find outputs (Home  work)
def  f1():              #10
        global  a       #11
        print(a)        #12
        a += 1          #13
def  f2():              #14
        global  a
        print(a)
        a += 1
# End  of  the  function
a = 10
print(a)
a += 1--->11
f1()
print(a)
a += 1-->13
f2()
print(a)
-----------------------------------------------
#Find  outputs (Home  work)
def   f1():                 #10
	a = 20              #20
	print(a)            #error   
                            #11
def  f2():
	print(a)#error
	a += 1
# End of the function
a = 10
print(a)
f1()
a += 1-->11
f2()
print(a)
-----------------------------------------------
# Find outputs (Home  work)
def  f1():                       #10
	a = 20                   #error
	global   a               #error
	print(a)                 #error
	print(globals()['a'])
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a)
a += 1-->11
f1()
print(a)
----------------------------------------------
#  Find   outputs
def   f1():                         #error
	x = x + 5-->15              
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x)
# End of f2  function
x = 10
f1()
f2()
print(x)