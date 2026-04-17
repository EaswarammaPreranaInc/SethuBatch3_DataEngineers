#Find outputs (Home work)
a = 10
def f1():
    b = 40
    print('a : ' , a)   # a : 11
    print('b : ' , b)   # b : 40
    print('c : ' , c)   # c : 31
    print()             # (blank line)
b = 20
def f2():
    a = 50
    print('a : ' , a)   # a : 50
    print('b : ' , b)   # b : 22
    print('c : ' , c)   # c : 32
c = 30
print('a : ' , a)   # a : 10
print('b : ' , b)   # b : 20
print('c : ' , c)   # c : 30
print()             # (blank line)
a += 1
b += 1
c += 1
f1()
a += 1
b += 1
c += 1
f2()
print('Bye')        # Bye



def f1():
    a = 20
    print(a)   # 20
    a += 1
a = 10
print(a)       # 10
a += 1         # a = 11
f1()
print(a)       # 11



def f1():
    a = 20
    print(a)            # 20
    dict = globals()
    print(dict['a'])    # 11
    a = 30
    dict['a'] = 40
a = 10
print(a)                # 10
a += 1                  # a = 11
f1()
print(a)                # 40


x = 10
def f1():
    print(x)              # 10
    print(globals()['x']) # 10
f1()


def f1():
    x = 20
    print(x)              # 20
    print(globals()['x']) # Error (no global variable 'x')
f1()



def f1():
    a = 40
    b = 50
    c = 60
    print(a , b , c)                 # 40 50 60
    dict = globals()
    print(dict['a'] , dict['b'] , dict['c'])   # 10 20 30
    dict['a'] = 100
    dict['b'] = 200
    dict['c'] = 300
def f2():
    print(a , b , c)                 # 100 200 300
a = 10
b = 20
c = 30
f1()
f2()



def f1():
    x = 20
    print(x)        # 20
def f2():
    global x
    x = 30
    print(x)        # 30
    x += 1          # x = 31
def f3():
    global y
    y = 40
    print(y)        # 40
    y += 1          # y = 41
def f4():
    x = 50
    global x        # SyntaxError (global after assignment not allowed)
x = 10
print(x)            # 10
x += 1              # x = 11
f1()
print(x)            # 11
f2()
print(x)            # 31
x += 1              # x = 32
f3()
print(y)            # 41
f4()                # SyntaxError occurs here (program stops)
print(x)            # Not executed


def f1():
    global a
    a = 20
    print(a)              # 20
    print(globals()['a']) # 20
    a = 30                # global a becomes 30
a = 10
print(a)                  # 10
f1()
print(a)                  # 30


def f1():
    global a
    print(a)              # NameError (global 'a' not defined yet)
    a = 10
    print(globals()['a']) # 10
    a = 20
    print(a)              # 20
    a = 30                # a = 30
def f2():
    print(a)              # 30
# End  of   f2   function
f1()
f2()
print(a)                  # 30


def f1():
    global a
    a = 10
    print(a)        # 10
    a = 20          # global a = 20
def f2():
    global a
    print(a)        # 20
    a = 30          # global a = 30
def f3():
    print(a)        # 30
    globals()['a'] = 40  # global a = 40
#End of f2 function
f1()
f2()
f3()
print(a)            # 40


def f1():
    global a
    a = 10
    print(a)        # 10
    a = 20          # global a = 20
def f2():
    print(a)        # 20
    a = 30          # UnboundLocalError occurs here
    print(a)        # Not executed due to error
def f3():
    print(a)        # Not executed if error occurs in f2()
    globals()['a'] = 40  # Not executed
# End of the function
f1()
f2()                 # Error occurs here: UnboundLocalError
f3()                 # Not executed
print(a)             # Not executed



def f1():
    a = 10
    global a          # Error: name 'a' is assigned before global declaration
    print(a)
    global b
    b = 20
# End of f1() function
f1()
print(a)
print(b)


def f1():
    global a
    print(a)        # 11
    a += 1          # a = 12
def f2():
    global a
    print(a)        # 13
    a += 1          # a = 14
# End of the function
a = 10
print(a)            # 10
a += 1              # a = 11
f1()
print(a)            # 12
a += 1              # a = 13
f2()
print(a)            # 14


def f1():
    a = 20
    print(a)        # 20
def f2():
    print(a)        # Error
    a += 1          # Not executed due to error
# End of the function
a = 10
print(a)            # 10
f1()
a += 1              # a = 11
f2()                # Error occurs here
print(a)            # Not executed



def f1():
    a = 20
    global a          # Error due to name 'a' is assigned to before global declaration
    print(a)
    print(globals()['a'])
    a = 30
    globals()['a'] = 40
# End of f1() function
a = 10
print(a)                # 10
a += 1                  # a = 11
f1()                    # Error occurs here
print(a)                # Not executed



def f1():
    x = x + 5       # Error due to local variable 'x' referenced before assignment
# End of f1 function
def f2():
    x = globals()['x'] + 5
    print(x)        # 15
# End of f2 function
x = 10
f1()                # Error occurs here
f2()                # Not executed due to error in f1()
print(x)            # Not executed