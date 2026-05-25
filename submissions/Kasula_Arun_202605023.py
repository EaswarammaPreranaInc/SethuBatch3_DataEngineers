# 1
t1.start()    # prints "f1 function" 10 times

# 2
t2.start()    # prints "m1 method of class c1" 10 times

# 3
t3.start()

# 4
t4.start()    # prints "run method of MyThread class" 10 times

# 5
t5.start()    # prints "run method of MyThread class" 10 times

# 6
t6.start()    # prints "f1 function" 10 times

# 7
t7.start()

# 8
t8.start()    # prints "run method of MyThread class" 10 times

# 9
t9.start()    # prints "m1 method of class c1" 10 times

# 10
t10.start()   # prints "run method of MyThread class" 10 times

# 11
t11.start()

# 12
t12.start()   # prints "m1 method of MyThread class" 10 times

# 13
t13.start()   # prints "f1 method of class c1" 10 times


# overriding start()

child.start()

# Run Method
# Start Method
# Main Thread


# main thread names

from threading import *

main = current_thread()

print(main.name)             # MainThread

main.name = 'Hyd'

print(main.name)             # Hyd

t = Thread(name='Sec')

print(t.name)                # Sec

t.name = 'Cyb'

print(t.name)                # Cyb

print(active_count())        # 1


# three threads

t1 = Thread()
t2 = Thread()
t3 = Thread()

print(t1.name)               # Thread-1
print(t2.name)               # Thread-2
print(t3.name)               # Thread-3

t1.name = 'One'
t2.name = 'Two'
t3.name = 'Three'

print(t1.name)               # One
print(t2.name)               # Two
print(t3.name)               # Three

print(active_count())        # 1


# child thread name

def f1():
    print(current_thread().name)    # child

t = Thread(target=f1, name='child')

t.start()

print(current_thread().name)        # MainThread


# rename threads

t1 = Thread(name='Hyd')
t2 = Thread()

print(current_thread().name)    # MainThread
print(t1.name)                  # Hyd
print(t2.name)                  # Thread-1

current_thread().name = 'India'

t1.name = 'Sec'
t2.name = 'Cyb'

print(current_thread().name)    # India
print(t1.name)                  # Sec
print(t2.name)                  # Cyb

print(active_count())           # 1


# infinite loop threads

t1.start()
t2.start()

# Hyd : 10
# Sec : 20
# Hyd : 10
# Sec : 20
# ...


# random guess program

t1.start()
t2.start()

# Rama guess 32 in attempt : 1
# Rama guess 75 in attempt : 2
# Rama finish in 2 attempts

# Sita guess 11 in attempt : 1
# Sita guess 50 in attempt : 2
# Sita finish in 2 attempts