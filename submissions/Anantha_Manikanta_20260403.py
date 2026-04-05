'''
1) def f1():
    yield 25
    yield 10.8
    yield 'Hyd'
# End of generator
while True:
    print(next(f1()))   # 25 <nextline> 25 <nextline> 25 <nextline> ... (infinite)
'''
'''
2) def f1():
    yield 25
    yield 10.8
    yield 'Hyd'
# End of generator
g = f1()
for x in g:
    print(x)   # 25 <nextline> 10.8 <nextline> Hyd
for x in g:
    print(x)
for x in g:
    print(x)
'''
'''
3) import time
def f1():
    yield 25
    yield 10.8
    yield 'Hyd'
# End of generator
g = f1()
print(next(g))
for x in g:
    print(x)
print()
for x in f1():
    print(x)
print()
gen = f1()
print(next(gen))
for x in f1():
    print(x)
print(next(gen))   # 25 <nextline> 10.8 <nextline> Hyd <nextline> <blank line> <nextline> 25 <nextline> 10.8 <nextline> Hyd <nextline> <blank line> <nextline> 25        <nextline> 25 <nextline> 10.8 <nextline> Hyd <nextline> 10.8
'''
'''
4) import time
g = (x * x for x in range(5))
for y in g:
    print(y)
    time.sleep(1)
    print('Hello')
for y in g:
    print(y)   # 0 <nextline> Hello <nextline> 1 <nextline> Hello <nextline> 4 <nextline> Hello <nextline> 9 <nextline> Hello <nextline> 16 <nextline> Hello
'''
'''
5) import time
for y in (x * x for x in range(5)):
    print(y)
    time.sleep(1)
for y in (x * x for x in range(5)):
    print(y)
    time.sleep(1)   # 0 <nextline> 1 <nextline> 4 <nextline> 9 <nextline> 16 <nextline> 0 <nextline> 1 <nextline> 4 <nextline> 9 <nextline> 16
'''
'''
6) import time
g1 = (x * x for x in range(5))
g2 = g1
for y in g1:
    print(y)
    time.sleep(1)
for y in g2:
    print(y)
print(g1 is g2)   # 0 <nextline> 1 <nextline> 4 <nextline> 9 <nextline> 16 <nextline> True
'''
'''
7) list = [x * x for x in range(500000000)]
for y in list:
    print(y)   # Memory Error
'''
'''
8) import time

g = (x * x for x in range(1000000000000000000000000000000000000000000000000000000000000000))

while True:
    try:
        print(next(g))
        time.sleep(0.5)
    except:
        break # 0 <nextline> 1 <nextline> 4 <nextline> 9 <nextline> 16 <nextline> 25 <nextline> ... It works no matter the given value is how much big and not like sequences
'''
'''