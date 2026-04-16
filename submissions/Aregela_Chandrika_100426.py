# Public  and  Private  members  demo  program
class  Test:
	def  _init_(self):
              self.x = 10      #How  to  initialize  public  variable  'x'  to  10
              self.__y = 20    #How  to  initialize  private  variable  'y'  to  20
	
    def  m1(self):
		print('m1  method')
		  print(self.x)      #How  to  print   variable  'x'
          print(self.__y)    #How  to  print  private  variable  'y'
          self.__m2()        #How  to  call    private  method   m2()
		print('Back to m1 method')
	
    def  __m2(self):
		print('__m2  method')
		print(self.x)    #How  to  print   variable  'x'
		print(self.__y)   #How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
ptint(t.x)   #How  to  print  variable  'x'
print(t.Test__y) #How  to  print   variable  'y'
print(t . __y)
print(t . _dict_)
t.m1()     #How  to  call  method  m1()
t._Test__m2()   #How  to  call   method  m2()
t . __m2()
print('End')


# Object  't'  --->








#  Find  outputs
class  c1:
	def _init_(self):
		self.x = 10   #How  to  initialize  public  variable  'x'  with  10
		self.__x = 20 #How  to  initialize  private  variable  'x'  with  20
		self.__x__ = 30 #How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  _m1_(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x)   #How  to  print   variable  'x'
print(a.__x__)     #How  to  print  public  dunder  variable  'x'
print(a.__x)   #How  to  print   private  variable  'x'
print(a . __x)
a.m1()            #How  to  call  public  method  m1()
a.__m1__()        #How  to  call  public  dunder  method  m1()
a.c1.__m1__()             #How  to  call  private  method  m1()
a . __m1()


# Object  'a'   --->










'''  
Find  outputs

Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
'''
class   c1:
	def   _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   _del_(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End  of  the  class
a = c1() # Object  is created at address  1000
a = None # Object  at address 1000 is lost
b = c1() # Object is created at address 2000
del    b # Object at address 2000 is lost
c = c1() # Object is created at address 3000
c = c1() # Object is created at address  4000 and Object at address 3000 is lost
d = c1() # Object is created at address  4000
e = c1() # Object is created at address 5000





# Identify  Error (Home  work)
class   c1:
	def  _del_(self , x):  # Error : destroctor cannot take 2 arhuments
		print('destructor : ' ,  x)
a = c1()
a . _del_(25)






# Find  outputs (Home  work)
class   c1:
	def  _del_(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . _del_(25)






# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor') # destructor ...........
			b = c1()
a = c1()







# Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('constructor') # constructor
		del  self
	def  _del_(self):
		print('destructor')  # destructor
		b = c1()
a = c1()








#  Find  outputs( Home  work)
class   c1:
	def  _del_(self):
		print('1st  destructor')
	def  _del_(self):
		print('2nd  destructor')
	def  _del_(self):
		print('3rd  destructor') # 3rd destructor
# End  of  the  class
a = c1()







#Find  outputs (Home  work)
class   c1:
	def   _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   _del_(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1() # Object is created at address  1000
del   a # ref a is lost
print('Hello') # HHello
del   b # ref b is lost
print('Hi') # hi
del   c # ref c is lost
print('Bye')  # Bye
d = c1() # Object is created at 2000
print('End') # End







# Find  outputs(Home  work)
class  c1:
        def     _init_(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     _del_(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
# End  of  the  class
list = [c1() , c1() , c1()] # object is created 
del  list # Object is lost


'''
Object is created at address : 1000
Object is created at address : 2000
Object is created at address : 3000
Object at address 1000 is lost
Object at address 2000 is lost
Object at address 3000 is lost'''



# Find  outputs  (Home  work)
class   c1:
	def  _del_(self):
		print('destructor') # destructor
		return  25
a = c1() 
print(a . _del_())
print('Hello') # Hello 
del   a






'''
Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

1) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   5 / 9
    What  is  the  sum  ?  ---> 2 / 3 + 5 / 9 =  (18 + 15) / 27 = 33 / 27 =  11 / 9
    What  is  the  difference  ?  --->  2 / 3 - 5 / 9 =  (18 - 15) / 27 = 3 / 27 = 1 / 9
    What  is  the  product  ?  --->  2 / 3 * 5 / 9 =  10 / 27 = 10 / 27
    What  is   the  division  ?  --->  2 / 3 /  5 / 9 = 2 / 3 * 9 / 5 =  18 / 15 =  6 / 5  --->  Succesful  division

2) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   0 / 9
    What  is  the  sum  ?  --->  2 / 3 + 0 / 9 =  (18 + 0) / 27 =  18 / 27 =  2 / 3
    What  is  the  difference  ?  ---> 2 / 3 - 0 / 9 =  (18 - 0) / 27 =  18 / 27 =  2 / 3
    What  is  the  product  ?  --->  2 / 3 * 0 / 9 =  0 / 27  =  0 / 27  --->  Simplification  is  not  required  becoz  numerator  is  0
    What  is   the  division  ?  --->  2 / 3 /  0 / 9 =  2 / 3 * 9 / 0 =  18 / 0  ---> Division  is  not   permitted

3) When  is  simplification  needed ?  --->  When  numerator  is  non-zero
'''
import  math
class  Rat:
	def  get(self):
             self.num = int(input("Enter numerator :")   #How  to  read  numerator  
             self.den = int(input("Enter denominator :")  #How  to  read  denominator 
             self.test()      #How  to  call  test()  method
	def  test(self):
		#Ask  user  to  reenter  denom  when  denom  is  zero
        while self.den = 0:
            print("Denominator cannot be zero. Re-enter:")
            self.den = int(input("Enter Denominator: ")
        
	def    __str__(self):
			 #return  values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
             return f"{self.num} / {self.den}"
	def   add(self , a , b):
		self.num = a.num*b.den + b.num * a.den #How  to  add  objects  'a'  and  'b' and  store  results  in  object  
         if self.num != 0:
            self.simplify()                           #How  to  simplify  object  
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		#How  to  subtract  objects  'a'  and  'b' and  store  results  in  object 
		#How  to  simplify  object  
        self.num = a.num * b.den - b.num * a.den
        self.den = a.den * b.den
        if self.num != 0:
            self.simplify()
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		#How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  
		#How  to  simplify  object 
        self.num = a.num * b.num
        self.den = a.den * b.den
        if self.num != 0:
            self.simplify()
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		#How  to  divide  objects  'a'  and  'b' and  store  results  in  object  
		#How  to  simplify  object 
        if b.num == 0:
            self.num = 0
            self.den = 0
        else:
            self.num = a.num * b.den
            self.den = a.den * b.num
            if self.num != 0:
                self.simplify()

	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
			#How  to  find  gcd  of  numerator  and   denominator
			#How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
        gcd = math.gcd(self.num, self.den)
        self.num //= gcd
        self.den //= gcd
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()
            
if  b.num != 0:
	print("Division =", f)
else:
	print('Division  is  not  permitted')


'''
Object  'a'  --->  

Object  'b'  --->  

Object  'c'  --->  

Object  'd'  --->  

Object  'e'  --->  

Object  'f'  --->  
'''