'''
1) def f1():
    a = 3
    if a:
        print(a)  3 <nextline> 3 <nextline> 3 <nextline> ... and error because in if condition when we are calling f1() again the value is becoming 3 and if condition is         #                 becoming True every time so it throws error as it runs an infinite loop
        a = a - 1
        f1()
        print('Hello')
        print('Hi')
        print(a)
    print('Bye')
# End of the function

a = 3
f1()
print('End')
'''