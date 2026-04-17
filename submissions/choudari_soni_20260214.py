#  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a)	    #(25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(*a) 	    #25  10.8  'Hyd'  True  3+4j  None  'Hyd'  25
print(type(a))      #<class 'int'>
print(len(a))       #8
print(a[2 : 5])     #a[2 : 5:1] tuple indexes from 2 to 4 insteps of 1 ('Hyd' , True , 3+4j)
print(*a[2 : 5])    #a[2 : 5:1] tuple indexes from 2 to 4 insteps of 1  ('Hyd'  True  3+4j)
a[2] = 'Sec'        #error because we can't replace in tuple
a . append('Sec')   #error because we can't add elements in tuple
a . remove('Hyd')   #error because we can't remove elements in tuple
b =  10 , 20 , 30
print(b)  	    #10 , 20 , 30
print(b * 2)	    #10 , 20 , 30 10 , 20 , 30
c = 40 , 50 , 60,
print(c)	    #40 , 50 , 60,
print(type(c))	    #<class 'tuple'>

______________________________________________________________________________


# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))   #<class 'int'>
print(type(b))	 #<class 'tuple'>
print(type(c))	 #<class 'int'>
print(type(d))	 #<class 'tuple'>
print(a * 4)	 # 100	  
print(b * 4)	 #(25, 25, 25, 25,)
print(c * 4) 	 # 100	
print(d * 4)	 #(25, 25, 25, 25,)


__________________________________________________________________________________


# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a) 		 #('H','y','d')
print(type(a)) 	  	 #<class 'tuple'>
print(len(a))		 #1
b = [10 , 20 , 15 , 18]
print(tuple(b))		 #(10 , 20 , 15 , 18)
print(tuple(range(5)))	 #(0,1,2,3,4)
print(tuple(25))	 #error because integer 25 don't accept the tuple
____________________________________________________________________________________


# Find  outputs (Home  work)
a = ()
print(type(a))		#<class 'int'>
print(a)		#empty tuple
print(len(a))		#0
b = tuple()
print(b)		#empty tuple	
print(len(b))		#0

__________________________________________________________________

# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)			#(10 , 20 , 30)
print(id(a))			#address of object
a = a * 2  #  Valid / Invalid   #valid because tuple can accept the repetation
print(a)			#(10 , 20 , 30,10 , 20 , 30)
print(id(a))			#address of object (10 , 20 , 30,10 , 20 , 30)

