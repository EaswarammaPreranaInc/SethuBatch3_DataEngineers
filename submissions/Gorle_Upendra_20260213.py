a = range(10 , 50 , 5)
print(type(a))  # <class 'range'>
print(a)        # range(10, 50, 5)
print(*a)       # 10 15 20 25 30 35 40 45
print(id(a))    # some address, we can't predict exact number, we can say something like 140123456789 (or just <address>)
print(len(a))   # 8
print(*a[2 : 7] , sep = ' , ')  # 20 , 25 , 30 , 35 , 40  (since a[2:7] gives indices 2,3,4,5,6: 20,25,30,35,40)
print(*a[ : : -1])  # 45 40 35 30 25 20 15 10
a[4] = 32        # TypeError: 'range' object does not support item assignment
print(a * 2)     # TypeError: unsupported operand type(s) for *: 'range' and 'int' (or something like that)