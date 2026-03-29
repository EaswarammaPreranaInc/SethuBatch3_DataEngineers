#1
#Find outputs (Home work)
a = 10
def f1():
    b = 40 # Local b
    print('a : ', a) # a : 11
    print('b : ', b) # b : 40
    print('c : ', c) # c : 31
    print()

b = 20 # Global b
def f2():
    a = 50 # Local a
    print('a : ', a) # a : 50
    print('b : ', b) # b : 22 (Uses global b)
    print('c : ', c) # c : 33 (Uses global c)

c = 30
print('a : ', a) # a : 10
print('b : ', b) # b : 20
print('c : ', c) # c : 30
print()

a += 1 # Global a becomes 11
b += 1 # Global b becomes 21
c += 1 # Global c becomes 31
f1()

a += 1 # Global a becomes 12
b += 1 # Global b becomes 22
c += 1 # Global c becomes 32 (Note: b & c continue to increment)
f2()
print('Bye') # Bye



#2
#Find outputs (Home work)
def f1():
    a = 20
    print(a) # 20
    a += 1
# End
a = 10
print(a) # 10
a += 1
f1()
print(a) # 11 (Global 'a' was not affected by f1)



#3
#Find outputs (Home work)
def f1():
    a = 20
    print(a) # 20
    dict = globals()
    print(dict['a']) # 11
    a = 30
    dict['a'] = 40 # Changes the global 'a'
# End
a = 10
print(a) # 10
a += 1
f1()
print(a) # 40



#4
#Find outputs (Home work)
x = 10
def f1():
    print(x) # 10
    print(globals()['x']) # 10
f1()



#5
#Find outputs (Home work)
def f1():
    x = 20
    print(x) # 20
    # Assuming x = 10 exists globally from previous context
    # print(globals()['x']) # 10 (or Error if 'x' not defined globally)
f1()



#6
#Find outputs (Home work)
def f1():
    a, b, c = 40, 50, 60
    print(a, b, c) # 40 50 60
    dict = globals()
    print(dict['a'], dict['b'], dict['c']) # 10 20 30
    dict['a'], dict['b'], dict['c'] = 100, 200, 300
def f2():
    print(a, b, c) # 100 200 300
a, b, c = 10, 20, 30
f1()
f2()



#7
#Find outputs (Home work)
def f1():
    x = 20
    print(x) # 20
def f2():
    global x
    x = 30
    print(x) # 30
    x += 1
def f3():
    global y
    y = 40
    print(y) # 40
    y += 1
def f4():
    # global x # Moving this to top for clarity
    # x = 50 
    # Error as name 'x' is assigned to before global declaration
    pass 

x = 10
print(x) # 10
x += 1 # 11
f1()
print(x) # 11
f2()
print(x) # 31
x += 1 # 32
f3()
print(y) # 41
# f4() # Error as global declaration must come before local use



#8
#Find outputs (Home work)
def f1():
    global a
    a = 20
    print(a) # 20
    print(globals()['a']) # 20
    a = 30
a = 10
print(a) # 10
f1()
print(a) # 30



#9
#Find outputs (Home work)
def f1():
    global a
    # print(a) # Error if f1 called before 'a' is defined
    a = 10
    print(globals()['a']) # 10
    a = 20
    print(a) # 20
    a = 30
def f2():
    print(a) # 30
f1()
f2()
print(a) # 30



#10
#Find outputs (Home work)
def f1():
    global a
    a = 10
    print(a) # 10
    a = 20
def f2():
    global a
    print(a) # 20
    a = 30
def f3():
    print(a) # 30
    globals()['a'] = 40
f1()
f2()
f3()
print(a) # 40



#11
#Find outputs (Home work)
def f1():
    global a
    a = 10
    print(a) # 10
    a = 20
def f2():
    # print(a) # Error as local variable 'a' referenced before assignment
    # Because 'a = 30' exists in this scope, Python treats 'a' as local.
    a = 30
    print(a)
f1()
# f2() # Error as cannot print 'a' locally before assigning it if assignment exists later in function.



#12
#Find outputs (Home work)
def f1():
    # a = 10
    # global a # Error as name 'a' is assigned to before global declaration
    global b
    b = 20
# f1() # Error as illegal sequence of local assignment and global declaration.



#13
#Find outputs (Home work)
def f1():
    global a
    print(a) # 11
    a += 1
def f2():
    global a
    print(a) # 13
    a += 1
a = 10
print(a) # 10
a += 1
f1()
print(a) # 12
a += 1
f2()
print(a) # 14



#14
#Find outputs (Home work)
def f1():
    a = 20
    print(a) # 20
def f2():
    # print(a) # Error as local variable 'a' referenced before assignment
    a = 1 # Added to show why error happens (a += 1 is an assignment)
    a += 1 
a = 10
print(a) # 10
f1()
a += 1
# f2() # Error as in f2, 'a += 1' makes 'a' local, so 'print(a)' fails before initialization.



#15
#Find outputs (Home work)
def f1():
    # a = 20
    # global a # Error as name 'a' is assigned to before global declaration
    pass
# f1() # Error as same as #12.



#16
#Find outputs (Home work)
def f1():
    # x = x + 5 # Error as local variable 'x' referenced before assignment
    pass
def f2():
    x = globals()['x'] + 5 # Takes global 10, adds 5 to a local x
    print(x) # 15
x = 10
# f1() # Error as cannot use 'x' to define 'x' locally without global keyword.
f2()
print(x) # 10