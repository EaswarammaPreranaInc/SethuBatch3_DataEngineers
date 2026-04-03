#1
# Tricky program
# Find outputs (Home work)
def f1():
    yield 25
    yield 10.8
    yield 'Hyd'
# End of generator
while True:
    print(next(f1())) # Output: 25, 25, 25, 25... (Infinite Loop)



#2
# Find outputs (Home work)
def   f1():
    yield 25
    yield 10.8
    yield 'Hyd'
# End of generator
g = f1()
for x in g:
    print(x) # 25, 10.8, Hyd (Generator g is now empty/exhausted)
for x in g:
    print(x) # (No Output) - Reason: g was already exhausted in the first loop.
for x in g:
    print(x) # (No Output)



#3
# Most tricky program
# Find outputs (Home work)
import time
def f1():
    yield  25
    yield  10.8
    yield  'Hyd'
# End of generator
g = f1()
print(next(g))    # 25
for x in g:
    print(x)      # 10.8, Hyd (Starts from where 'next' left off)
print()           # (Empty line)
for x in f1():
    print(x)      # 25, 10.8, Hyd (f1() creates a new or fresh generator)
print()           # (Empty line)
gen = f1()
print(next(gen))  # 25
for x in f1():    
    print(x)      # 25, 10.8, Hyd (Uses a completely different generator)
print(next(gen))  # 10.8 (Continues from the 'gen' instance started before)



#4
# Find outputs (Home work)
import time
g = (x * x for x in range(5))
for y in g:
    print(y)          # 0
    time . sleep(1)
    print('Hello')    # Hello (Then 1, Hello, 4, Hello, 9, Hello, 16, Hello)
for y in g:
    print(y)          # (No Output) because g is already exhausted.



#5
# Find outputs (Home work)
import time
for y in (x * x for x in range(5)):
    print(y)                           # 0, 1, 4, 9, 16
    time . sleep(1)
for y in (x * x  for x in range(5)):
    print(y)                           # 0, 1, 4, 9, 16
    time . sleep(1)



#6
# Find outputs(Home work)
import time
g1 = (x * x for x in range(5))
g2 = g1
for y in g1:
    print(y)          # 0, 1, 4, 9, 16
    time . sleep(1)
for y in g2:
    print(y)          # (No Output) because g1 and g2 share the same state.
print(g1 is g2)       # True



#7
# Drawback of sequences 
# list = [x * x for x in range(500000000)]
# MemoryError as a List Comprehension (using []) tries to build the entire list in RAM at once. 
# 500 million elements will consume gigabytes of memory, likely crashing the program.
# for y in list:
#     print(y)



#8
# Advantage of generator?
import time
g = (x * x for x in range(1000000000000000000000000000000000000000000000000000000000000000))
# Generators only calculate one value at a time (on demand). The size of the 'range' doesn't matter for memory.
while True:
    try:
        print(next(g))     # 0, 1, 4, 9, 16...
        time . sleep(0.5)
    except:
        break