'''Find  outputs   (Home  work)'''
try:
from threading import Thread
from threading import *
from threading import *
from threading import Thread
from threading import *
from threading import *
  print('Outer   try')
   try:
        print('Inner    try')
        print(7 / 0)   # ZeroDivisionError
        int('Hyd')  # Skipped
        'Hyd'[5]  # Skipped
        eval('Hyd')  # Skipped
    except ZeroDivisionError:
        print('ZDE   of   inner   try')
        int('Ten')  # ValueError
    except ValueError:  # Skipped
        print('ValueError  of  inner  try')
    finally:
        print('Inner  try  finally')
    print('End  of  inner  try')  # Skipped
except ValueError:
    print('ValueError  of  outer  try')
except IndexError:  # Skipped
    print('IndexError  of  outer  try')
except:  # Skipped
    print('default  except  of  outer  try')
finally:
    print('Outer  try  finally')
print('End  of  outer  try')
'''output'''
# Outer   try
# Inner    try
# ZDE   of   inner   try
# Inner  try  finally
# ValueError  of  outer  try
# Outer  try  finally
# End  of  outer  try
'''Find outputs   (Home  work)'''
try:
    print('Outer  try')
    try:
        print('Inner  try')
        int('Hyd')  # ValueError
        'Hyd'[5]  # Skipped
        eval('Hyd')  # Skipped
    except ZeroDivisionError:  # Skipped
        print('ZDE  of  inner  try')
        int('Ten')  # Skipped
    except ValueError:
        print('ValueError  of  inner  try ')
    finally:
        print('Inner  try  finally')
    print('End  of  inner  try')
except ValueError:
    print('ValueError  of  outer try')
except IndexError:
    print('IndexError of outer try')
except:
    print('default except of outer try')
finally:
    print('Outer try finally')
print('End of outer try')
'''output'''
# Outer  try
# Inner  try
# ValueError  of  inner  try
# Inner  try  finally
# End  of  inner  try
# Outer try finally
# End of outer try
''' Find outputs   (Home  work)'''
try:
    print('Outer  try')
    try:
        print('Inner  try')
        'Hyd'[3]  # IndexError
        eval('Hyd')  # Skipped
    except ZeroDivisionError:  # Skipped
        print('ZDE  of  inner  try')
        int('Ten')  # Skipped
    except ValueError:  # Skipped
        print('ValueError  of  inner  try ')
    finally:
        print('Inner  try  finally')
    print('End  of  inner  try')  # Skipped
except ValueError:  # Skipped
    print('ValueError  of  outer  try')
except IndexError:
    print('IndexError  of  outer  try')
except:  # Skipped
    print('default except of outer try')
finally:
    print('Outer try finally')
print('End  of  outer  try')
'''output'''
# Outer  try
# Inner  try
# Inner  try  finally
# IndexError  of  outer  try
# Outer try finally
# End  of  outer  try
''' Find  outputs (Home  work)'''
try:
    print('Outer  try')
    try:
        print('Inner  try')
        eval('Hyd')  # NameError
    except ZeroDivisionError:  # Skipped
        print('ZDE  of  inner  try')
        int('Ten')  # Skipped
    except ValueError:  # Skipped
        print('ValueError  of   inner  try ')
    finally:
        print('Inner  try  finally')
    print('End of inner try')
except ValueError:  # Skipped
    print('ValueError  of  outer try')
except IndexError:  # Skipped
    print('IndexError of outer try')
except:
    print('default  except  of  outer  try')
finally:
    print('Outer  try  finally')
print('End  of  outer  try')
'''output'''
# Outer  try
# Inner  try
# Inner  try  finally
# default  except  of  outer  try
# Outer  try  finally
# End  of  outer  try
'''Find  outputs (Home  work)'''
try:
    print('Outer  try')
    try:
        print('Inner  try')
        print(10 + '20')  # TypeError
    except ZeroDivisionError:  # Skipped
        print('ZDE  of  inner  try')
        int('Ten')  # Skipped
    except ValueError:  # Skipped
        print('ValueError  of   inner  try ')
    finally:
        print('Inner  try  finally')
    print('End of inner try')  # Skipped
except ValueError:  # Ignored
    print('ValueError  of  outer try')
except IndexError:  # Ignored
    print('IndexError of outer try')
finally:
    print('Outer  try  finally')
print('End  of  outer  try')  # Skipped
'''output'''
# Outer  try
# Inner  try
# Inner  try  finally
# Outer  try  finally
''' Find  outputs   (Home  work)'''


class MyError:
    def __init__(self, y):
        self . a = y
        print('Constructor')
# End  of  the  class


def compute(x):
    print(x)
    if x > 20:
        raise MyError(x)
    print('Hello')  # Skipped


# End  of  the function
try:
    compute(10)
    compute(30)
except MyError as msg:
    print('Caught  MyError  outside  :  ',  msg)
print('End')
'''output'''
# 10
# Hello
# 30
# Constructor
# Caught  MyError  outside  :30
# End
''' Find  outputs   (Home  work)'''


class MyError(NameError):
    def __init__(self):
        self . a = 25
        print('Constructor')
# End of  the class


def compute(x):
    print(x)
    if x > 20:
        raise MyError()
    print('Hello')


# End  of  the  function
try:
    compute(30)
    compute(10)
except MyError as msg:
    print('Caught  MyError  outside  :  ',  msg)
print('End')
'''output'''
# 30
# Constructor
# Caught  MyError  outside  : 25
# End
'''Find  outputs (Home  work)'''
try:
    print(1)
    print(2)
    print(3)
except:
    print(4)
else:
    print(5)
finally:
    print(6)
print(7)
'''output'''
# 1
# 2
# 3
# 5
# 6
# 7
'''Find  outputs   (Home  work)'''
try:
    print(1)
    print(7 / 0)  # ZeroDivisionErrror
    print(3)  # Skipped
except:
    print(4)
else:
    print(5)  # Skipped
finally:
    print(6)
print(7)
'''output'''
# 1
# 4
# 6
# 7
'''Find  outputs   (Home  work)'''
try:
    print(1)
    print(7 / 0)  # ZeroDivisionErrror
    print(3)  # Skipped
except:
    int('Two')  # TypeError
else:
    print(5)  # Skipped
finally:
    print(6)
# print(7)
'''output'''
# 1
# 6
'''Find  outputs  (Home  work)'''


class c1:
    def m1(self):
        for i in range(10):
            print('child  thread')


a = c1()
child  = Thread(target=a . m1)
a . m1()
for i in range(10):
    print('main  thread')

''' Find  outputs (Home  work)'''


class c1:
    def m1(self):
        for i in range(10):
            print('child  thread')


a = c1()
child = Thread(target=a . m1())  # Error
child . start()
for i in range(10):
    print('main  thread')

''' Find  outputs  (Home  work)'''


class c1:
    @classmethod
    def m1(cls):
        for i in  range(1, 11):
            print('Child  Thread  :  ', i)  # 10 times


child = Thread(target=c1.m1)
child . start()
for i in  range(1, 11):
    print('Main  Thread  :  ', i)  # 10 times

''' Find  outputs  (Home  work)'''


class Thread:
    def run(self):
        for i in range(10):
            print('Child  Thread')


# End of the class
t = Thread()
t . start()  # Error
for i in range(10):
    print('main  thread')

'''Find  outputs  (Home  work)'''


class Thread:
    def run(self):
        for i in range(10):
            print('Child  Thread')


t = Thread()
t . start()
for i in range(10):
    print('Main  Thread')  # 10 times  Main  Thread


''' Find  outputs  (Home  work)'''


class MyThread(Thread):
    def run(self):
        for i in range(10):
            print('child  thread')    # 10 times  child  Thread


# End  of  the  class
child = MyThread()
child .  run()
for i in range(10):
    print('main  thread')   # 10 times  Main  Thread


'''Find  outputs'''


class MyThread(Thread):
    def run(self):
        print('run  method')


def f1():
    print('f1  function')


new = MyThread(target= f1)
new . start()
print('Main  Thread')
'''output'''
# run method
# Main Thread

''' Find  outputs'''


class MyThread(Thread):
    pass


def f1():
    for i in range(10):
        print('f1  function')


new = MyThread(target = f1)
new . start()
for i in range(10):
    print('Main  Thread')
'''output'''
# 10 times f1 function
# 10 times Main Thread

'''  Find  outputs'''


class MyThread(Thread):
    pass


new = MyThread()
new . start()
for i in range(10):
    print('Main  Thread')  # 10 times Main Thread

''' Find  outputs (Home  work)'''
class MyThread(Thread):
    def walk(self):
        for i in range(10):
            print('walk  method')
child = MyThread()
child . start()
for i in range(10):
    print('Main  Thread')   # 10 times  Main  Thread
