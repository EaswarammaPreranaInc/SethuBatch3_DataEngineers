# float  object  demo  program (Home  work)
a = 10.8
print(a)		#10.8
print(type(a))	#class float
print(id(a))		#address of the reference a will be printed lets assume 1000
b = 25.
print(b)		#25
print(type(b))	#class int
c = .689		
print(c)		#0.689
d = 3.4E2
print(d)		#360.0
print(type(d))	#class float
e = 9.62e-2
print(e)		#0.0962
print(9.8.2)		#ERROR

# complex object demo program
a = 3 + 4j
print(a)		# 3 + 4j
print(type(a))	# class complex
print(id(a))		# address of the reference a will be printed lets assume 2000
print(a . real)	# 3.0
print(a . imag)	# 4.0
print(type(a . real)) # class float
print(type(a . imag)) # class float




# Find outputs (Home work)
a = 6j
print(a)		# 6j
print(type(a))	# class complex
print(a.real)		# 0.0
print(a.imag)	# 6.0
print(5 + j6)  	# ERROR because imag number is last
print(3 + 4i) 	# ERROR because in complex j is used i is a reference 
print(4+j) 		# ERROR because no imag number is given
print(4 + 1j)		# 4 + 1j
print(4 + 0j)		# 4 + 0j
# bool object demo program  (Home  work)
a = True
print(a)			# True
print(type(a))		# class bool
print(id(a))			# address of the reference a will be printed lets assume 3000
b = False
print(b)			# False
print(type(b))		# class bool
print(True + True)		# 2
print(True + False)		# 1
print(False + True)		# 1
print(False + False)	# 0
print(True + True + True)	# 3
print(25 + 10.8 + True)	# 36.8
print(True > False)  	# True
print(True)			# True
print(False)			# False
print(true)			# Error in true T should be capital
print(false)			# Error in False F should be capital
# Find  outputs (Home  work)
a = 0O6247
print(a)		# 3239
print(type(a))	# class int
print(id(a))  		# address of the reference a will be printed lets assume 4000
b = 0o6247
print(id(b))		# address of the reference b will be printed lets assume 5000
print(b)		# 3239
c = 3239
print(c)		# 3239
print(id(c))		# address of the reference a will be printed lets assume 6000
print(0o9248)	# Error because ‘9’ is not valid octal number

# Find  outputs  (Home  work)
a = 0XA7B9
print(a) 			# 42937
print(type(a))		# class int
b = 0xBEEF
print(b) 			# 48879
print(A7B9)  		# Error as it’s not defined 
print('A7B9')		# A7B9
print(0XBEER)		# Error X is not defined
print(0XHYD)		# Error X is not defined
print(0xA7G9B)		# Error X is not defined

# Find outputs (Home  work)
a = 9248
print(a)			# 9248
print(type(a))		# class int
