def f1():
    yield 25
    yield 10.8
    yield 'Hyd'
# End of generator
while True:
    print(next(f1()))  # 25 And immediately stops with StopIteration except suite



def f1():
    yield 25
    yield 10.8
    yield 'Hyd'
# End of generator
g = f1()
for x in g:
    print(x)  # 25, 10.8, 'Hyd'
for x in g:
    print(x)  # nothing is printed (generator exhausted)
for x in g:
    print(x)  # nothing is printed (generator exhausted)



import time
def f1():
    yield 25
    yield 10.8
    yield 'Hyd'
g = f1()
print(next(g))  # 25
for x in g:
    print(x)      # 10.8, 'Hyd'
print()
for x in f1():
    print(x)      # 25, 10.8, 'Hyd' (new generator creates each time)
print()
gen = f1()
print(next(gen))  # 25
for x in f1():
    print(x)        # 25, 10.8, 'Hyd' (new generator)
print(next(gen))   # 10.8



import time
g = (x * x for x in range(5))
for y in g:
    print(y)      # 0, 1, 4, 9, 16
    time.sleep(1)
    print('Hello')  # After each square (alternatively printed)
for y in g:
    print(y)      # nothing is printed (generator exhausted)



import time
for y in (x * x for x in range(5)):
    print(y)      # 0, 1, 4, 9, 16
    time.sleep(1)
for y in (x * x for x in range(5)):
    print(y)      # 0, 1, 4, 9, 16 (new generator for each loop)
    time.sleep(1)


import time
g1 = (x * x for x in range(5))
g2 = g1
for y in g1:
    print(y)  # 0, 1, 4, 9, 16
    time.sleep(1)
for y in g2:
    print(y)  # nothing is printed(g1 exhausted, g2 is the same generator)
print(g1 is g2)  # True



# Drawback of sequences
list = [x * x for x in range(500000000)]
for y in list:
    print(y)  # prints squares from 0 up to (500000000-1)^2



# Advantage of generator
import time
g = (x * x for x in range(1000000000000000000000000000000000000000000000000000000000000000))
while True:
    try:
        print(next(g))  # 0, 1, 4, 9, ... infinite
        time.sleep(0.5)
    except:
        break