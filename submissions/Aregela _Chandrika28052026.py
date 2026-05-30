from threading import *
import time

def f1():
    with l1:
        time.sleep(1)

        with l2:
            print('1st thread is under execution')

    print('End of the 1st thread')


def f2():
    with l1:
        time.sleep(1)

        with l2:
            print('2nd thread is under execution')

    print('End of the 2nd thread')


# Locks
l1 = Lock()
l2 = Lock()
# Threads
t1 = Thread(target=f1)
t2 = Thread(target=f2)
# Start threads
t1.start()
t2.start()
# Wait for expiry 
t1.join()
t2.join()

print('End of main thread')


#-------------------



