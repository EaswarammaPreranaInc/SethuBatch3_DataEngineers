#  Find  outputs
a = 25
print(id(a))        # some_memory_address1
a = 35
print(id(a))        # some_memory_address2 (different from above)


# Find  outputs (Home  work)
a = 25.7
print(id(a))        # some_memory_address3
print(a)            # 25.7
a = 35.6
print(id(a))        # some_memory_address4 (different from above)
print(a)            # 35.6
b = True
print(id(b))        # some_memory_address_of_True
b = False
print(id(b))        # some_memory_address_of_False
c = None
print(id(c))        # same_memory_address_of_None
c = None
print(id(c))        # same_memory_address_of_None (same as above)


#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))        # some_memory_address5
a[1] = 'e'          # TypeError: 'str' object does not support item assignment
a = 'Sec'
print(id(a))        # some_memory_address6 (different from above)
b = (10 , 20 , 15 , 18)
print(id(b))        # some_memory_address7
b[2] = 19           # TypeError: 'tuple' object does not support item assignment
b = (30 , 40 , 35 , 32)
print(id(b))        # some_memory_address8 (different from above)
c = range(5)
print(id(c))        # some_memory_address9
c[3] = 10           # TypeError: 'range' object does not support item assignment
c = range(5)
print(id(c))        # some_memory_address10 (different from above)


# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)     # True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)     # True
e = False
f = False
print(e  is  f)     # True
g = range(10)
h = range(10)
print(g  is  h)     # False


#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)     # False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)     # False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)     # True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)     # False


# Find outputs (Home work) - 18/02/2026
print(10 + 20)                                      # 30
print(10.8 + 20.6)                                  # 31.4
print(3 + 4j + 5 + 6j)                              # (8+10j)
print(True + False)                                 # 1
print('Hyder' + 'abad')                             # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')                 # SankarDayalSarma
print('10' + '20')                                  # 1020
print([10 , 20 , 30] + [1 , 2 , 3])                 # [10, 20, 30, 1, 2, 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))# (25, 10.8, 'Hyd', (3+4j), True, None)
print({10 , 20} + {30 , 40})                        # TypeError
print({10 : 'Hyd'} + {20 : 'Sec'})                  # TypeError
print(range(4) + range(5))                          # TypeError
print(10 + '20')                                    # TypeError
print([10 , 20 , 30] + 5)                           # TypeError
print([10 , 20 , 30] + (40 , 50 , 60))              # TypeError


# Find outputs (Home work)
print(25 * 3)                                       # 75
print(10.8 * 25.6)                                  # 276.48
print(True * False)                                 # 0
print((3 + 4j) * (5 + 6j))                          # (-9+38j)
print(3 + 4j * 5 + 6j)                              # (3+26j)
print('25' * 3)                                     # 252525
print(3 * '25')                                     # 252525
print('Hyd' * 4)                                    # HydHydHydHyd
print([10 , 20 , 15] * 2)                           # [10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3)                  # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)                         # TypeError
print({10 , 20 , 15} * 2)                           # TypeError
print({10 : 20 , 30 : 40} * 2)                      # TypeError
print([10] * [20])                                  # TypeError
