# float  object  demo  program (Home  work)
a = 10.8  ---> # float class object.
print(a) ---> # Adress of object
print(type(a)) ---> # Reference
print(id(a)) ---> #may be 1000
b = 25. ---> # int class object
print(b) ----> #Adress of object
print(type(b)) ----> # Reference 
c = .689 ----> # Error because decimal point is in front
print(c) ---> # Error
d = 3.4E2 ---> # Error because E is in middle 
print(d) ----> # error
print(type(d)) ---> #Error
e = 9.62e-2 ----> # Error because e and -2 are not  in float
print(e) ----> # Error
print(9.8.2) ---> Error

# Find outputs (Home work)
a = 6j --> # Error because no real in class object
print(a) ---> # Error because dont have real 
print(type(a)) ---> # Error
print(a.real) ----> # Error 
print(a.imag) ---> # Error 
print(5 + j6)  ---> # Error because imag j is valid after numbers 
print(3 + 4i)  ----> # 3.0 and 4.0
print(4+j)  ---> # Error because only j is there no number in front of j
print(4 + 1j) ----> # 4.0 and 1.0
print(4 + 0j) ---> # 4.0 and 0.0

# bool object demo program  (Home  work)
a = True ---> # bool class object
print(a) ----> adress of bool class object
print(type(a)) ---> Reference of object
print(id(a)) ---> may be 3000
b = False --->  # bool class object
print(b) ---> # adress of bool object
print(type(b)) ---># referemce of object
print(True + True) ---> # its a decimal value bool comaparsion to decimal  1+1 = 3.
print(True + False)---> # its a decimal vallue bool comparision to decimal 1+0 = 2.
print(False + True) ---> # its a decimal vallue bool comparision to decimal 0+1 = 1.
print(False + False) ----> # its a decimal vallue bool comparision to decimal 0+0 = 0.
print(True + True + True) ----> #  its a decimal vallue bool comparision to decimal 1+1+1 = 7.
print(25 + 10.8 + True) ----> # Error  because it have int and float
print(True > False)  ---> # Error because it have special character 
print(True) ----> # True  
print(False) ---> # False 
print(true) ---> # Error t is small should be in capital T , True is a keyword
print(false)---> # Error f is small should be in capital  F, False is a keyword

# Find  outputs (Home  work)
a = 0O6247 ---> #Octal decimal number range (0-7) weight is 8
print(a) ----> #Address of octal class object
print(type(a)) ----> #Reference of object
print(id(a))  ----> #may be 43000
b = 0o6247 ----> # Octal decimal number range (0-7) weight is 8 
print(id(b)) ---->  #Address of octal class object
print(b) ---->  #reference of object
c = 3239 ----> # error because octal decimal contain (0-7) there is 9 in c object
print(c) ----> # Error 
print(id(c)) ----># Error 
print(0o9248) ---> Error because alphabet o and 9 and 8 are present

# Find  outputs  (Home  work)
a = 0XA7B9 ---> # it is hexa decimal number
print(a) ----> #  its a hexa decimal convert to  decimal number then object of a is 107129
print(type(a)) ---> # it is reference 
b = 0xBEEF ---->  # it is hexa decimal number
print(b) --->  #  its a hexa decimal convert to  decimal number then object of a is
print(A7B9)  ---> # Error no prifix 
print('A7B9')---> #Error no prifix and there is comments
print(0XBEER) --->   # Error hexa decimal contains (0-9)(A-F) total 16 R is not valid                                                      print(0XHYD) ----> # Error hexa decimal contains (0-9)(A-F) total 16 Y is not valid  
print(0xA7G9B)---># Error hexa decimal contains (0-9)(A-F) total 16 G is not valid

