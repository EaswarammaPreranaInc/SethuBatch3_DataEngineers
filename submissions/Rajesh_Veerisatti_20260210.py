# float  object  demo  program (Home  work)
a = 10.8
print(a) # 10.8
print(type(a)) # float class object
print(id(a)) # address id of object    ( which is given in .py )
b = 25.
print(b) # 25.0
print(type(b)) # float
c = .689
print(c) # 0.689
d = 3.4E2
print(d) # 340.0
print(type(d)) # float class object 
e = 9.62e-2
print(e) # 0.0962
# print(9.8.2)  # error(it contains two decimal point so it does not accept by PVM)


# complex object demo program
a = 3 + 4j
print(a) # 3+4j
print(type(a)) # complex class object 
print(id(a)) # address of the object "a" ( Which is given by .py)
print(a . real) # 3.0
print(a . imag) # 4.0
print(type(a . real)) # float class object 
print(type(a . imag)) # float class object


# Find outputs 
a = 6j
print(a) # 0+6j
print(type(a)) # complex class object 
print(a.real) # 0.0
print(a.imag) # 6.0
# print(5 + j6)  # error( before the imag "j" is not valid in .py)
# print(3 + 4i) # error ( "i" is not value in .py in .py there is using "j")
# print(4+j) # error ( there is no imäg)
print(4 + 1j) # 4+1j
print(4 + 0j) # 4+0j


# bool object demo program 
a = True
print(a) # True
print(type(a)) # bool class object 
print(id(a)) # address of the object "a" (given by .py)
b = False
print(b) # Flase
print(type(b)) # bool class object
print(True + True) # 2
print(True + False) # 1
print(False + True) # 1
print(False + False) # 0
print(True + True + True) # 3
print(25 + 10.8 + True) # 36.8
print(True > False)  # True
print(True) # True
print(False) # Flase
# print(true) # error ( " True" and " Flase" are keywords in .py so it must be start withuppercase latters "True" and "Flase")
#print(false) # error ( " True" and " Flase" are keywords in .py so it must be start withuppercase latters "True" and "Flase")




# Find  outputs (Home  work)
a = 0O6247
print(a) # 3239
print(type(a)) # octa decimal integer class object 
print(id(a))  # address of the object " a" given by .py
b = 0o6247
print(id(b)) # address of the object " b" given by .py ( same address of object "b")
print(b) # 3239
c = 3239
print(c) # 3239
print(id(c))# same address for the object "a"
# print(0o9248) # error  9 and 8 is invalid ( octa decimal int class contains o to 7 only)


# Find  outputs  
a = 0XA7B9
print(a) # 42937
print(type(a)) # hexa decimal int class object 
b = 0xBEEF 
print(b) # 48879
# print(A7B9)  # error ( bcz name of the object it does mean invalid in .py)
print('A7B9') # A7B9
# print(0XBEER)# error (In hexa decimal int "R" is not valid)
# print(0XHYD)# error bcz of HY ( hexa decimal int class object contains only 0 to 9 and (A to F )in upcase )
# print(0xA7G9B) # error bcz of G ( hexa decimal int class object contains only 0 to 9 and (A to F )in upcase )



# Find outputs 
a = 9248
print(a) # 9248
print(type(a)) # int class object