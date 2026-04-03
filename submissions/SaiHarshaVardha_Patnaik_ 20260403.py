# ========================================
# 1. Infinite loop with next(f1())
# ========================================
def f1():
    yield 25
    yield 10.8
    yield 'Hyd'

while True:
    print(next(f1()))  # Output: 25 (then 10.8, 'Hyd', repeats forever)[code_file:1]

# Explanation: Creates new generator each next() call, so infinite loop printing 25, 10.8, 'Hyd' repeatedly.

# ========================================
# 2. Multiple for-loops on same g
# ========================================
def f1():
    yield 25
    yield 10.8
    yield 'Hyd'

g = f1()
for x in g:
    print(x)  # First loop: 25\n10.8\nHyd
for x in g:
    print(x)  # Second: nothing (exhausted)
for x in g:
    print(x)  # Third: nothing[code_file:1]

# Explanation: Generator exhausts after first loop; later loops print nothing.

# ========================================
# 3. Most tricky: mix of next(), for, new gens
# ========================================
import time
def f1():
    yield 25
    yield 10.8
    yield 'Hyd'

g = f1()
print(next(g))  # 25
for x in g:
    print(x)    # 10.8\nHyd
print()
for x in f1():  # New gen
    print(x)    # 25\n10.8\nHyd
print()
gen = f1()      # New gen
print(next(gen)) # 25
for x in f1():  # Another new gen
    print(x)    # 25\n10.8\nHyd
print(next(gen)) # 10.8 (continues first gen)[code_file:1]

# Full output:
# 25
# 10.8
# Hyd
#
# 25
# 10.8
# Hyd
#
# 25
# 25
# 10.8
# Hyd
# 10.8

# ========================================
# 4. Generator assigned to g, two for-loops
# ========================================
import time
g = (x * x for x in range(5))
for y in g:
    print(y)     # 0\n1\n4\n9\n16
    time.sleep(1)
    print('Hello')
for y in g:
    print(y)     # Nothing (exhausted)[code_file:1]

# ========================================
# 5. Inline gens in each for-loop
# ========================================
import time
for y in (x * x for x in range(5)):
    print(y)     # 0 (sleep) 1 (sleep) 4 (sleep) 9 (sleep) 16 (sleep)
    time.sleep(1)
for y in (x * x for x in range(5)):
    print(y)     # 0 (sleep) 1 (sleep) 4 (sleep) 9 (sleep) 16 (sleep)
    time.sleep(1)[code_file:1]

# Explanation: New generator each for-loop, so both print full sequence.

# ========================================
# 6. g1 = g2 (same object)
# ========================================
import time
g1 = (x * x for x in range(5))
g2 = g1
for y in g1:
    print(y)     # 0\n1\n4\n9\n16
    time.sleep(1)
for y in g2:
    print(y)     # Nothing
print(g1 is g2)  # True[code_file:1]

# ========================================
# 7. Drawback of lists (memory hog)
# ========================================
# list = [x * x for x in range(500000000)]  # MemoryError!
# for y in list:
#     print(y)
# Explanation: Tries to store 500M ints in RAM → crash. Bad for huge data.[code_file:1]

# ========================================
# 8. Generator advantage (lazy, no memory issue)
# ========================================
import time
g = (x * x for x in range(1000000000000000000000000000000000000000000000000000000000000000))
while True:
    try:
        print(next(g))  # Prints 0, 1, 4, ... forever, one at a time
        time.sleep(0.5)
    except:
        break  # Never hits exception, runs indefinitely w/o memory crash[code_file:1]

# Key takeaway: Generators are lazy (compute on-demand), memory-efficient for huge/infinite sequences.