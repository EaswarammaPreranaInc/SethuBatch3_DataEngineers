''' Find  outputs (Home  work)'''
import time
from threading import *
import time
from threading import *
from threading import *


def disp():
    for i in range(10):
        print('child  thread')


# End  of  the  function
child = Thread(target=disp)
child . start()  # print child may be 10 times ------>  thread
child . join()  # main thread waits for termination or dead of child thread then after main thread goes to the ready state then T.S and wait for  T.S to selete it to execute
for i in range(10):
    print('main  thread')  # prints 10 times  --->     main  thread


'''Find  outputs (Home  work)'''


def disp():
    for i in range(10):
        print('child  thread')
        time . sleep(2)


#  End  of  the  function
child = Thread(target=disp)
child . start()  # executes the  target disp() for 10 sec's or untill termination of child ,in other words which ever come first
# main thread goes under waiting statefor 10 sec's or untill termination of child ,in other words which ever come first
child . join(10)
for i in range(10):  # after 10 sec or termination of child the main thread gets the chance to execute
    print('main  thread')

''' outputs'''
# child  thread---5 times
# main  thread--2 times
# child  thread--1 time
# main  thread--5 times
# child  thread--4 time
# main  thread--3 times

'''Find  outputs (Home work)'''
main = main_thread()  # main thread object
name = main . name  # MainThread
print(name, ' is started')  # MainThread is started
main . join()  # error main thread can wait for child thread but cant wait for itself untill it terminates so error
# if we comented  'main . join()' then  output is MainThread is ended
print(name, 'is ended')

''' Find  outputs (Home  work)'''


def double():
    for i in range(1, 7):
        print('Double : ', 2 * i)
        time . sleep(1)


def square():
    for i in range(1, 7):
        print('Square : ', i * i)
        time . sleep(1)


start = time . time()  # time from 1970-01-01 12:00 pm(epoch time ) to now in seconds
double()  # Double : 0 <nxtline>  Double : 2  <nxtline>  Double : 4 <nxtline>  Double : 6 <nxtline>  Double : 8  <nxtline>  Double : 10 <nxtline>  Double : 12
square()  # Square :0 <nxtline> Square :1  <nxtline> Square :4 <nxtline> Square :9  <nxtline> Square :16 <nxtline> Square 25 <nxtline> Square :36
end = time . time()  # time from 1970-01-01 12:00 pm(epoch time ) to now in seconds
print(end - start)  # execution time for the functions 'square() and double()'

'''Find  outputs  (Home  work)'''


def display():
    name = current_thread() . name
    print(name, ' is  started')
    time . sleep(3)
    print(name, ' is  ended')


# End  of  the  function
print(active_count())
t1 = Thread(target=display, name='One')
t2 = Thread(target=display, name='Two')
t3 = Thread(target=display, name='Three')
print(active_count())  # 1
t1 . start()
t2 . start()
t3 . start()
print(active_count())
t1 . join()
t2 . join()
t3 . join()
print(active_count())

# outputs :
# One is started <nxtline >One is ended ----------- may be 4 times
# Two is started <nxtline >Two is ended ----------- may be 7 times
# Three is started <nxtline >Three is ended ----------- may be 4 times
# 4
# One is started <nxtline >One is ended ----------- may be 6 times
# Two is started <nxtline >Two is ended ----------- may be 3 times
# Three is started <nxtline >Three is ended ----------- may be 6 times
# 1


''' Find  outputs  (Home  work)'''


def disp():
    name = current_thread() . name
    print(name, ' is  started')
    time . sleep(3)
    print(name, '  is  ended')


# End  of  the  function
t1 = Thread(target=disp, name='One')
t2 = Thread(target=disp, name='Two')
t3 = Thread(target=disp, name='Three')
t1 . start()
t2 . start()
t3 . start()
list = enumerate()
for t in list:
    print(t . name)
t1 . join()
t2 . join()
t3 . join()
list = enumerate()
for t in list:
    print(t . name)

# outputs :
# outputs -- vary from run to run

# One is started
# Two is started
# Three is started
# MainThread
# One
# Two
# Three
# One is ended
# Two is ended
# Three is ended
# MainThread

# before join()
# enumerate() returns 4 active threads
# MainThread
# One
# Two
# Three

# after join()
# only MainThread remains active
# enumerate() returns 1 active thread


''' is_alive()  method   demo  program'''


def disp():
    name = current_thread() . name
    print(name, 'is   started')
    time . sleep(3)
    print(name, '   is    ended')


t1 = Thread(target=disp, name='One')
t2 = Thread(target=disp, name='Two')
t3 = Thread(target=disp, name='Three')
t1 . start()
t2 . start()
t3 . start()
print(t1 . is_alive())  # True
print(t2 . is_alive())  # True
print(t3 . is_alive())  # True
t1 . join()
t2 . join()
t3 . join()
print(t1 . is_alive())  # False
print(t2 . is_alive())  # False
print(t3 . is_alive())  # False

#   outputs  :
# One is started
#  Two is started
# Three is started
# True
# True
# True
# Three is ended
# One is ended
# Two is ended
# False
# False
# False
# before join()
# t1.is_alive() --> True
# t2.is_alive() --> True
# t3.is_alive() --> True
# after join()
# t1.is_alive() --> False
# t2.is_alive() --> False
# t3.is_alive() --> False

''' Find  outputs (Home  work)'''


def table(n):
    print('Table  :  ', n)
    for i in range(1, 11):
        print(F'{n}  *  {i}    =   {n * i}')
        time . sleep(1)


#  End  of  the  function
t1 = Thread(target=table, args=(7,))
t2 = Thread(target=table, args=(4,))
t1 . start()
t2 . start()

# outputs -- vary from run to run
# because both threads execute simultaneously
# time.sleep(1)
# pauses current thread for 1 second
# so thread scheduler switches between threads frequently

# Table : 4
# 4 * 1 = 4
# Table : 7
# 7 * 1 = 7
# 4 * 2 = 8
# 7 * 2 = 14
# ...
# 4 * 10 = 40
# 7 * 10 = 70
# t1 executes table(7)
# t2 executes table(4)
