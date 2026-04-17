#Find outputs
def f1():
    a = 3              
    if a:              
        print(a)       # 3
        a = a - 1      # Local 'a' becomes 2
        f1()           # Error due maximum recursion depth will be exceeded
        print('Hello') 
        print('Hi')
        print(a)
    print('Bye')
#End of the function
a = 3                  # This is a Global 'a', but f1() ignores it because of the local 'a = 3'
f1()
print('End')