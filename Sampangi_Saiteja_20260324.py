# Modify program so every function is executed

def f1():
    print('No-argument function')

def f2(x):
    print('Single argument function : ', x)

def f3(x , y):
    print('Two argument function : ', x , y)

def f4(x , y , z):
    print('Three argument function : ', x , y , z)


f1()             # No-argument function
f2(10)           # Single argument function :  10
f3(10 , 20)      # Two argument function :  10 20
f4(10 , 20 , 30) # Three argument function :  10 20 30