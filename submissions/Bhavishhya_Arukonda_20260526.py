#  Find  outputs  (Home  work)
from  threading  import  RLock
r = RLock()
r . acquire()
print('Locked')  # Locked
r . acquire()
print('Locked')  # Locked
r . release()
print('Unlocked')  # Unlocked
r . release()
print('Unlocked')  # Unlocked
r . release()   # Error
print('End') # End



# Find  outputs  (Home  work)
from threading import *
l = Lock()
l . acquire()
print('Locked')  # locked
l . acquire() 
print('Locked')  # waiting time 
l . release()
print('Unlocked')  # Unlocked
l . release()
print('Unlocked')  # error
print('End')  # End